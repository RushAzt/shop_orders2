from django.contrib import admin
from .models import Order, OrderItem, OrderProduct, User


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderProduct)
