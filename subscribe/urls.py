from django.urls import path
from .views import subscribe, subscribe_success  # Import subscribe_success correctly

urlpatterns = [
    path("", subscribe, name="subscribe"),
    path("success/", subscribe_success, name="subscribe_success"),
]
