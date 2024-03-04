from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from product.models import (
    ProductCategory,
    ProductBrand,
    Product,
    ProductImage,
    ProductOption,
)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', ]


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', ]


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductOptionAdmin(admin.TabularInline):
    model = ProductOption
    extra = 1


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'category',
            'brand',
        ]


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin, ProductOptionAdmin]
    list_display = [
        'name',
        'product_image_display',
        'price',
        'category',
        'brand',
    ]
    list_per_page = 10
    form = ProductAdminForm

    def product_image_display(self, obj):
        if obj.images.exists():
            first_image = obj.images.first()
            return mark_safe(f'<img src="{first_image.image.url}" style="width: 100px; height:100px;" />')
        else:
            return '이미지 없음'

    product_image_display.short_description = '상품 이미지'


admin.site.register(ProductCategory, CategoryAdmin)
admin.site.register(ProductBrand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
