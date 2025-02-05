from django.shortcuts import render, redirect
from .forms import SubscriptionForm
from django.contrib.admin.views.decorators import staff_member_required
from .models import Subscriber

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

# Added the subscribers


@staff_member_required
def view_subscribers(request):
    subscribers = Subscriber.objects.all()
    return render(request, 'subscribe/view_subscribers.html', {'subscribers': subscribers})


