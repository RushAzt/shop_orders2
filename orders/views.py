from rest_framework.viewsets import ModelViewSet
from orders.models import Order, OrderInfo
from orders.serializers import OrderSerializers, OrderInfoSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    lookup_field = 'id'

class OrderInfoViewSet(ModelViewSet):
    queryset = OrderInfo
    serializer_class = OrderInfoSerializer
    lookup_field = 'id'

# class OrderAPIView(APIView):
#     serializer = OrderSerializers
#
#     def post(self, request):
#         order = Order(request)
#         id = request.data['id']
#         product = get_object_or_404(Product, id=id)


