from django.db import models

from account.models import user_directory_path


class ProductCategory(models.Model):
    class Meta:
        verbose_name = '카테고리'
        verbose_name_plural = '카테고리'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, verbose_name='카테고리명')
    parent = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='children',
        null=True,
        blank=True,
        verbose_name='부모 카테고리 FK'
    )


class ProductBrand(models.Model):
    class Meta:
        verbose_name = '브랜드'
        verbose_name_plural = '브랜드'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, verbose_name='브랜드명')


class Product(models.Model):
    class Meta:
        verbose_name = '상품'
        verbose_name_plural = '상품'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, verbose_name='상품명')
    description = models.TextField(null=True, blank=True, verbose_name='상품 상세 설명')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='가격')

    category = models.ForeignKey(
        'ProductCategory',
        on_delete=models.PROTECT,
        related_name='categories',
        null=True,
        blank=True,
        verbose_name='카테고리 FK'
    )
    brand = models.OneToOneField(
        'ProductBrand',
        on_delete=models.PROTECT,
        related_name='brands',
        null=True,
        blank=True,
        verbose_name='브랜드 FK'
    )


class ProductImage(models.Model):
    class Meta:
        verbose_name = '상품 이미지'
        verbose_name_plural = '상품 이미지'

    def __str__(self):
        return '상품 이미지'

    product = models.ForeignKey(
        'Product',
        related_name="images",
        on_delete=models.PROTECT,
        verbose_name='상품 이미지 FK'
    )
    image = models.FileField(upload_to=user_directory_path, default="product_image.jpg")


class ProductOption(models.Model):
    class Meta:
        verbose_name = '상품 옵션'
        verbose_name_plural = '상품 옵션'

    def __str__(self):
        return f'{self.size}/{self.color}/{self.stock_quantity}/'

    product = models.ForeignKey(
        'Product',
        related_name="options",
        on_delete=models.PROTECT,
        verbose_name='상품 FK'
    )
    size = models.CharField(max_length=30, verbose_name='사이즈')
    color = models.CharField(max_length=30, verbose_name='색상')
    stock_quantity = models.PositiveIntegerField(default=0, verbose_name='재고 수량')
    in_stock = models.BooleanField(default=True, verbose_name='재고 여부')
