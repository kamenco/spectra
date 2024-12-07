from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_page, name='product'),  # Map the home page
]