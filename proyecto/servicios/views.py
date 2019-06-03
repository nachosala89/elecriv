from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse
from django.template import loader

from .models import Servicio, Cliente, EmpleadoDeCuadrilla, Cuadrilla, Tarea, ParteDeTrabajo

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import ServicioForm, TareaForm, ParteForm, ParteJefeForm, ClienteForm, CuadrillaForm, EmpleadoForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.utils import timezone

@login_required
def index(request):
    lista_servicios = Servicio.objects.order_by('-fecha_solcitud')[:20]
    context = {'lista_servicios': lista_servicios}
    return render(request, 'servicios/index.html', context)

            
@login_required
def detalle(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    es_coordinador = es_miembro(request, 'coordinador')
    context = {'servicio': servicio, 'es_coordinador': es_coordinador}
    return render(request, 'servicios/detalle.html', context)

@login_required
def nuevo_servicio(request):
    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            servicio = form.save(commit=False)
            servicio.save()
            return HttpResponseRedirect(reverse('servicios:detalle', args=(servicio.id,)))
    else:
        form = ServicioForm(initial={'fecha_solcitud': timezone.now(), 'fecha_inicio': timezone.now(), 'estado': 'Pendiente'})
    return render(request, 'servicios/editar_servicio.html', {'form': form})


@login_required    
def editar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    if request.method == "POST":
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            servicio = form.save(commit=False)
            servicio.save()
            return HttpResponseRedirect(reverse('servicios:detalle', args=(servicio.id,)))
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'servicios/editar_servicio.html', {'form': form})


@login_required    
def eliminar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    servicio.delete()
    return HttpResponseRedirect(reverse('servicios:index'))    


def finalizar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    servicio.estado = 'Finalizado'
    servicio.fecha_fin = timezone.now()
    servicio.save()
    return HttpResponseRedirect(reverse('servicios:detalle', args=(servicio.id,)))
    

@login_required        
def tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    es_coordinador = es_miembro(request, 'coordinador')
    context = {'tarea': tarea, 'es_coordinador': es_coordinador}
    return render(request, 'servicios/tarea.html', context)

@login_required
def nueva_tarea(request, servicio_id):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)            
            tarea.save()
            servicio = Servicio.objects.get(pk=servicio_id)
            servicio.estado = 'En curso'
            servicio.save()
            return HttpResponseRedirect(reverse('servicios:tarea', args=(tarea.id,)))
    else:
        form = TareaForm(initial={'servicio': servicio_id, 'estado': 'Pendiente'})
    return render(request, 'servicios/editar_tarea.html', {'form': form})

@login_required    
def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.save()
            return HttpResponseRedirect(reverse('servicios:tarea', args=(tarea.id,)))
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'servicios/editar_tarea.html', {'form': form})    

@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    servicio_id=tarea.servicio.id
    tarea.delete()
    return HttpResponseRedirect(reverse('servicios:detalle', args=(servicio_id,)))    

def finalizar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    tarea.estado = 'Finalizado'
    tarea.save()
    return HttpResponseRedirect(reverse('servicios:tarea', args=(tarea.id,)))


@login_required
def parte(request, parte_id):
    parte = get_object_or_404(ParteDeTrabajo, pk=parte_id)
    return render(request, 'servicios/parte.html', {'parte': parte, 'es_coordinador': es_miembro(request, 'coordinador')})

@login_required
def nuevo_parte(request, tarea_id):
    if request.method == "POST":
        form = ParteForm(request.POST)
        if form.is_valid():
            parte = form.save(commit=False)
            parte.save()
            tarea = Tarea.objects.get(pk=tarea_id)
            tarea.estado = 'En curso'
            tarea.save()
            return HttpResponseRedirect(reverse('servicios:parte', args=(parte.id,)))
    else:
        form = ParteForm(initial={'tarea': tarea_id, 'fecha': timezone.now() })
    return render(request, 'servicios/editar_parte.html', {'form': form})


def nuevo_parte_jefe(request, tarea_id):
    if request.method == "POST":
        form = ParteJefeForm(request.POST)
        if form.is_valid():
            parte = form.save(commit=False)
            parte.aprobado_por = EmpleadoDeCuadrilla.objects.get(apellido=request.user.last_name)
            parte.save()
            tarea = Tarea.objects.get(pk=tarea_id)
            tarea.estado = 'En curso'
            tarea.save()
            return HttpResponseRedirect(reverse('servicios:parte', args=(parte.id,)))
    else:
        form = ParteJefeForm(initial={'tarea': tarea_id, 'fecha': timezone.now()})
    return render(request, 'servicios/editar_parte.html', {'form': form})

@login_required    
def editar_parte(request, parte_id):
    parte = get_object_or_404(ParteDeTrabajo, pk=parte_id)
    if request.method == "POST":
        form = ParteForm(request.POST, instance=parte)
        if form.is_valid():
            parte = form.save(commit=False)
            parte.save()
            return HttpResponseRedirect(reverse('servicios:parte', args=(parte.id,)))
    else:
        form = ParteForm(instance=parte)
    return render(request, 'servicios/editar_parte.html', {'form': form})    

@login_required
def eliminar_parte(request, parte_id):
    parte = get_object_or_404(ParteDeTrabajo, pk=parte_id)
    tarea_id=parte.tarea.id
    parte.delete()
    return HttpResponseRedirect(reverse('servicios:tarea', args=(tarea_id,)))    

