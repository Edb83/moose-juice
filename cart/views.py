from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ A view to return the shopping cart contents """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the chosen product (inc options) to the shopping cart """

    product = Product.objects.get(pk=item_id)
    size_id = request.POST.get('size')
    nic_id = request.POST.get('nic')
    # Create string representing item and options chosen for contexts.py
    item = f'{item_id}_{size_id}_{nic_id}'
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item in list(cart.keys()):
        cart[item] += quantity
        messages.success(request, f'Added more {product.name}')
    else:
        cart[item] = quantity
        messages.success(request, f'Added {product.name}')

    request.session['cart'] = cart
    return redirect(redirect_url)


# Want to update whole cart on form submit
def update_cart(request, item_id):
    """ Update quantity of the chosen product in shopping cart """

    product = Product.objects.get(pk=item_id.split('_')[0])
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {product.name}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name}')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove chosen product from shopping cart """

    product = Product.objects.get(pk=item_id.split('_')[0])
    cart = request.session.get('cart', {})

    try:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name}')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)


def toggle_discount(request):
    discount_applied = request.session.get('discount_applied', False)
    request.session['discount_applied'] = not discount_applied
    
    return redirect(reverse('view_cart'))
