from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from .views import * # si ponemos .views importa todo lo de la carpeta 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   
    # URL Pryecto Soporte HA 
    
    path('', Inicio , name = 'inicio'),
    path('base/', Base),
    
    path('RemotoMDA/',Remoto_MDA , name= 'remoto'),
    path('Procedimientos/', Procedimientos, name= 'procedimientos'),
    path('Programas_medicos/',Programas_medicos, name= 'programas_medicos'),
    
    
    path('registro', registro, name='registro'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name='logout'),
    
    path('perfil', perfil, name='perfil'), 
    path('editarperfil', editar_perfil, name='editar_perfil'),  
    path('editarperfil/password', cambiar_password.as_view(template_name='SoporteHAWebapp/cambiar_pass.html'),name='cambiar_pass'),  
    path('agregar_avatar', agregar_avatar, name="agregar_avatar"),
    
    path('crearpublicacion', crear_publicacion, name='crear_publicacion'),
    path('editar_publicacion/<publicacion_id>', editar_publicacion, name='editar_publicacion'),
    
    path('sector/', Sectores, name= 'sector'),
    path('ver_sector/<pk>', ver_sectores.as_view(), name='ver_sector'),
    path('buscarsector/', buscarsector, name= 'buscarsector'),
    
    path('blog/', blog, name= 'blog-usuario'),
    path('buscarblog/', buscarblog, name= 'buscarblog'),
    path('publicaciones/<pk>', ver_publicacion.as_view(), name='ver_publicacion'),
    path('eliminar_publicacion/<publicacion_id>', eliminar_publicacion, name='eliminar_publicacion'),
    
    
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)