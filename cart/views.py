from django.shortcuts import render, redirect


def view_cart(request):
    """ A view to return the shopping cart contents """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the chosen product (inc options) to the shopping cart """

    size = request.POST.get('size')
    nic = request.POST.get('nic')
    # Create string representing item and options chosen for contexts.py
    item = f'{item_id}_{size}_{nic}'
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item in list(cart.keys()):
        cart[item] += quantity
    else:
        cart[item] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
