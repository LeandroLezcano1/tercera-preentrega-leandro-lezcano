from django.shortcuts import render
from .models import Trabajador
from .forms import BuscarTrabajadorForm

# Create your views here.

def buscar_trabajador(request):
    if request.method == 'GET':
        form = BuscarTrabajadorForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            antiguedad = form.cleaned_data['antiguedad']
            trabajadores = Trabajador.objects.filter(nombre__icontains=nombre, apellido__icontains=apellido, fecha_nacimiento=fecha_nacimiento, antiguedad=antiguedad)
    else:
        form = BuscarTrabajadorForm()
        trabajadores = Trabajador.objects.all()
    context = {'form': form, 'trabajadores': trabajadores}
    return render(request, 'buscar_trabajador.html', context)

def pagina_principal(request):
    return render(request, 'base.html')