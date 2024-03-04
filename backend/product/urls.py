from django.urls import path

from product.views import (
    ProductCategoryListAPIView,
    ProductBrandListAPIView,
    ProductListAPIView,
    ProductRetrieveAPIView,
    ProductSearchAPIView,
)

urlpatterns = [
    path('category/', ProductCategoryListAPIView.as_view(), name='category'),
    path('brand/', ProductBrandListAPIView.as_view(), name='brand'),
    path('products/', ProductListAPIView.as_view(), name='products'),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product'),
    path('search/', ProductSearchAPIView.as_view(), name='search'),
]
