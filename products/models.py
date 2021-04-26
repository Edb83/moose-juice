from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.friendly_name


class ProductProfile(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(
        'Brand', null=True, blank=True, on_delete=models.SET_NULL)
    profile = models.ForeignKey(
        'ProductProfile', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