def aprobar_parte(request, parte_id):
    parte = get_object_or_404(ParteDeTrabajo, pk=parte_id)
    parte.aprobado_por = EmpleadoDeCuadrilla.objects.get(apellido=request.user.last_name)
    parte.save()
    return HttpResponseRedirect(reverse('servicios:parte', args=(parte_id,)))    


@login_required
def clientes(request):
    lista_clientes = Cliente.objects.order_by('-nombre')[:20]
    context = {'lista_clientes': lista_clientes}
    return render(request, 'servicios/clientes.html', context)

@login_required
def cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render(request, 'servicios/cliente.html', {'cliente': cliente})

@login_required
def nuevo_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)            
            cliente.save()
            return HttpResponseRedirect(reverse('servicios:cliente', args=(cliente.id,)))
    else:
        form = ClienteForm()
    return render(request, 'servicios/editar_cliente.html', {'form': form})

@login_required    
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return HttpResponseRedirect(reverse('servicios:cliente', args=(cliente.id,)))
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'servicios/editar_cliente.html', {'form': form})    

@login_required
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    cliente.delete()
    return HttpResponseRedirect(reverse('servicios:clientes'))    
    

@login_required
def empleado(request, empleado_id):
    empleado = get_object_or_404(EmpleadoDeCuadrilla, pk=empleado_id)
    return render(request, 'servicios/empleado.html', {'empleado': empleado})

@login_required
def nuevo_empleado(request, cuadrilla_id):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)            
            empleado.save()
            return HttpResponseRedirect(reverse('servicios:empleado', args=(empleado.id,)))
    else:
        form = EmpleadoForm(initial={'cuadrilla': cuadrilla_id})
    return render(request, 'servicios/editar_empleado.html', {'form': form})

@login_required    
def editar_empleado(request, empleado_id):
    empleado = get_object_or_404(EmpleadoDeCuadrilla, pk=empleado_id)
    if request.method == "POST":
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.save()
            return HttpResponseRedirect(reverse('servicios:empleado', args=(empleado.id,)))
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'servicios/editar_empleado.html', {'form': form})    

@login_required
def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(EmpleadoDeCuadrilla, pk=empleado_id)
    cuadrilla_id = empleado.cuadrilla.id
    empleado.delete()
    return HttpResponseRedirect(reverse('servicios:cuadrilla', args=(cuadrilla_id,)))    


@login_required
def cuadrillas(request):
    lista_cuadrillas = Cuadrilla.objects.order_by('-especialidad')[:10]
    context = {'lista_cuadrillas': lista_cuadrillas}
    return render(request, 'servicios/cuadrillas.html', context)

@login_required
def cuadrilla(request, cuadrilla_id):
    cuadrilla = get_object_or_404(Cuadrilla, pk=cuadrilla_id)
    return render(request, 'servicios/cuadrilla.html', {'cuadrilla': cuadrilla})

@login_required
def nueva_cuadrilla(request):
    if request.method == "POST":
        form = CuadrillaForm(request.POST)
        if form.is_valid():
            cuadrilla = form.save(commit=False)            
            cuadrilla.save()
            return HttpResponseRedirect(reverse('servicios:cuadrilla', args=(cuadrilla.id,)))
    else:
        form = CuadrillaForm()
    return render(request, 'servicios/editar_cuadrilla.html', {'form': form})

@login_required    
def editar_cuadrilla(request, cuadrilla_id):
    cuadrilla = get_object_or_404(Cuadrilla, pk=cuadrilla_id)
    if request.method == "POST":
        form = CuadrillaForm(request.POST, instance=cuadrilla)
        if form.is_valid():
            cuadrilla = form.save(commit=False)
            cuadrilla.save()
            return HttpResponseRedirect(reverse('servicios:cuadrilla', args=(cuadrilla.id,)))
    else:
        form = CuadrillaForm(instance=cuadrilla)
    return render(request, 'servicios/editar_cuadrilla.html', {'form': form})    

@login_required
def eliminar_cuadrilla(request, cuadrilla_id):
    cuadrilla = get_object_or_404(Cuadrilla, pk=cuadrilla_id)
    cuadrilla.delete()
    return HttpResponseRedirect(reverse('servicios:cuadrillas'))    

@login_required
def seleccionar_jefe(request, cuadrilla_id):
    cuadrilla = get_object_or_404(Cuadrilla, pk=cuadrilla_id)
    context = {'cuadrilla': cuadrilla}
    return render(request, 'servicios/seleccionar_jefe.html', context)
    
@login_required
def seleccionar_jefe2(request, cuadrilla_id):
    cuadrilla = get_object_or_404(Cuadrilla, pk=cuadrilla_id)
    try:
        jefe_selec = cuadrilla.empleadodecuadrilla_set.get(pk=request.POST['empleado'])
    except (KeyError, EmpleadoDeCuadrilla.DoesNotExist):
        return render(request, 'servicios/seleccionar_jefe.html', {
            'cuadrilla': cuadrilla,
            'error_message': "No se seleccionó jefe",
        })
    else:
        for empleado in cuadrilla.empleadodecuadrilla_set.all():
            if empleado == jefe_selec:
                empleado.es_jefe = True
            else:
                empleado.es_jefe = False
            empleado.save()
                        
        return HttpResponseRedirect(reverse('servicios:cuadrilla', args=(cuadrilla.id,)))


def es_miembro(request, grupo):
    return request.user.groups.filter(name=grupo).exists()
