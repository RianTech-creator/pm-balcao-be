from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def home_view(request):
    return render(request, 'home_usuario.html')

def cadastrar_usuario(request):
    return render(request, 'cadastrar_usuario.html')

def login_view(request):
    return render(request, 'login_usuario.html')

def listar_usuarios(request):
    return render(request, 'listar_usuarios.html')

def usuario_painel(request):
    return render(request, 'painel_usuario.html')

def logout_usuario(request):
    logout()
    return redirect('login_usuario')

def login_view(request):
    if request.method == 'POST':
        return redirect('painel_usuario')
    return render(request, 'login_usuario.html')