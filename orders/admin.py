from django.contrib import admin
from .models import Order, OrderInfo, OrderProduct, User


admin.site.register(Order)
admin.site.register(OrderInfo)
admin.site.register(OrderProduct)
