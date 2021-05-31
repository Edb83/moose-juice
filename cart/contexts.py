from decimal import Decimal
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404
from products.models import Product, Size, Nicotine
from profiles.models import UserProfile
import math


def cart_contents(request):

    cart_items = []
    total = 0
    savings = 0
    product_count = 0
    points_available = 0
    points_earned = 0
    discount_applied = request.session.get('discount_applied')
    cart = request.session.get('cart', {})

    # Create a new dict so that items can be removed if needed
    new_dict = {k: v for k, v in cart.items()}

    for item, quantity in new_dict.items():
        # Use string created in cart view to isolate model ids
        product_id = item.split("_")[0]
        size_id = item.split("_")[1]
        nic_id = item.split("_")[2]

        # Retrieve relevant objects for templating and remove if
        # no longer in database
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            del cart[item]
            messages.error(request, 'An item was removed from your cart as it is \
                no longer available. Try to find a worthy replacement!')
            continue

        try:
            size = Size.objects.get(pk=size_id)
        except Size.DoesNotExist:
            del cart[item]
            messages.error(request, 'An item could not be added as its \
                size is no longer available. Try to find a worthy replacement!')
            continue

        try:
            nic = Nicotine.objects.get(pk=nic_id)
        except Nicotine.DoesNotExist:
            del cart[item]
            messages.error(request, 'An item could not be added as its \
                nicotine options have changed. Try to find a worthy replacement!')
            continue

        # Check sale status and retrieve relevant price from Size model
        if product.on_sale:
            price = size.sale_price
            savings += (size.price - size.sale_price) * quantity
        else:
            price = size.price
        total += quantity * price
        product_count += quantity
        cart_items.append({
            'item_id': item,
            'product': product,
            'size': size,
            'nic': nic,
            'price': price,
            'quantity': quantity,
        })

    original_total = total
    request.session['cart'] = cart

    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user_id=request.user)

    else:
        profile = None

    if profile:
        points_available = profile.points

    if discount_applied:
        if total - Decimal(points_available / 100) <= 0:
            total = 0

        else:
            total -= Decimal(points_available / 100)

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.STANDARD_DELIVERY)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total

    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total
    points_earned = int(math.floor(total))

    context = {
        'cart_items': cart_items,
        'total': total,
        'original_total': original_total,
        'savings': savings,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'points_available': points_available,
        'discount_applied': discount_applied,
        'points_earned': points_earned,
    }

    return context
