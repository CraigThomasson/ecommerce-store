from django import forms
from .models import Order

class order_Form(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name', 'email', 'phone_number',
            'town_or_city', 'postcode', 'country',
            'county,'
        )