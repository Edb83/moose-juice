from django.contrib import admin
from products.models import (
    Brand,
    Size,
    Nicotine,
    Category,
    Tag,
    Product,
    ProductReview
)


class BrandAdmin(admin.ModelAdmin):
    filter_horizontal = (
        'available_sizes', 'available_sizes',
        'available_nics', 'available_nics'
        )


class SizeAdmin(admin.ModelAdmin):
    list_display = (
        'label',
        'price',
        'sale_price',
    )


class NicotineAdmin(admin.ModelAdmin):
    list_display = (
        'strength',
        'type',
    )


class CategoryAdmin(admin.ModelAdmin):
    ordering = ('name',)


class TagAdmin(admin.ModelAdmin):
    ordering = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'brand',
        'category',
        'average_rating',
        'on_sale',
    )
    ordering = ('brand', 'name',)
    filter_horizontal = ('tags', 'tags')
    readonly_fields = ('average_rating',)


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'created_on',
        'rating',
    )
    ordering = ('created_on',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Nicotine, NicotineAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
