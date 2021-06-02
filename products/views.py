from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.db.models import F, Q
from django.db.models.functions import Lower

from .models import Product, Brand, Category, ProductReview
from profiles.models import UserProfile

from .forms import ProductForm, ReviewForm

from checkout.models import OrderLineItem


def all_products(request):
    """ A view to return all Products """

    products = Product.objects.all()
    sort = None
    direction = None
    sale = False
    brand = None
    category = None
    query = None

    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user_id=request.user)
    else:
        profile = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'average_rating':
                # F used to leave nulls last in Postgres queries
                products = products.order_by(F(
                    'average_rating').desc(nulls_last=True))
            else:
                if sortkey == 'name':
                    sortkey = 'lower_name'
                    products = products.annotate(lower_name=Lower('name'))

                if 'direction' in request.GET:
                    direction = request.GET['direction']
                    if direction == 'desc':
                        sortkey = f'-{sortkey}'
                products = products.order_by(sortkey)

        if 'sale' in request.GET:
            sale = True
            products = products.filter(on_sale=True)

        if 'brand' in request.GET:
            brand = request.GET['brand']
            products = products.filter(brand__name=brand)
            brand = get_object_or_404(Brand, name=brand)

        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name=category)
            category = get_object_or_404(Category, name=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You forgot to put the words in!")
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(tags__name__icontains=query)
                )

            # distinct disregards duplicate rows across tables
            products = products.filter(queries).distinct()

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'sale': sale,
        'brand': brand,
        'profile': profile,
        'category': category,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to return individual Product details and a form for
    submitting product reviews and ratings
    """

    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm()

    context = {
        'product': product,
        'form': form,
        'on_product_detail_page': True,
    }

    return render(request, 'products/product-detail.html', context)


@login_required
def favourites(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    products = profile.favourites.all()
    template = 'products/favourites.html'
    context = {
        'products': products,
    }

    return render(request, template, context)


@login_required
def toggle_favourite(request, product_id):

    profile = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    data = {
        'is_favourite': profile.favourites.filter(pk=product_id).exists(),
        'is_authenticated': request.user.is_authenticated,
    }

    if profile.favourites.filter(pk=product_id).exists():
        profile.favourites.remove(product)
    else:
        profile.favourites.add(product)

    return JsonResponse(data)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, you don't have the necessary permissions to do that.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.info(request, 'Product added')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to add product - please check form and try again")

    else:
        form = ProductForm()

    template = 'products/add-product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    """

    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, you don't have the necessary permissions to do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.info(request, f'Updated {product.name}')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update product - please check form and try again")

    else:
        form = ProductForm(instance=product)

    template = 'products/edit-product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store
    """

    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, you don't have the necessary permissions to do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product_name = product.name
    # Save reviews for later removal
    reviews = product.reviews.all()
    # Delete the product, SET_NULL on delete will take effect
    product.delete()
    # Delete all reviews
    # Signal will still fire to update_rating if product exists
    reviews.delete()
    messages.info(request, f'{product_name} deleted')

    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """ Add a review for a product """
    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user_id=request.user)
    else:
        profile = None

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            reviews = product.reviews.all()

            if reviews.filter(user=request.user).exists():
                messages.info(
                    request, f"You've already reviewed {product.name}")
                return redirect(reverse('product_detail', args=[product.id]))

            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                # Check whether line items related to user include the product
                if OrderLineItem.objects.filter(
                    order__user_profile=profile).filter(
                        product=product).exists():
                    review.verified_purchase = True

                review.save()
                if review.verified_purchase:
                    messages.info(
                        request,
                        'Thanks for the review - 5 points to you!')
                else:
                    messages.info(
                        request,
                        'Thanks for the review!')

                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(
                    request,
                    "Failed to add review - please check form and try again")

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, context)


@login_required
def edit_review(request, review_id):
    """
    Edit a product review
    """
    review = get_object_or_404(ProductReview, pk=review_id)
    product = review.product

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated review')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update review - please check form and try again")

    else:
        form = ReviewForm(instance=review)

    messages.info(request, f"You are editing your review of {product}.")
    template = 'products/product-detail.html'
    context = {
        'form': form,
        'review': review,
        'product': product,
        'edit': True,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """
    Delete a user's product review
    """

    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, you don't have the necessary permissions to do that.")
        return redirect(reverse('home'))

    review = get_object_or_404(ProductReview, pk=review_id)
    product = review.product
    review_owner = review.user
    review.delete()
    messages.info(request, f"Deleted {review_owner}'s review")

    return redirect(reverse('product_detail', args=[product.id]))
