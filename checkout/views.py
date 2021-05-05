from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IGZ1CKZPwRGOjxvsVa1O850xKX7d8z8twXJdLqtG9cFzNM3I0xWKdCqaN05XVDpqN8mnn8fFzYLqXlDYaZ2pkVA00Riip31vA',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
