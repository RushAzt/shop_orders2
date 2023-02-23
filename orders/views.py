from django.shortcuts import redirect
from rest_framework import permissions, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from orders.models import Order, OrderItem, Payment, Address, Product
from .serializers import OrderSerializers, OrderItemSerializer, PaymentSerializer, AddressSerializer

class AddressViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    def perform_create(self, serializer):
        order = serializer.save()
        items = self.request.data.get('items')
        for item in items:
            product_id = item['product']
            quantity = item['quantity']
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity
            )
        return redirect('payment')

class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order_id = request.session.get('order_id')
        order = Order.objects.get(id=order_id)
        order.paid = True
        order.save()
        payment = serializer.save()
        payment.order = order
        payment.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



# class PaymentViewSet(ModelViewSet):
#     queryset = Payment.objects.all()
#     serializer_class = PaymentSerializer
#     lookup_field = 'id'
#     permission_classes = [permissions.IsAuthenticated]
#
# class OrderViewSet(ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializers
#     lookup_field = 'id'
#     permission_classes = [permissions.IsAuthenticated]
#
# class OrderItemViewSet(ModelViewSet):
#     queryset = OrderItem.objects.all()
#     serializer_class = OrderItemSerializer
#     lookup_field = 'id'
#     permission_classes = [permissions.IsAuthenticated]
#
# # class OrderAPIView(APIView):
# #     serializer = OrderSerializers
# #
# #     def post(self, request):
# #         order = Order(request)
# #         id = request.data['id']
# #         product = get_object_or_404(Product, id=id)
#
#
