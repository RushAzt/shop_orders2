from django.urls import path
from . import views

get_post = {'get': 'list',
            'post': 'create'}
get_put_delete = {'get': 'retrieve',
                  'put': 'update',
                  'delete': 'destroy'}

urlpatterns = [
    path('create_order/payment/', views.PaymentViewSet.as_view(get_post)),
    path('create_order/payment/<int:id>/', views.PaymentViewSet.as_view(get_put_delete)),
    path('create_order/', views.OrderViewSet.as_view(get_post)),
    path('create_order/<int:id>/', views.OrderViewSet.as_view(get_put_delete)),
    path('order_item/', views.OrderViewSet.as_view(get_post)),
    path('order_item/<int:id>/', views.OrderViewSet.as_view(get_put_delete)),
]