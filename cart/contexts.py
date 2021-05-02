from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Size, Nicotine


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item, quantity in cart.items():
        # Use string created in cart view to isolate model ids
        product_id = item.split("_")[0]
        size_id = item.split("_")[1]
        nic_id = item.split("_")[2]
        # Retrieve relevant objects for templating
        product = get_object_or_404(Product, pk=product_id)
        size = get_object_or_404(Size, pk=size_id)
        nic = get_object_or_404(Nicotine, pk=nic_id)
        # Check sale status and retrieve relevant price from Size
        if product.on_sale:
            price = size.sale_price
        else:
            price = size.price
        total += quantity * price
        product_count += quantity
        cart_items.append({
            'item_id': product_id,
            'size_id': size_id,
            'nic_id': nic_id,
            'product': product,
            'size': size,
            'nic': nic,
            'price': price,
            'quantity': quantity,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
