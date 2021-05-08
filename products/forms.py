from django import forms
from .models import Product, Category, Brand


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('on_sale', 'average_rating')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        brands = Brand.objects.all()
        category_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        brand_friendly_names = [(b.id, b.get_friendly_name()) for b in brands]

        self.fields['category'].choices = category_friendly_names
        self.fields['brand'].choices = brand_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'