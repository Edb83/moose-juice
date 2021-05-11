from django.db import models
from django.contrib.auth.models import User

from django.db.models import Avg


class Size(models.Model):
    label = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    sale_price = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.label


class Nicotine(models.Model):
    TYPE_CHOICES = (
        ('freebase', 'FREEBASE'),
        ('salt', 'SALT'),
        ('hybrid', 'HYBRID'),
    )
    strength = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(
        max_length=8, choices=TYPE_CHOICES, null=True, blank=True
    )

    def __str__(self):
        return self.strength


class Brand(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    available_sizes = models.ManyToManyField(Size)
    available_nics = models.ManyToManyField(Nicotine)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    on_sale = models.BooleanField(default=False)
    description = models.TextField()
    brand = models.ForeignKey(
        'Brand', null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
    average_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def calculate_rating(self):
        self.average_rating = self.reviews.all().aggregate(Avg("rating"))[
            'rating__avg']
        self.save()

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(
        Product, null=True, blank=True, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    body = models.TextField()
    rating = models.DecimalField(max_digits=4, decimal_places=2, default=3)
    created_on = models.DateTimeField(auto_now_add=True)
    verified_purchase = models.BooleanField(default=False)

    def __str__(self):
        return self.title
