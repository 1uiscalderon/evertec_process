from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Order
from django.template import loader
from .forms import OrderForm
from datetime import datetime, timedelta

URL = 'https://test.placetopay.com/redirection/api/session'

# Setting up data for the request in the URL
data = {
    "payment": {
        "reference": "TEST_01",
        "description": "Pago de Prueba",
        "amount": {
            "currency": "COP",
            "total": "10000"
        }
    },
    "expiration": (datetime.now() + timedelta(days=1)).isoformat(),
    "returnUrl": "http://127.0.0.1:8000/store",
    "ipAddress": "127.0.0.1",
    "userAgent": "Mozilla/5.0 (X11; Linux x86_64)"
                 "AppleWebKit/537.36 (KHTML, like Gecko)"
                 "Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41",
}


@require_http_methods(['GET', 'POST'])
def create_order(request):
    """Method to create a new order using the Order form: form_orders.html"""
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        order_det = Order.objects.all().last()
        context = {
            'order_det': order_det,
        }
        # Renders the output when an order is created
        return render(request, 'app_v1/order_created.html', context)
    # Redern the form
    return render(request, 'app_v1/form_orders.html', {'form': form})


@require_http_methods(['GET'])
def order_detail(request, id):
    """Method to retrieve data of an order"""
    order_det = Order.objects.get(id=id)
    context = {
        'order_det': order_det,
    }
    return render(request, 'app_v1/order_detail.html', context)


@require_http_methods(['GET'])
def list_orders(request):
    """Method to render the list of all orders"""
    orders_list = Order.objects.all()
    context = {
        'orders_list': orders_list,
    }
    return render(request, 'app_v1/list_orders.html', context)


@require_http_methods(['GET', 'POST'])
def order_status(request):
    pass


def search_order(request):
    """Method to use in the search field on the navbar, search for a specific
    Order id"""
    if request.method == "POST":
        searched = request.POST['searched']
        # Check if the input in the search
        try:
            order_id = Order.objects.get(id=searched)
        except Exception:
            order_id = None
        context = {
            'searched': searched,
            'order_id': order_id,
        }
        if order_id is None:
            return render(request, 'app_v1/search_id.html', {})
        return render(request, 'app_v1/search_id.html', context)
    else:
        return render(request, 'app_v1/search_id.html', {})
