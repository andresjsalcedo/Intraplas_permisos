from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import  usuario
from .forms import RegistroForm, LoginForm
# Create your views here.

#VISTA PARA USUARIOS INTRAPLAS SAS

def adminpanel(request):
    usuarios = usuario.objects.all()
    return render(
        request,
        'post/list.html', {'usuarios': usuarios}
    )



# Vista para el registro de usuarios intraplas
def registrointraplas(request):
   # Si la solicitud es de tipo POST
   if request.method == 'POST':
       # Se crea un formulario RegistroForm con los datos enviados en la solicitud
       form = RegistroForm(request.POST)
       # Si el formulario es válido
       if form.is_valid():
           # Se guarda el nuevo usuario
           form.save()
           # Se redirige al usuario a la página de inicio de sesión
           return redirect('loginintraplas')
   # Si la solicitud no es de tipo POST
   else:
       # Se crea un formulario RegistroForm vacío
       form = RegistroForm()
   # Se renderiza la plantilla 'pagina_inicial/registro.html' pasando el formulario como contexto
   return render(request, 'registrointraplas.html', {'form': form})

# Vista para el inicio de sesión intraplas
def loginintraplas(request):
   # Si la solicitud es de tipo POST
   if request.method == 'POST':
       # Se crea un formulario LoginForm con los datos enviados en la solicitud
       form = LoginForm(request, data=request.POST)
       # Si el formulario es válido
       if form.is_valid():
           # Se obtiene el usuario del formulario
           user = form.get_user()
           # Se inicia sesión con el usuario
           auth_login(request, user)
           # Se redirige al usuario a la lista de la página inicial
           return redirect('adminpanel')
   # Si la solicitud no es de tipo POST
   else:
       # Se crea un formulario LoginForm vacío
       form = LoginForm()
   # Se renderiza la plantilla 'pagina_inicial/loginintraplas.html' pasando el formulario como contexto
   return render(request, 'loginintraplas.html', {'form': form})

# Vista para cerrar sesión intraplas
@login_required
def logoutintraplas(request):
   # Se cierra la sesión del usuario
   auth_logout(request)
   # Se redirige al usuario a la página de inicio de sesión
   return redirect('loginintraplas')

# Vista para la página inicial protegida intraplas
@login_required
def adminpanel_view(request):
   # Se renderiza la plantilla 'pagina_inicial/adminpanel.html' pasando el usuario actual como contexto
   return render(request, 'adminpanel.html', {'user': request.user})