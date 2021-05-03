from django.shortcuts import render, redirect, reverse, HttpResponse


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


def update_cart(request, item_id):
    """ Update quantity of the chosen product in shopping cart """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove chosen product from shopping cart """

    cart = request.session.get('cart', {})

    try:
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
