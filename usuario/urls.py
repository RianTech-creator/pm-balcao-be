from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('login/', views.login_view, name='login_usuario'),
    path('listar/', views.listar_usuarios, name='listar_usuarios'),
    path('painel/', views.usuario_painel, name='painel_usuario'),
]