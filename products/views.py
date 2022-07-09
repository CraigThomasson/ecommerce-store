from django.shortcuts import render
from .models import Product

def all_products(request):
    """
    This view displays all products and
    handles sorting and searching quries
    """
    
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)