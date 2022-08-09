
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from ckeditor.fields import *


class CrearSectores(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = RichTextField(blank=True, null=True)
    fecha= models.DateField()
    autor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) 

    class Meta:
        verbose_name_plural = "CrearSectores"
        
        
class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatar/', blank=True, null=True)
    
class mda_usuario(models.Model):

    nombre = models.CharField(max_length=30) # Texto
    apellido = models.CharField(max_length=30) # Texto
    email = models.EmailField(blank=True, null=True) # Email - Opcional

class mda_admin_usuario(models.Model):

    nombre = models.CharField(max_length=30) # Texto
    apellido = models.CharField(max_length=30) # Texto
    email = models.EmailField(blank=True, null=True) # Email - Opcional

    profesion = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Usuarios"

class Publicaciones(models.Model):
    imagenone = models.ImageField(null=True, blank=True)
    imagentwo = models.ImageField(null=True, blank=True)
    imagenthree = models.ImageField(null=True, blank=True)
    titulo = models.CharField(max_length=50)
    descripcion = RichTextField(blank=True, null=True)
    fecha= models.DateField()
    autor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) 

    class Meta:
        verbose_name_plural = "Publicaciones"
        db_table = "imageupload"

        


    
    
    
    

