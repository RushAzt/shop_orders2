from django.contrib import admin
<<<<<<< HEAD
from .models import Order, OrderItem, OrderProduct, User
=======
from .models import Order, OrderItem, Payment, Address, User
>>>>>>> origin/master


admin.site.register(Order)
admin.site.register(OrderItem)
<<<<<<< HEAD
admin.site.register(OrderProduct)
=======
admin.site.register(Address)
admin.site.register(Payment)
>>>>>>> origin/master
