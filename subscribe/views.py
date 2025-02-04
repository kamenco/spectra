from django.shortcuts import render, redirect
from .forms import SubscriptionForm


# Create your views here.

def subscribe(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("subscribe_success")  # Redirect to success page
    else:
        form = SubscriptionForm()
    return render(request, "subscribe/subscribe.html", {"form": form})

    # Successfully subscribed


def subscribe_success(request):
    return render(request, "subscribe/success.html")

