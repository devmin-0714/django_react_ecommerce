from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

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

    def get_object(self):
        pk = self.kwargs.get('pk')
        return Product.objects.get(id=pk)


class ProductSearchAPIView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        query = self.request.GET.get('query')
        products = Product.objects.filter(name__icontains=query)
        return products
