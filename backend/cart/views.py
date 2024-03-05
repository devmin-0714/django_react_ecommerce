from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from cart.models import Cart
from cart.serializers import CartSerializer


class CartListCreateAPIView(ListCreateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        payload = request.data

        cart_id = payload['cart_id']
        user_id = payload.get('user')
        product_id = payload['product']
        product_option = payload['product_option']
        quantity = payload['quantity']
        price = payload['price']
        shipping_amount = payload['shipping_amount']

        product = get_object_or_404('product.Product', id=product_id)
        user = get_object_or_404('account.User', id=user_id) if user_id else None

        cart = Cart.objects.filter(cart_id=cart_id, product=product).first()

        if cart:
            message = '장바구니가 업데이트 되었습니다'
        else:
            message = '장바구니가 추가 되었습니다'
            cart = Cart()

        cart.cart_id = cart_id
        cart.user = user
        cart.product = product
        cart.product_option = product_option
        cart.quantity = quantity
        cart.price = price
        cart.shipping_amount = Decimal(shipping_amount) * int(quantity)
        cart.total = Decimal(price) * int(quantity) + cart.shipping_amount

        cart.save()

        return Response(
            {'message': message},
            status=status.HTTP_200_OK if cart else status.HTTP_201_CREATED
        )


class CartListAPIView(ListAPIView):
    serializer_class = CartSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        cart_id = self.kwargs['cart_id']
        user_id = self.kwargs['user_id']

        if user_id:
            user = get_object_or_404('account.User', id=user_id)
            queryset = Cart.objects.filter(Q(user=user, cart_id=cart_id) | Q(user=user))
        else:
            queryset = Cart.objects.filter(cart_id=cart_id)

        return queryset


class CartRetrieveAPIView(RetrieveAPIView):
    serializer_class = CartSerializer
    lookup_field = 'cart_id'
    permission_classes = (AllowAny,)

    def get_queryset(self):
        cart_id = self.kwargs['cart_id']
        user_id = self.kwargs.get('user_id')

        if user_id:
            user = get_object_or_404('account.User', id=user_id)
            queryset = Cart.objects.filter(cart_id=cart_id, user=user)
        else:
            queryset = Cart.objects.filter(cart_id=cart_id)

        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        total_shipping = 0.0
        total_total = 0.0

        for cart_item in queryset:
            total_shipping += float(self.calculate_shipping(cart_item))
            total_total += round(float(self.calculate_total(cart_item)), 2)

        # Create a data dictionary to store the cumulative values
        data = {
            'shipping': round(total_shipping, 2),
            'total': total_total,
        }

        # Return the data in the response
        return Response(data)

    def calculate_shipping(self, cart_item):
        return cart_item.shipping_amount

    def calculate_total(self, cart_item):
        return cart_item.total


class CartItemDestroyAPIView(DestroyAPIView):
    serializer_class = CartSerializer
    lookup_field = 'cart_id'

    def get_object(self):
        cart_id = self.kwargs['cart_id']
        item_id = self.kwargs['item_id']
        user_id = self.kwargs.get('user_id')

        if user_id:
            user = get_object_or_404(get_user_model(), id=user_id)
            cart = get_object_or_404(Cart, cart_id=cart_id, id=item_id, user=user)
        else:
            cart = get_object_or_404(Cart, cart_id=cart_id, id=item_id)

        return cart
