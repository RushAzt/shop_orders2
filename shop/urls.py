from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('core.urls')),
    path('api/v1/', include('orders.urls')),
    # path('api/v1/users/', include('users.urls')),
]
