from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from checkout.models import Order
from subscribe.models import Subscriber  # Fetch subscribed emails
# Create your views here.
# account/views.py

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to profile after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/account-signup.html', {'form': form})

# Profile view

# @login_required
# def profile(request):
   # orders = request.user.orders.all()  # Fetch all orders for the logged-in user
   # return render(request, 'account/profile.html')


@login_required
def profile(request):
    # Fetch all orders for the logged-in user and include related completed work
    orders = Order.objects.filter(user=request.user).select_related('completed_work')
    return render(request, 'registration/profile.html', {'orders': orders})

    # Profile for subscribed users

@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)

    # Fetch subscribed emails if superuser
    subscribed_emails = Subscriber.objects.all() if request.user.is_superuser else None

    return render(request, 'registration/profile.html', {
        'orders': orders,
        'subscribed_emails': subscribed_emails
    })
