from django.contrib import admin
from .models import Order, OrderItem, Payment, Address, User


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(Payment)
