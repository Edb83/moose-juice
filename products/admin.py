from django.contrib import admin
from products.models import (
    Brand,
    ProductProfile,
    Product
)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'brand',
        'profile',
    )


admin.site.register(Brand)
admin.site.register(ProductProfile)
admin.site.register(Product, ProductAdmin)
