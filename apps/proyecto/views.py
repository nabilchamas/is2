from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required, permission_required

from apps.proyecto.models import Proyecto
from apps.userstory.models import UserStory
from apps.sprint.models import Sprint
from apps.flujo.models import Flujo, Actividad
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
    if request.method == 'POST':
        form = ProyectoModelForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('proyecto:listar_proyectos'))

    form = ProyectoModelForm()
    context = {'form':form}
    return render(request, 'proyecto/crear_proyecto.html', context)



@login_required
@permission_required('proyecto.change_proyecto')
def modificar_proyecto(request, proyecto_id):
    '''
        Modifica un nuevo proyecto
    '''

    proyecto = Proyecto.objects.get(pk=proyecto_id)
    form = ProyectoModelForm(instance=proyecto)

    if request.method == 'POST':
        form = ProyectoModelForm(request.POST, instance=proyecto)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('proyecto:listar_proyectos'))

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

    lista_proyectos = Proyecto.objects.all().order_by('pk')
    context = {'lista_proyectos':lista_proyectos}
    return render(request, 'proyecto/listar_proyectos.html', context)

def informe_proyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    lista_user_stories = UserStory.objects.all().filter(proyecto=proyecto)
    lista_sprints = Sprint.objects.all().filter(proyecto=proyecto).order_by('nombre')
    flujo = Flujo.objects.get(proyecto=proyecto)
    primera_actividad = Actividad.objects.order_by('pk').filter(flujo=flujo)[0]
    ultima_actividad = Actividad.objects.order_by('pk').reverse().filter(flujo=flujo)[0]



    context = {'proyecto':proyecto, 'lista_user_stories':lista_user_stories,
    'lista_sprints':lista_sprints, 'primera_actividad':primera_actividad, 
    'ultima_actividad':ultima_actividad}
    return render(request, 'proyecto/informe_proyecto.html', context)
