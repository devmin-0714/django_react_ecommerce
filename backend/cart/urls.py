from django.urls import path

from cart.views import CartListCreateAPIView, CartRetrieveAPIView, CartItemDestroyAPIView

urlpatterns = [
    path('carts/', CartListCreateAPIView.as_view(), name='cart_list_create'),
    path('cart/<str:cart_id>/', CartRetrieveAPIView.as_view(), name='cart_retrieve'),
    path('cart/<str:cart_id>/<int:user_id>/', CartRetrieveAPIView.as_view(), name='cart_retrieve'),
    path('cart/<str:cart_id>/<int:item_id>/', CartItemDestroyAPIView.as_view(), name='cart_destroy'),
    path('cart/<str:cart_id>/<int:item_id>/<int:user_id>/', CartItemDestroyAPIView.as_view(), name='cart_destroy'),
]