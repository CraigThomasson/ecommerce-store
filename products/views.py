from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import Product_form


def all_products(request):
    """
    This view displays all products and
    handles sorting and searching quries
    """

    products = Product.objects.all()
    query = None

    if request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, 'You submitted a blank search')
            return redirect(reverse('products'))

        queries = Q(
            name__icontains=query
        ) | Q(
            description__icontains=query
        ) | Q(
            scent__icontains=query
        ) | Q(
            colour__icontains=query
        )
        products = products.filter(queries)

    context = {
        'products': products,
        'search_results': query,
    }

    return render(request, 'products/products.html', context)


def view_product(request, product_id):
    """
    This view displays  product detials for selected product
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/view_product.html', context)


@login_required
def add_product(request):
    """
    view to add products to the db
    """
    # checks if user has permition to add products
    if not request.user.groups.filter(
        name="site_admin"
    ).exists() or request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        print(request.user.groups)
        print('access denined')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = Product_form(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product Added')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'The producted was not added. Please check the form is valid.')
    else:
        form = Product_form()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


