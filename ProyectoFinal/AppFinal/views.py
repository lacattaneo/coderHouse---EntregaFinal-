from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import FormularioRegistro, FormularioLogin, SeleccionarEventoForm
from AppFinal.models import Usuario, CompraEntrada

def index(request):
    return render(request, 'index.html')


def chamame(request):
    return render(request, 'chamame.html')


def ibera(request):
    return render(request, 'ibera.html')

def pesca (request):
    return render(request, 'pesca.html')

def padre(request):
    return render(request,'padre.html')

def carnaval(request):
    return render(request,'carnaval.html')

def yo(request):
    return render(request, 'yo.html')

def loginPagina(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')



def registroUsuario(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['contraseña'])
            user.save()
            user = authenticate(username=user.email, password=form.cleaned_data['contraseña'])
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = FormularioRegistro()
    return render(request, 'registro.html', {'form': form})

def loginUsuario(request):
    if request.method == 'POST':
        form = FormularioLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['contraseña']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Email o contraseña incorrectos.')
    else:
        form = FormularioLogin()
    return render(request, 'login.html', {'form': form})


@login_required
def perfilUsuario(request):
    return render(request, 'perfil_usuario.html', {'usuario': request.user})


def userLogout(request):
    logout(request)
    return redirect('index')


@login_required
def comprarEntrada(request):
    if request.method == 'POST':
        form = SeleccionarEventoForm(request.POST)
        if form.is_valid():
            # Procesar la compra de la entrada aquí
            return redirect('confirmacionCompra')  # Redirige a la página de confirmación
    else:
        form = SeleccionarEventoForm()

    return render(request, 'comprarEntrada.html', {'form': form})



def confirmacionCompra(request):
    return render(request, 'confirmacionCompra.html')





