from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import FormularioRegistro, FormularioLogin
from AppFinal.models import Usuario

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

def login(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')



def registroUsuario(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            nacionalidad = form.cleaned_data['nacionalidad']
            contraseña = form.cleaned_data['contraseña']

        Usuario.objects.create(nombre=nombre, apellido=apellido,email=email,telefono=telefono,nacionalidad=nacionalidad, contraseña=contraseña)
        return redirect('loginUsuario')  # Redirige a la pagina para iniciar sesion
    

    else:
        form = FormularioRegistro()
    return render(request, 'registro.html', {'form': form})

def loginUsuario(request):
    if request.method == 'POST':
        form = FormularioLogin(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            contraseña = form.cleaned_data['contraseña']
            usuario = authenticate(request, nombre=nombre, contraseña=contraseña)
            if usuario is not None:
                auth_login(request, Usuario)
                return redirect('index.html')  # Redirige al usuario a la página de inicio
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = FormularioLogin()

    return render(request, 'login.html', {'form': form})

@login_required
def perfilUsuario(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        usuario = Usuario.objects.get(id=usuario_id)
        return render(request, 'perfil_usuario.html', {'usuario': usuario})
    else:
        return redirect('iniciar_sesion')




