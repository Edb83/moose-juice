from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q  # for handling complex queries
from django.db.models.functions import Lower
from .models import Product, Brand, Category
from .forms import ProductForm, ReviewForm


def all_products(request):
    """ A view to return all Products """

    products = Product.objects.all()
    sort = None
    direction = None
    sale = False
    brand = None
    category = None
    query = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
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

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Review added')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add review - please check form and try again')
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'products/product-detail.html', context)


def add_product(request):
    """ Add a product to the store """

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully added')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product - please check form and try again')

    else:
        form = ProductForm()

    template = 'products/add-product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """
    Edit a product in the store
    """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product - please check form and try again')
    
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit-product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
