from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Chamado
from .forms import ChamadoForm
from django.contrib import messages

# --- Views Públicas ---
def index(request): return render(request, 'core/index.html')
def sobre(request): return render(request, 'core/sobre.html')
def servicos(request): return render(request, 'core/servicos.html')
def contato(request): return render(request, 'core/contato.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') # Redirecione para a sua página inicial
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.') # <--- ESTA É A MENSAGEM
    return render(request, 'login.html')

# --- View de Logout ---
def logout_view(request):
    logout(request)
    return redirect('index')

# --- Views da Área do Cliente ---
@login_required
def area_cliente(request): return render(request, 'core/area_cliente.html')

@login_required
def info_conta(request):
    contagem_chamados = Chamado.objects.filter(cliente=request.user).count()
    context = {'contagem_chamados': contagem_chamados}
    return render(request, 'core/info_conta.html', context)

@login_required
def lista_chamados(request):
    chamados = Chamado.objects.filter(cliente=request.user).order_by('-data_criacao')
    context = {'chamados': chamados}
    return render(request, 'core/lista_chamados.html', context)

@login_required
def criar_chamado(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            chamado = form.save(commit=False)
            chamado.cliente = request.user
            chamado.save()
            return redirect('lista_chamados')
    else:
        form = ChamadoForm()
    return render(request, 'core/criar_chamado.html', {'form': form})