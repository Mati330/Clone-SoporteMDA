from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import *
from django.forms import  Textarea

from .models import*
"""
aca creamos el formulario, para no pasarlo en el html, se va mostrar de tomas maneras 
"""
class CrearPublicacion(forms.Form):
    imagenone = forms.ImageField(allow_empty_file=True)
    imagentwo = forms.ImageField(allow_empty_file=True)
    imagenthree = forms.ImageField(allow_empty_file=True)
    titulo = forms.CharField(max_length=50)
    descripcion = RichTextFormField()
    
class CrearSector(forms.Form):
    titulo = forms.CharField(max_length=50)
    descripcion = RichTextFormField()

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2',]
        #help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Email")  
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")    
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):

    imagen = forms.ImageField(label="Imagen", required=False)

    class Meta:

        model = Avatar
        fields = ['imagen']

