from django.db import models
from django.contrib.auth.models import User
from products.models import Product

from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    User profile model for maintaining default delivery info,
    order history and favourites
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Default delivery details
    default_full_name = models.CharField(
        max_length=80, null=True, blank=True)
    default_email = models.EmailField(
        max_length=80, null=True, blank=True)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_county = models.CharField(
        max_length=80, null=True, blank=True)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)

    # Favourite products
    favourites = models.ManyToManyField(Product)

    # Reward points
    points = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Otherwise just save/update profile
    instance.userprofile.save()
