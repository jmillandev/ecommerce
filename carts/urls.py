from django.urls import path

from . import views

app_name = 'carts'

urlpatterns = [
    path('add', views.add, name='add'),
    path('eliminar', views.remove, name='remove'),
    path('', views.cart, name='cart'),
]