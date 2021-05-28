import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from decimal import Decimal

from django_countries.fields import CountryField

from products.models import Product, Size, Nicotine
from profiles.models import UserProfile
from rewards.models import Reward


class Order(models.Model):
    class Meta:
        ordering = ['-id']

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')
    points_redeemed = models.IntegerField(null=True, blank=True)
    points_earned = models.IntegerField(null=True, blank=True, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0

        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = Decimal(settings.STANDARD_DELIVERY)
        else:
            self.delivery_cost = 0

        if self.points_redeemed:
            reward_base = getattr(Reward.objects.get(type="Purchase"), "value")
            discount_to_apply = (self.points_redeemed * reward_base) / 100
        else:
            discount_to_apply = 0

        self.grand_total = self.order_total + self.delivery_cost - Decimal(discount_to_apply)
        print(f'order_number saved on model instance: {self.order_number}')
        print(f'user_profile saved on model instance: {self.user_profile}')
        print(f'order_total saved on model instance: {self.order_total}')
        print(f'grand_total saved on model instance: {self.grand_total}')
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    bottle_size = models.ForeignKey(
        Size, null=False, blank=False, on_delete=models.CASCADE)
    nicotine = models.ForeignKey(
        Nicotine, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        if self.product.on_sale:
            price = self.bottle_size.sale_price
        else:
            price = self.bottle_size.price

        self.lineitem_total = price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name}-{self.bottle_size.label}-{self.nicotine.strength} on order {self.order.order_number}'
