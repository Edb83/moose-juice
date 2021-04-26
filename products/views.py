from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q  # for handling complex queries
from .models import Product, Brand, ProductProfile


def all_products(request):
    """ A view to return all Products """

    products = Product.objects.all()
    brand = None
    query = None
    profile = None

    if request.GET:
        if 'brand' in request.GET:
            brand = request.GET['brand']
            products = products.filter(brand__name=brand)
            brand = get_object_or_404(Brand, name=brand)

        if 'profile' in request.GET:
            profile = request.GET['profile']
            products = products.filter(profile__name=profile)
            profile = get_object_or_404(ProductProfile, name=profile)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You forgot to put the words in!")
                return redirect(reverse('products'))
            # Need to amend to search on flavours
            queries = (
                Q(name__icontains=query) | Q(description__icontains=query))
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'brand': brand,
        'profile': profile,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to return individual Product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product-detail.html', context)
