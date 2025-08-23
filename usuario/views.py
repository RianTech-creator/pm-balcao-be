from django.shortcuts import render, redirect

# Create your views here.
def home_view(request):
    return render(request, 'home_usuario.html')

def cadastrar_usuario(request):
    return render(request, 'cadastrar.html')

def login_view(request):
    return render(request, 'login.html')

def listar_usuarios(request):
    return render(request, 'listar_usuarios.html')

def usuario_painel(request):
    return render(request, 'painel.html')


def login_view(request):
    if request.method == 'POST':
        # Aqui normalmente você faz a autenticação...
        # Se o login for bem-sucedido:
        return redirect('painel_usuario')  # Usa o nome da rota cadastrada no urls.py
    return render(request, 'login.html')
