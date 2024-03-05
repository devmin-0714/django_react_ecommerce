from django.db import models
from shortuuid.django_fields import ShortUUIDField


class Cart(models.Model):
    class Meta:
        verbose_name = '장바구니'
        verbose_name_plural = '장바구니'

    def __str__(self):
        return f'{self.cart_id} - {self.product.name}'

    cart_id = models.CharField(max_length=1000, null=True, blank=True, verbose_name='장바구니 ID')
    user = models.ForeignKey(
        'account.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='유저 FK'
    )
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품 FK')
    product_option = models.ForeignKey(
        'product.ProductOption',
        on_delete=models.CASCADE,
        verbose_name='상품 옵션 FK'
    )
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name='수량')
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name='가격')
    shipping_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name='배송비')
    total = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name='총 가격')


class CartOrder(models.Model):
    class Meta:
        verbose_name = '장바구니 주문'
        verbose_name_plural = '장바구니 주문'

    class STATUS:
        # payment
        UNPAID = 'UNPAID'
        PAID = 'PAID'
        CANCELLED = 'CANCELLED'
        REFUNDED = 'REFUNDED'

        PAYMENT_CHOICES = [
            (UNPAID, '미결제'),
            (PAID, '결제 완료'),
            (CANCELLED, '취소'),
            (REFUNDED, '환불'),
        ]

        # order
        DELIVERING = 'DELIVERING'
        DELIVERED = 'DELIVERED'

        ORDER_CHOICES = [
            (DELIVERING, '배송중'),
            (DELIVERED, '배송 완료'),
        ]

    oder_id = ShortUUIDField(length=10, max_length=25, alphabet="abcdefghijklmnopqrstuvxyz")
    seller = models.ManyToManyField('seller.Seller', blank=True, verbose_name='판매자 FK')
    buyer = models.ForeignKey(
        'account.User',
        on_delete=models.SET_NULL,
        related_name='buyer',
        null=True,
        blank=True,
        verbose_name='구매자'
    )
    shipping_amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='배송비')
    total = models.DecimalField(default=0.00, max_digits=12, decimal_places=2, verbose_name='총 가격')

    # 상태
    payment_status = models.CharField(max_length=50, choices=STATUS.PAYMENT_CHOICES, verbose_name='결제 상태')
    order_status = models.CharField(max_length=50, choices=STATUS.ORDER_CHOICES, verbose_name='주문 상태')

    # 주소
    address = models.CharField(max_length=1000, null=True, blank=True, verbose_name='주소')

    # 개인정보
    name = models.CharField(max_length=30, verbose_name='구매자명')
    email = models.CharField(max_length=50, verbose_name='구매자 이메일')
    phone = models.CharField(max_length=30, verbose_name='구매자 핸드폰 번호')


class CartOrderItem(models.Model):
    class Meta:
        verbose_name = '장바구니 주문 아이템'
        verbose_name_plural = '장바구니 주문 아이템'

    class STATUS:
        # payment
        ORDER_PLACED = 'ORDER_PLACED'
        DELIVERING = 'DELIVERING'
        DELIVERED = 'DELIVERED'
        RETURNING = 'RETURNING'
        RETURNED = 'RETURNED'

        DELIVERY_STATUS = [
            (ORDER_PLACED, '주문 완료'),
            (DELIVERING, '배송중'),
            (DELIVERED, '배송 완료'),
            (RETURNING, '반품중'),
            (RETURNED, '반품 완료'),
        ]

    order_id = ShortUUIDField(length=10, max_length=25, alphabet="abcdefghijklmnopqrstuvxyz")
    cart_order = models.ForeignKey(
        'CartOrder',
        on_delete=models.CASCADE,
        related_name='order_item',
        verbose_name='장바구니 주문 FK'
    )
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.CASCADE,
        related_name='order_item',
        verbose_name='상품 FK'
    )
    product_option = models.ForeignKey(
        'product.ProductOption',
        on_delete=models.CASCADE,
        verbose_name='상품 옵션 FK'
    )
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name='수량')
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name='가격')
    shipping_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='배송비',
        help_text='예상 배송료 = 배송료 * 총액"'
    )
    total = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name='총액')

    expected_delivery_date_from = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name='예상 배송 시작일')
    expected_delivery_date_to = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name='예상 배송 도착일')
    saved = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        null=True,
        blank=True,
        help_text="구매자에 의해 저장된 금액"
    )

    # 주문 단계
    order_placed = models.BooleanField(default=False, verbose_name='주문 완료')
    product_delivering = models.BooleanField(default=False, verbose_name='배송중')
    product_delivered = models.BooleanField(default=False, verbose_name='배송 완료')
    product_returning = models.BooleanField(default=False, verbose_name='반품중')
    product_returned = models.BooleanField(default=False, verbose_name='반품 완료')

    delivery_status = models.CharField(max_length=100, choices=STATUS.DELIVERY_STATUS)
    tracking_id = models.CharField(max_length=100000, null=True, blank=True)

    seller = models.ForeignKey('seller.Seller', on_delete=models.SET_NULL, null=True, verbose_name='판매자 FK')
