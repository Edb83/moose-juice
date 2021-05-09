from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import ProductReview


@receiver(post_save, sender=ProductReview)
def update_rating_on_save(sender, instance, created, **kwargs):
    """
    Update rating on product review update/create
    """
    instance.product.calculate_rating()


@receiver(post_delete, sender=ProductReview)
def update_rating_on_delete(sender, instance, **kwargs):
    """
    Update rating on product review delete
    """
    instance.product.calculate_rating()
