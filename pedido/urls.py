from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pedidos, name='listar_pedidos'),
]