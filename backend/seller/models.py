from django.db import models


class Seller(models.Model):
    class Meta:
        verbose_name = '판매자'
        verbose_name_plural = '판매자'

    def __str__(self):
        return self.name

    user = models.OneToOneField(
        'account.User',
        on_delete=models.PROTECT,
        null=True,
        related_name='seller',
        verbose_name='유저 FK'
    )
    name = models.CharField(max_length=50, help_text='스토어명', verbose_name='스토어명')
    email = models.EmailField(
        max_length=50,
        help_text='스토어 이메일',
        null=True,
        blank=True,
        verbose_name='스토어 이메일'
    )
