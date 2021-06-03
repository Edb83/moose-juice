from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import ProductReview


@receiver(post_save, sender=ProductReview)
def update_rating_on_save(sender, instance, created, **kwargs):
    """
    Update a product's average rating on when a review
    is created or updated.
    """
    instance.product.calculate_rating()


@receiver(post_delete, sender=ProductReview)
def update_rating_on_delete(sender, instance, **kwargs):
    """
    Update a product's average rating when a review is deleted.
    """
    if instance.product:
        instance.product.calculate_rating()
