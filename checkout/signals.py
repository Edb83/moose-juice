from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def total_signal_revive(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def total_signal_destroy(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
