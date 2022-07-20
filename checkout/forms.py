from django import forms
from .models import Order

class Order_form(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name', 'email', 'phone_number',
            'town_or_city', 'postcode', 'country',
            'county',
        )