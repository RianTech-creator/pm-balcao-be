from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def listar_pedidos(request):
    return render(request, 'listar_pedidos.html')