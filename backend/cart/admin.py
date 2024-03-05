from django.contrib import admin

from cart.models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = [
        'cart_id',
        'user',
        'product',
        'product_option',
        'quantity',
        'price',
        'shipping_amount',
        'total',
    ]


admin.site.register(Cart, CartAdmin)
