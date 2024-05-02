from django.urls import path
from Avtosalon.views import get_info, get_product, detail



urlpatterns = [
    path('', get_info, name='get_info'),
    path('products/<int:pk>', get_product, name='get_products'),
    path('products/detail/<int:pk>', detail, name='detail')]