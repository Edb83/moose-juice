from django.db import models
from datetime import datetime


class Brand(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    brand = models.ForeignKey(
        'Brand', null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
    average_rating = models.PositiveSmallIntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
