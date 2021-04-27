from django.contrib import admin
from products.models import (
    Brand,
    Category,
    Tag,
    Product,
)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'brand',
        'category',
    )
    filter_horizontal = ('tags', 'tags')


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product, ProductAdmin)
