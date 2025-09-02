from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def listar_pedidos(request):
    return render(request, 'listar_pedidos.html')

def criar_pedidos(request):
    return render(request, 'criar_pedidos.html')

def historico_pedidos(request):
    return render(request, 'historico_pedidos.html')