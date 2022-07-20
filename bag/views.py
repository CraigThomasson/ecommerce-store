from django.shortcuts import render, redirect, reverse, HttpResponse
from products.models import Product
from django.contrib import messages


def bag_view(request):
    """
    veiw from bag page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')  # gets request.path from hidden file in product details view
    bag = request.session.get('bag', {})  # access the saved session in the browser to get the saved session

    # check if item is already in list and ads quantitsy to current item, and item if not in list
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'{product.name} was added to bag')
    else:
        bag[item_id] = quantity
        messages.success(request, f'{product.name} was added to bag')

    request.session['bag'] = bag  # updates the session bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """ update the quantity of the specified product to the shopping bag in the view bag page """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})  # access the saved session in the browser to get the saved session

    # check if item is already in list and ads quantitsy to current item, and item if not in list

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag  # updates the session bag
    return redirect(reverse('bag_view'))


def remove_bag_Item(request, item_id):
    """ remove item from the bag"""

    try:
        bag = request.session.get('bag', {})  # access the saved session in the browser to get the saved session

        bag.pop(item_id)

        request.session['bag'] = bag  # updates the session bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
