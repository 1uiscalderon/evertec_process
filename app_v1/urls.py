from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('<int:id>/', views.order_detail, name='order_detail'),
    path('', views.list_orders, name='list_orders'),
    path('status/', views.order_status, name='order_status'),
    # Create order
    path('create/', views.create_order, name='create_order'),
    # Search Order by id
    path('search_order/', views.search_order, name='search_order'),
]
