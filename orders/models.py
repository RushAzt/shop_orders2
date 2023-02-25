from django.contrib.auth import get_user_model
from django.db import models
from core.models import Product
# from django.contrib.auth.models import User
# from django.conf import settings

User = get_user_model()

class Payment(models.Model):
    card_number = models.CharField(max_length=16, verbose_name='Номер счета')
    date = models.DateField(verbose_name='Срок годности')
    cvc_code = models.CharField(verbose_name='cvc код', max_length=3)
    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"


    def __str__(self):
        return f"Payment {self.card_number}"




CHOICES = (
    ('В обработке', 'В обработке'),
    ('Выполнен', 'Выполнен'),
    ('Отменен', 'Отменен'),
)
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    email = models.EmailField(verbose_name='Email')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамиля')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    city = models.CharField(verbose_name='Город', max_length=32)
    street_name = models.CharField(verbose_name='Название улицы', max_length=64)
    street_type = models.CharField(verbose_name='Тип города', max_length=16)
    zip_code = models.CharField(max_length=100, verbose_name='Индекс', )
    house = models.CharField(verbose_name='Дом', max_length=64)
    status = models.CharField(max_length=100, choices=CHOICES, default='New', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order №{self.id} Paid: {self.paid}'




class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_info', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)

    class Meta:
        verbose_name = 'Инфо о заказе'
        verbose_name_plural = 'Информация о заказе'


    def __str__(self):
        return f'{self.id} {self.order}'

    def get_cost(self):
        return round(self.quantity * self.product.price, 2)

    def add_quantity(self, amount):
        self.quantity += amount
        self.save()
