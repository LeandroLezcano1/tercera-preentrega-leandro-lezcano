from django import forms
from .models import TrabajadorReciente, TrabajadorAntiguo, TrabajadorPrueba

class TrabajadorRecienteForm(forms.ModelForm):
    class Meta:
        model = TrabajadorReciente
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'antiguedad']

class TrabajadorAntiguoForm(forms.ModelForm):
    class Meta:
        model = TrabajadorAntiguo
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'antiguedad']

class TrabajadorPruebaForm(forms.ModelForm):
    class Meta:
        model = TrabajadorPrueba
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'antiguedad']

class BuscarTrabajadorForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)
    fecha_nacimiento = forms.DateField(required=False)
    antiguedad = forms.CharField(max_length=100, required=False)
