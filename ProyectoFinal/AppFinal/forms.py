from django import forms
from .models import Usuario

class FormularioRegistro(forms.Form):
        nombre = forms.CharField(
                label="Nombre",
                max_length=100,
                widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
        
        apellido = forms.CharField(
                label="Apellido",
                max_length=100,
                widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
        
        email = forms.EmailField(
                label="Email",
                max_length=100,
                widget=forms.TextInput(attrs={'placeholder': 'Correo Electronico'}))

        telefono = forms.IntegerField(
                label="telefono",
                widget=forms.TextInput(attrs={'placeholder': 'telefono'}))

        nacionalidad = forms.CharField(
                label="nacionalidad",
                max_length=100,
                widget=forms.TextInput(attrs={'placeholder': 'nacionalidad'}))
        
        contraseña = forms.CharField(
                label="Contraseña",
                max_length=100,
                widget=forms.PasswordInput(attrs={'placeholder': 'comtraseña'}))

        

class FormularioLogin(forms.Form):
        nombre = forms.CharField(
                label="Nombre",
                max_length=100,
                widget=forms.TextInput(attrs={'placeholder': 'nombre'}))
        
        contraseña = forms.CharField(
                label="Contraseña",
                max_length=100,
                widget=forms.PasswordInput(attrs={'placeholder': 'comtraseña'}))
        

        
        



