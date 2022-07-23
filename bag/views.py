from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product


def bag_view(request):
    """
    veiw from bag page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    # gets request.path from hidden file in product details view
    redirect_url = request.POST.get('redirect_url')
    # access the saved session in the browser to get the saved session
    bag = request.session.get('bag', {})

    # check if item is already in list and ads quantitsy to current item,
    # and item if not in list
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'updated {product.name} quantity in bag')
    else:
        bag[item_id] = quantity
        messages.success(request, f'{product.name} was added to bag')

    request.session['bag'] = bag  # updates the session bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """
    update the quantity of the specified
    product to the shopping bag in the view bag page
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    # access the saved session in the browser to get the saved session
    bag = request.session.get('bag', {})

    # check if item is already in list and ads quantitsy to current item,
    #  and item if not in list
    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'updated {product.name} quantity in bag')
    else:
        bag.pop(item_id)
        messages.success(request, f'removed {product.name} from bag')

    request.session['bag'] = bag  # updates the session bag
    return redirect(reverse('bag_view'))


def remove_bag_Item(request, item_id):
    """ remove item from the bag"""

    product = get_object_or_404(Product, pk=item_id)

    try:
        # access the saved session in the browser to get the saved session
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'removed {product.name} from bag')

        request.session['bag'] = bag  # updates the session bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
