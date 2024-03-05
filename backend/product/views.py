from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from product.models import ProductCategory, ProductBrand, Product
from product.serializers import (
    ProductCategorySerializer,
    ProductBrandSerializer,
    ProductSerializer,
)


class ProductCategoryListAPIView(ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
    permission_classes = (AllowAny,)


class ProductBrandListAPIView(ListAPIView):
    serializer_class = ProductBrandSerializer
    queryset = ProductBrand.objects.all()
    permission_classes = (AllowAny,)


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (AllowAny,)


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=pk)


class ProductSearchAPIView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('query', openapi.IN_QUERY, description="검색어", type=openapi.TYPE_STRING),
    ])
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', '')
        queryset = self.get_queryset(query)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self, query):
        products = Product.objects.filter(name__icontains=query)
        return products
