from decimal import Decimal
from django.conf import settings
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

    cart = request.session.get('cart', {})

    discount_applied = request.session.get('discount_applied')

    for item, quantity in cart.items():
        # Use string created in cart view to isolate model ids
        product_id = item.split("_")[0]
        size_id = item.split("_")[1]
        nic_id = item.split("_")[2]
        # Retrieve relevant objects for templating
        product = get_object_or_404(Product, pk=product_id)
        size = get_object_or_404(Size, pk=size_id)
        nic = get_object_or_404(Nicotine, pk=nic_id)
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
