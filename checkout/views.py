from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from . forms import Order_form


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'there are no items in your bag.')
        return redirect(reverse('products'))

    order_form = Order_form()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
    }

    return render(request, template, context)