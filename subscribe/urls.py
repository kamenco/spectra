from django.urls import path
from .views import subscribe, subscribe_success  # Import subscribe_success correctly
from .views import view_subscribers

urlpatterns = [
    path("", subscribe, name="subscribe"),
    path("success/", subscribe_success, name="subscribe_success"),
    path('subscribers/', view_subscribers, name='view_subscribers'),
]

