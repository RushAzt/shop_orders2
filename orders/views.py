from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from orders.models import Order, OrderItem, Payment
from .serializers import OrderSerializers, OrderItemSerializer, PaymentSerializer



class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)

        # return Response(data={"order_create": serializer.data, "redirect": "http://127.0.0.1:8000/api/v1/create_order/payment/"})
        return Response(serializer.data, status=status.HTTP_201_CREATED)



    # def perform_create(self, serializer):
    #     order = serializer.save()
        # items = self.request.data.get('items')
        # for item in items:
        #     product_id = item['product']
        #     quantity = item['quantity']
        #     product = Product.objects.get(id=product_id)
        #     OrderItem.objects.create(
        #         order=order,
        #         product=product,
        #         quantity=quantity
        #     )
        #     order.save()

        # return Response(data={"redirect_to": "http://127.0.0.1:8000/api/v1/create_order/payment/"})

class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]



class PaymentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = "id"

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     order_id = request.session.get('order_id')
    #     order = Order.objects.get(id=order_id)
    #     order.paid = True
    #     order.save()
    #     payment = serializer.save()
    #     payment.order = order
    #     payment.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)




