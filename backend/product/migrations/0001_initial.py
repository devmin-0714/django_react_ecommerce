# Generated by Django 4.2.7 on 2024-03-04 14:18

import account.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='상품명')),
                ('description', models.TextField(blank=True, null=True, verbose_name='상품 상세 설명')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='가격')),
            ],
            options={
                'verbose_name': '상품',
                'verbose_name_plural': '상품',
            },
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='브랜드명')),
            ],
            options={
                'verbose_name': '브랜드',
                'verbose_name_plural': '브랜드',
            },
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=30, verbose_name='사이즈')),
                ('color', models.CharField(max_length=30, verbose_name='색상')),
                ('stock_quantity', models.PositiveIntegerField(default=0, verbose_name='재고 수량')),
                ('in_stock', models.BooleanField(default=True, verbose_name='재고 여부')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='options', to='product.product', verbose_name='상품 FK')),
            ],
            options={
                'verbose_name': '상품 옵션',
                'verbose_name_plural': '상품 옵션',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default='product_image.jpg', upload_to=account.models.user_directory_path)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='images', to='product.product', verbose_name='상품 이미지 FK')),
            ],
            options={
                'verbose_name': '상품 이미지',
                'verbose_name_plural': '상품 이미지',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='카테고리명')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='product.productcategory', verbose_name='상위 카테고리명')),
            ],
            options={
                'verbose_name': '카테고리',
                'verbose_name_plural': '카테고리',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='brands', to='product.productbrand', verbose_name='브랜드 FK'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='product.productcategory', verbose_name='카테고리 FK'),
        ),
    ]