from rest_framework import serializers

from cart.models import Cart, CartOrderItem
from product.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Cart
        fields = [
            'cart_id',
            'user',
            'product',
            'product_option',
            'quantity',
            'price',
            'shipping_amount',
            'total',
        ]


class CartOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartOrderItem
        fields = [
            'order_id',
            'cart_order',
            'product',
            'product_option',
            'quantity',
            'price',
            'shipping_amount',
            'total',
            'expected_delivery_date_from',
            'expected_delivery_date_to',
            'saved',
            'order_placed',
            'product_delivering',
            'product_delivered',
            'product_returning',
            'product_returned',
            'delivery_status',
            'tracking_id',
            'seller',
        ]


class CartOrderSerializer(serializers.ModelSerializer):
    order_item = CartOrderItemSerializer(many=True, read_only=True)
