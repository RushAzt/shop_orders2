from rest_framework import serializers
from orders.models import Order


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "id first_name last_name phone_number city status sum address".split()


class OrderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "id order product quantity price".split()