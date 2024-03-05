from rest_framework import serializers

from product.models import (
    ProductCategory,
    ProductBrand,
    Product,
    ProductImage,
    ProductOption
)


class ProductCategorySerializer(serializers.ModelSerializer):
    sub_categories = serializers.SerializerMethodField()

    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'parent', 'sub_categories', ]

    def get_sub_categories(self, obj):
        children = obj.children.all()
        return [{'id': child.id, 'name': child.name} for child in children]


class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = ['id', 'name', ]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image', ]


class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = [
            'id',
            'product',
            'size',
            'color',
            'stock_quantity',
            'in_stock'
        ]


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    options = ProductOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'category',
            'brand',
            # extra info
            'images',
            'options'
        ]
