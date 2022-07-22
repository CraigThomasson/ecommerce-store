from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from . forms import Order_form
from bag.contexts import bag_contents
import stripe

def checkout(request):
    """
    this view deals with the checkout pahe and stripe payment
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'there are no items in your bag.')
        return redirect(reverse('products'))

    # get the current bad from bag.contexts 
    # and create total to be passes to stripe
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )


    order_form = Order_form()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)