from django.db import models
from core.models import Product
from django.contrib.auth.models import User
# from django.conf import settings

class Payment(models.Model):
    account_number = models.CharField(max_length=16, verbose_name='Номер счета')
    expiration_date = models.DateField()
    microwave_code = models.CharField(max_length=3)

    def __str__(self):
        return f"Payment {self.account_number}"
class Address(models.Model):
    """
        Модель адреса пользователя
    """
    customer = models.ForeignKey(User, verbose_name='Покупатель', on_delete=models.CASCADE)
    city = models.CharField(verbose_name='Город', max_length=32)
    street_name = models.CharField(verbose_name='Название улицы', max_length=64)
    street_type = models.CharField(verbose_name='Тип города', max_length=16)
    zip_code = models.CharField(max_length=100, verbose_name='Индекс',)
    house = models.CharField(verbose_name='Дом', max_length=64)
    contact_phone = models.CharField(verbose_name='Контактный телефон', max_length=32, null=True)
    contact_fio = models.CharField(verbose_name='ФИО', max_length=64, null=True)

    def __str__(self):
        return f'Город {self.city}, улица {self.street_name}, дом {self.house}'

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

class Address(models.Model):
    customer = models.ForeignKey(User, verbose_name='Покупатель', on_delete=models.CASCADE)
    city = models.CharField('Город', max_length=32)
    street_name = models.CharField('Название улицы', max_length=64)
    house = models.CharField('Дом', max_length=64)
    postal_code = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Payment(models.Model):
    card_number = models.CharField(max_length=16, verbose_name="Номер карты")
    date = models.DateField()
    cvc = models.CharField(max_length=3)


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
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="order_address", verbose_name='Адрес')
    phone_number = models.CharField(max_length=250, verbose_name='Номер телефона')
    address = models.ForeignKey(Address, related_name='order_address', on_delete=models.CASCADE, verbose_name='Адрес')
    status = models.CharField(max_length=100, choices=CHOICES, default='New', verbose_name="Статус")
    sum = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order №{self.id} Paid: {self.paid}'


# class OrderProduct(models.Model):
#     pass


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_info', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)

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
