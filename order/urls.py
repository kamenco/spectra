from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_home, name='order_home'),  # Add this line to create a URL named 'order'
]