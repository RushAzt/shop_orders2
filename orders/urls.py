from django.urls import path
from . import views

get_post = {'get': 'list',
            'post': 'create'}
get_put_delete = {'get': 'retrieve',
                  'put': 'update',
                  'delete': 'destroy'}

urlpatterns = [
    path('create_order/', views.OrderViewSet.as_view(get_post)),
    path('create_order/<int:id>/', views.OrderViewSet.as_view(get_put_delete)),
    path('order_info/', views.OrderInfoViewSet.as_view(get_post)),
    path('order_info/<int:id>/', views.OrderInfoViewSet.as_view(get_put_delete)),
]