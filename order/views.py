from django.shortcuts import render, redirect


# Create your views here.
# Home view for orders (e.g., to show the order form)
def order_home(request):
    return render(request, 'order/order.html')
