from django.shortcuts import redirect, render
from .forms import factura_servicio_form, vehiculo_form
from .models import Factura, Factura_servicio, Servicio, Vehiculo, Persona
from datetime import datetime, date

# Create your views here.
def inicio_view(request):
    return render(request, 'web/inicio.html', locals())    

def vehiculo_add_view(request):
    usuario = Persona.objects.get(id_user = request.user.id)
    if request.method == 'POST':
        form_v = vehiculo_form(request.POST)
        if form_v.is_valid():
            v = form_v.save(commit=False)
            v.propietario = usuario
            v.save()
            return redirect('/mis_vehiculos/')
    else:
        form_v = vehiculo_form()
    return render(request, 'web/agregar_vehiculo.html', locals())

def vehiculo_edit_view(request, id_vehiculo):
    vehiculo = Vehiculo.objects.get(id = id_vehiculo)
    if request.method == 'POST':
        form_v = vehiculo_form(request.POST, instance=vehiculo)
        if form_v.is_valid():
            form_v.save()
            return redirect('/mis_vehiculos/')
    else:
        form_v = vehiculo_form(instance=vehiculo)
    return render(request, 'web/editar_vehiculo.html', locals())
    
def mis_vehiculos_view(request):
    usuario = Persona.objects.get(id_user = request.user.id)
    object = Vehiculo.objects.filter(propietario = usuario)
    return render (request, 'web/mis_vehiculos.html', locals())

def fatura_view(request):
    factura = Factura_servicio.objects.filter(vehiculo__propietario__id_user = request.user)
    return render (request, 'web/factura.html', locals())

def fatura_add_view(request):
    id_factura = Factura.objects.create()
    return redirect('servicio/{}'.format(id_factura.id))

def fatura_destalles_view(request, id_factura):
    services = Factura_servicio.objects.filter(factura = id_factura)
    print(services)
    return render (request, 'web/factura_detalles.html', locals())

def factura_servicio_view(request, id_factura):
    factura = Factura.objects.get(id = id_factura)
    if request.method == 'POST':
        form_f = factura_servicio_form(request.POST)
        if form_f.is_valid():
            fecha1 = form_f.cleaned_data['hora_inicio']
            fecha2 = form_f.cleaned_data['hora_fin']
            cantid = form_f.cleaned_data['cantidad']
            f = form_f.save(commit=False)
            servicio = Servicio.objects.get(id = f.servicio.id)
            precio = servicio.valor
            tipo = servicio.tipos
            f.factura = factura
            if tipo == 'Horas':
                fecha = fecha2 - fecha1
                total = int(fecha.seconds/3600) * int(precio) * int(cantid)
                
            if tipo == 'Mensual':
                total = int(precio) * int(cantid)
                
            if tipo == 'Nocturno':
                formHora = "%H:%M:%S"
                hora = "08:00:00"
                hora = datetime.strptime(hora, formHora).time()
                if fecha2.time() > hora:
                    
                    h= datetime.combine(date.today(), fecha2.time()) - datetime.combine(date.today(), hora)
                    total = (int(h.seconds/3600) * 1500) + int(precio)
                    
                else:
                    total = precio

            f.subtotal = total    
            semitotal =factura.total
            factura.total = int(semitotal)+ int(total)
            factura.save()
            f.save()
            return redirect('factura/')

    else:
        form_f = factura_servicio_form()
    return render (request, 'web/facturaservicio.html', locals())



