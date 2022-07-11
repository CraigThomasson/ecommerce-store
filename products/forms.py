from django import forms
from .models import Product, Category


class Product_form(forms.ModelForm):
    """
    form for managing crud for products
    """
    class Meta:
        model = Product
        fields = '__all__'

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    Categories = Category.objects.all()
    friendly_names = [(c.id, c.get_friendly_name()) for c in Categories]

    self.fields['category'].choices = friendly_names
