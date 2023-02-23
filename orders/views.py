from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Payment, Order
from .serializers import PaymentSerializer, OrderSerializer

class PaymentListCreateView(generics.ListCreateAPIView):
    """
    API view to list all payments or create a new payment.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class OrderListCreateView(generics.ListCreateAPIView):
    """
    API view to list all orders or create a new order.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific order.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


# from rest_framework.viewsets import ModelViewSet
# from orders.models import Order, OrderItem
# from orders.serializers import OrderSerializers, OrderItemSerializer
#

# class OrderViewSet(ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializers
#     lookup_field = 'id'
#
# class OrderInfoViewSet(ModelViewSet):
#     queryset = OrderItem
#     serializer_class = OrderItemSerializer
#     lookup_field = 'id'

# class OrderAPIView(APIView):
#     serializer = OrderSerializers
#
#     def post(self, request):
#         order = Order(request)
#         id = request.data['id']
#         product = get_object_or_404(Product, id=id)


