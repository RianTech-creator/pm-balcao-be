from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_pedidos, name='criar_pedidos'),
    path('listar/', views.listar_pedidos, name='listar_pedidos'),
    path('historico/', views.historico_pedidos, name='historico_pedidos'),
]