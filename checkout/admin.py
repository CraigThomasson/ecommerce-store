from django.contrib import admin
from .models import Order, OrderLineItem

# code taken from boutique ado project.


class OrderLineItemAdminInline(admin.TabularInline):
    """
    sets up admin for prderline item
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


# code taken from boutique ado project.

class OrderAdmin(admin.ModelAdmin):
    """
    sets up admin for order modle
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
