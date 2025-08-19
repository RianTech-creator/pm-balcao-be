from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def listar_usuarios(request):
    return render(request, 'listar_usuarios.html')

