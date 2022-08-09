
from optparse import Values
from urllib import request
from django.shortcuts import render
from contextvars import Context
from multiprocessing import context
from SoporteHAWebapp.models import *
import datetime
from django.contrib import messages

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, reverse

from django.shortcuts import redirect, render
from django.http import HttpResponse


from .models import *
from .forms import *
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy



def entrada(request):
    return redirect("index")

def Base(request):
    return render(request,"SoporteHAWebapp/base.html", {},)

def Inicio(request):
     return render(request,"SoporteHAWebapp/index.html", {},)

@login_required
def Remoto_MDA(request):
     return render(request,"SoporteHAWebapp/remotomda.html", {},)
 
@login_required
def Procedimientos(request):
     return render(request,"SoporteHAWebapp/procedimientos.html", {},)

     """
     modulo de la problematicas, derivar 
     """

@login_required
def Programas_medicos (request):
    
    resultado_programas_medicos = Problematicas_sectores.objects.all()
         
    return render ( request, "SoporteHAWebapp/proyectos.html",{"programas_medicos" : resultado_programas_medicos})

@login_required
def Sectores(request):
    
    sector = CrearSectores.objects.all
         
    return render ( request, "SoporteHAWebapp/sector.html",{"sector" : sector})

@login_required   
def buscarsector(request):
    
    if request.method == "POST":
    
        buscar = request.POST.get("search")
    
        if buscar != "":
            resultado = Publicaciones.objects.filter( Q (titulo__icontains=buscar) | Q (descripcion__icontains=buscar) ).values()
        
            return render ( request, "SoporteHAWebapp/buscarsector.html",{"resultado": resultado, "search":buscar}) 
    
    resultado = []

    return render ( request, "SoporteHAWebapp/buscarsector.html",{})

class ver_sectores(DetailView):

    model = CrearSectores
    template_name = "SoporteHAWebapp/ver_sector.html"

@login_required
def crear_publicacion(request):

    autor = User.get_username(request.user)
    if request.method == "POST":
        
        publicacion = CrearPublicacion(request.POST, request.FILES)
        
        if publicacion.is_valid():

            informacion = publicacion.cleaned_data

            publicacion_nueva = Publicaciones(imagenone=informacion["imagenone"],
                                              imagentwo=informacion["imagentwo"],
                                              imagenthree=informacion["imagenthree"],
                                              titulo=informacion["titulo"],
                                              descripcion=informacion["descripcion"],
                                              fecha=datetime.datetime.today(),
                                              autor=request.user)
            publicacion_nueva.save()
            
            messages.success(request, "El comentario fue publicado.") 
            return redirect('inicio')

            
        
        return render(request, "SoporteHAWebapp/crearpublicacion.html", {"publicacion":publicacion})
    
    publicacion = CrearPublicacion()
    return render(request, 'SoporteHAWebapp/crearpublicacion.html', {'publicacion':publicacion})

@login_required
def blog(request):
    
    blogg = Publicaciones.objects.all
         
    return render ( request, "SoporteHAWebapp/blog.html",{"blogg" : blogg})

@login_required   
def buscarblog(request):
    
    if request.method == "POST":
    
        buscar = request.POST.get("search")
    
        if buscar != "":
            resultado = Publicaciones.objects.filter( Q (titulo__icontains=buscar) | Q (descripcion__icontains=buscar) ).values()
        
            return render ( request, "SoporteHAWebapp/buscarblog.html",{"resultado": resultado, "search":buscar}) 
    
    resultado = []

    return render ( request, "SoporteHAWebapp/buscarblog.html",{})

class ver_publicacion(DetailView):

    model = Publicaciones
    template_name = "SoporteHAWebapp/ver_publicacion.html"

def registro(request):

    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            form.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')            
            else:
                pass
                #return redirect('login')
        
        return render(request, 'SoporteHAWebapp/registro.html', {"form":form})
    
    form = UserRegisterForm()

    return render(request, 'SoporteHAWebapp/registro.html', {"form":form})

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        else:
            return redirect("login")
    
    form = AuthenticationForm()

    return render(request,"SoporteHAWebapp/login.html",{"form":form})

def logout_request(request):
    logout(request)
    return redirect("inicio")

@login_required
def editar_perfil(request):

    user = request.user

    if request.method == "POST":

        form = UserEditForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data
            user.email = info['email']
            user.first_name = info['first_name']
            user.last_name = info['last_name']

            user.save()

            return redirect('inicio')

    else:
        form = UserEditForm(initial={'email':user.email, "first_name":user.first_name, "last_name":user.last_name})
    
    return render (request, 'SoporteHAWebapp/editarperfil.html', {"form":form})

@login_required
def perfil(request):      
    
    return render(request, "SoporteHAWebapp/perfil.html",{})

class cambiar_password(PasswordChangeView):
    form = PasswordChangeForm
    success_url = reverse_lazy('editar_perfil') 

    def get_context_data(self, *args, **kwargs):
        contexto = super(cambiar_password, self).get_context_data()
        mensaje = messages.success(self.request, 'La contraseña se cambio correctamente')

        contexto['mensaje']=mensaje

        return contexto
    
@login_required
def agregar_avatar(request):

    if request.method == "POST":

        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            user = request.user

            avatar = Avatar(user=user, imagen=form.cleaned_data["imagen"])

            avatar.save()

            messages.success(request, "El avatar se agrego exitosamente.") 
            return redirect("editar_perfil")

    else:

        form = AvatarForm()

    
    return render(request, "SoporteHAWebapp/agregar_avatar.html", {"form":form})

@login_required
def editar_publicacion(request, publicacion_id):
    
    publicacion = Publicaciones.objects.get(id=publicacion_id)

    if request.method == "POST":

        formulario = CrearPublicacion(request.POST, request.FILES)

        if formulario.is_valid():

            info_publicacion = formulario.cleaned_data

            publicacion.imagen = info_publicacion["imagen"]
            publicacion.titulo = info_publicacion["titulo"]
            publicacion.descripcion = info_publicacion["descripcion"]           

            publicacion.save()
            messages.success(request, "La publicacion se edito exitosamente.") 
            
            return redirect ("blog-usuario")

    
    formulario = CrearPublicacion(initial={"titulo":publicacion.titulo, "descripcion":publicacion.descripcion, "fecha_viaje":datetime.datetime.today()})

    return render (request, "SoporteHAWebapp/editar_publicacion.html", {"form":formulario})

@login_required
def eliminar_publicacion(request, publicacion_id):

    publicacion = Publicaciones.objects.get(id=publicacion_id)
    publicacion.delete()

    messages.success(request, "La publicacion se elimino exitosamente.") 
    return redirect("blog-usuario")