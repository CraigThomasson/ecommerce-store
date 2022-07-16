from django.shortcuts import render, redirect


def bag_view(request):
    """
    veiw from bag page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity')) 
    redirect_url = request.POST.get('redirect_url')  # gets request.path from hidden file in product details view
    bag = request.session.get('bag', {})  # access the saved session in the browser to get the saved session

    # check if item is already in list and ads quantitsy to current item, and item if not in list
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag  # updates the session bag
    return redirect(redirect_url)
