from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q  # for handling complex queries
from django.db.models.functions import Lower
from .models import Product, Brand, Category


def all_products(request):
    """ A view to return all Products """

    products = Product.objects.all()
    brand = None
    query = None
    category = None
    sort = None
    direction = None

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
            # Need to amend to search on flavours

            queries = (
                Q(friendly_name__iexact=query) |
                # Q(description__icontains=query)
                Q(tags__name__iexact=query)
                )

            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'brand': brand,
        'category': category,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to return individual Product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product-detail.html', context)
