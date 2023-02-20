from django.db import models
from core.models import Product
from django.contrib.auth.models import User

CHOICES = (
    ('В обработке', 'В обработке'),
    ('Выполнен', 'Выполнен'),
    ('Отменен', 'Отменен'),
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамиля')
    phone_number = models.CharField(max_length=250, verbose_name='Номер телефона')
    city = models.CharField(max_length=255, verbose_name='Город')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    sum = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=CHOICES, default='New', verbose_name="Статус")
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order {self.id}'


class OrderProduct(models.Model):
    pass


class OrderInfo(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_info', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Инфо о заказе'
        verbose_name_plural = 'Информация о заказе'


    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity

    def add_quantity(self, amount):
        self.quantity += amount
        self.save()
