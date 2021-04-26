from django.contrib import admin
from products.models import (
    Brand,
    Category,
    Product,
)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'brand',
        'category',
    )


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
