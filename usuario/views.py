from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Usuario
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # REMOVER DA PRODUÇÃO - USAR EM DEBUG APENAS


# Create your views here.
def home_view(request):
    """
    Renderiza a página inicial. Se o usuário já estiver logado,
    redireciona para o painel.
    """
    if request.user.is_authenticated:
        return redirect('painel_usuario')
    return render(request, 'home_usuario.html')

def cadastrar_usuario(request):
    """
    Cria um novo usuário e o perfil associado.
    O username do usuário será o seu e-mail.
    """
    if request.method == 'POST':
        nome_completo = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if not nome_completo or not email or not senha:
            return render(request, 'cadastrar_usuario.html', {'error': 'Todos os campos são obrigatórios.'})

        if User.objects.filter(username=email).exists():
            return render(request, 'cadastrar_usuario.html', {'error': 'Este e-mail já está em uso.'})

        partes_nome = nome_completo.split(' ', 1)
        first_name = partes_nome[0]
        last_name = partes_nome[1] if len(partes_nome) > 1 else ''

        user = User.objects.create_user(username=email, email=email, password=senha, first_name=first_name, last_name=last_name)
        Usuario.objects.create(user=user)

        return redirect('login_usuario')

    return render(request, 'cadastrar_usuario.html')

@csrf_exempt  # REMOVER DA PRODUÇÃO - USAR EM DEBUG APENAS
def login_usuario(request):
    """
    Autentica o usuário e inicia a sessão.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Usamos o email como username para autenticar
        user = authenticate(request, username=email, password=senha)

        if user is not None:
            login(request, user)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': True, 'message': 'Login realizado com sucesso!'})
            return redirect('painel_usuario')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'message': 'E-mail ou senha inválidos.'})
            return render(request, 'login_usuario.html', {'error': 'E-mail ou senha inválidos.'})

    return render(request, 'login_usuario.html')

def listar_usuarios(request):
    return render(request, 'listar_usuarios.html')

@login_required(login_url='login_usuario')
def painel_usuario(request):
    """
    Exibe o painel do usuário. Acessível apenas para usuários logados.
    """
    return render(request, 'painel_usuario.html')

def logout_usuario(request):
    """
    Encerra a sessão do usuário.
    """
    logout(request)
    return redirect('home_view')