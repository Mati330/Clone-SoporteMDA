from django.contrib import admin
from .models import *
from SoporteHAWebapp.models import *

class CrearSectoresadmin(admin.ModelAdmin):
    
    list_display= ('titulo', 'descripcion', 'fecha',)
    search_fields = ('titulo', 'descripcion', 'fecha',)
    
class mda_usuarioadmin(admin.ModelAdmin): # hereda modelo de aministrador, sin eso no aparece en el panel 
    
    list_display= ( 'nombre', 'apellido', 'email',)# los campos que puede  mostrar nombre, apellido y correo 
    search_fields = ( 'nombre', 'apellido', 'email',)# los campos que se puede buscar nombre, appelido y correo 



class PublicacionesAdmin(admin.ModelAdmin):
    
    list_display= ( 'titulo', 'descripcion', 'fecha',)
    search_fields = ( 'titulo', 'descripcion', 'fecha',)
    


admin.site.register(mda_usuario, mda_usuarioadmin)
admin.site.register(CrearSectores, CrearSectoresadmin) # le decimos como mostrarse en el panel de administracion 
admin.site.register(Publicaciones, PublicacionesAdmin)
    
    
"""
Esto es lo que hay que hacer para que podamos modificar " Problematica_sectores " 
Recorda crear superuser 
python manage.py createsuperuser
mati330
matty330
"""
# Register your models here.
