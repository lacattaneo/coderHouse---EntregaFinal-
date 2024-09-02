from django import forms
from AppFinal.models import Usuario, Evento, CompraEntrada

class FormularioRegistro(forms.ModelForm):
        contraseña = forms.CharField(widget=forms.PasswordInput)

        class Meta:
                model = Usuario
                fields = ['nombre', 'apellido', 'email', 'telefono', 'nacionalidad', 'contraseña']

class FormularioLogin(forms.Form):
        email = forms.EmailField(label='Email')
        contraseña = forms.CharField(label='Contraseña',widget=forms.PasswordInput)


class SeleccionarEventoForm(forms.Form):
        evento = forms.ModelChoiceField(
                queryset=Evento.objects.all(),
                widget=forms.Select(attrs={'class': 'form-control'}),
                label='Seleccionar Evento')
        cantidad = forms.IntegerField(
                min_value=1,
                widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad de Entradas'}),
                label='Cantidad de Entradas')