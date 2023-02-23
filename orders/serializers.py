from rest_framework import serializers
from orders.models import Order, OrderItem, Payment, Address


class AddressSerializer(serializers.ModelSerializer):
    """
    Serializer for the Address model.
    """
    class Meta:
        model = Address
        fields = ['id', 'customer', 'city', 'street_name', 'street_type', 'zip_code', 'house', 'contact_phone', 'contact_fio']



class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "account_number expiration_date microwave_code".split()

class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the OrderItem model.
    """
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price', 'get_cost']



class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.
    """
    address = AddressSerializer(read_only=True)
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'first_name', 'last_name', 'phone_number', 'address',
                  'status', 'sum', 'created_at', 'updated_at', 'paid', 'order_items']


