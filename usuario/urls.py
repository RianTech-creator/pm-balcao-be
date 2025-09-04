from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('cadastro/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('listar/', views.listar_usuarios, name='listar_usuarios'),
    path('painel/', views.painel_usuario, name='painel_usuario'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
]