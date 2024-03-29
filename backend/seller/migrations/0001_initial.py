# Generated by Django 4.2.7 on 2024-03-05 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='스토어명', max_length=50, verbose_name='스토어명')),
                ('email', models.EmailField(blank=True, help_text='스토어 이메일', max_length=50, null=True, verbose_name='스토어 이메일')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='seller', to=settings.AUTH_USER_MODEL, verbose_name='유저 FK')),
            ],
            options={
                'verbose_name': '판매자',
                'verbose_name_plural': '판매자',
            },
        ),
    ]
