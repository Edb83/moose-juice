from products.models import Brand, Category


def product_groups(request):
    """
    Provides global access to brands and categories (flavours)
    """

    brands = Brand.objects.all()
    categories = Category.objects.all()

    context = {
        'brands': brands,
        'categories': categories,
    }

    return context
