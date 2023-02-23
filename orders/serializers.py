from rest_framework import serializers
from orders.models import Order, OrderItem, Payment, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "customer city street_name house contact_phone postal_code".split()

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "id card_number date cvc".split()

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "id first_name last_name phone_number status sum address".split()


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializers()
    cost = serializers.SerializerMethodField()
    class Meta:
        model = OrderItem
        fields = "id order product quantity get_cost".split()

