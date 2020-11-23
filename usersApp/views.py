from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import AuthenticationForm #form de auth
from django.contrib.auth import authenticate#para autenticar users & pass
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm #para crear usuarios nuevos
from datetime import datetime
from .forms import SignUpForm


from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'usersApp/register.html'
    success_url = reverse_lazy('login')
    


def home(request):
    now = datetime.now()

    if request.user.is_authenticated:
        return render(request, "usersApp/home.html",{'now':now})
    return redirect('/login')




def login(request):
    
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario    
    return render(request, "usersApp/login.html",{'form': form})
    

# def register(request):
#     # Creamos el formulario de autenticación vacío
#     form = SignUpForm()
#     if request.method == "POST":
#         # Añadimos los datos recibidos al formulario
#         form = SignUpForm(data=request.POST)
#         # Si el formulario es válido...
#         if form.is_valid():

#             # Creamos la nueva cuenta de usuario
#             user = form.save()

#             # Si el usuario se crea correctamente 
#             if user is not None:
#                 # Hacemos el login manualmente
#                 do_login(request, user)
#                 # Y le redireccionamos a la portada
#                 return redirect('/')

#     # Si llegamos al final renderizamos el formulario
#     return render(request, "usersApp/register.html",{'form': form})

def logout(request):
    do_logout(request)
    #edireccionamos a la portada
    return redirect('/')    