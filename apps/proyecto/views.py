from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required, permission_required

from apps.proyecto.models import Proyecto
from apps.proyecto.forms import ProyectoModelForm

@login_required
def menu_proyecto(request):
    """
        Sirve para acceder al menu de proyecto
    """
    return render(request, 'proyecto/menu_proyecto.html')

@login_required
@permission_required('proyecto.add_proyecto')
def crear_proyecto(request):
    """
        Crea un nuevo proyecto
    """
    if request.method == 'GET':
        form = ProyectoModelForm()

    else:    
        form = ProyectoModelForm(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            codigo = form.cleaned_data['codigo']
            descripcion = form.cleaned_data['descripcion']
            cliente = form.cleaned_data['cliente']

            proyecto = Proyecto.objects.create(
                nombre = nombre,
                codigo = codigo,
                descripcion = descripcion,
                cliente = cliente
                )
            proyecto.save()
            return HttpResponseRedirect(reverse('proyecto:listar_proyectos'))

    return render(request, 'proyecto/crear_proyecto.html', {'form':form})

@login_required
@permission_required('proyecto.change_proyecto')
def modificar_proyecto(request, proyecto_id):
    '''
        Modifica un nuevo proyecto
    '''

    if request.method == 'POST':    
        form = ProyectoModelForm(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            codigo = form.cleaned_data['codigo']
            descripcion = form.cleaned_data['descripcion']
            cliente = form.cleaned_data['cliente']

            proyecto = Proyecto.objects.get(pk=proyecto_id)
            proyecto.nombre = nombre
            proyecto.codigo = codigo
            proyecto.descripcion = descripcion
            proyecto.cliente = cliente
            proyecto.save()

            return HttpResponseRedirect(reverse('proyecto:listar_proyectos'))
    else:
        proyecto = Proyecto.objects.get(pk=proyecto_id)

        form = ProyectoModelForm(
            initial = {
                'nombre':proyecto.nombre,
                'codigo':proyecto.codigo,
                'descripcion':proyecto.descripcion,
                'cliente':proyecto.cliente
                }
            )

    context = {'form':form, 'proyecto_id':proyecto_id}
    return render(request, 'proyecto/modificar_proyecto.html', context)

@login_required
@permission_required('proyecto.remove_proyecto')
def eliminar_proyecto(request, proyecto_id):
    '''
        Elimina un proyecto
    '''

    proyecto = Proyecto.objects.get(pk=proyecto_id)
    proyecto.delete()
    return HttpResponseRedirect(reverse('proyecto:listar_proyectos'))

@login_required
def listar_proyectos(request):
    '''
        Lista los proyectos
    '''

    lista_proyectos = Proyecto.objects.all()
    context = {'lista_proyectos':lista_proyectos}
    return render(request, 'proyecto/listar_proyectos.html', context)
