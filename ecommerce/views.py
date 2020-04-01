from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .forms import RegisterForm

def index(request):
    return render(request, 'index.html', {
        #Context 
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') #diccionario
        password = request.POST.get('password') #diccionario

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña invalidos')

    return render(request, 'users/login.html', {
        #context
    })

def logout_view(request):
    user = request.user
    logout(request)
    messages.success(request, 'Sessión cerrada exitosamente. ¡Nos vemos pronto {}!'.format(user.username))
    return redirect('login')

def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')

    return render(request, 'users/register.html',{
        'form': form
    })