from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from apps.userstory.models import UserStory
from apps.flujo.models import Flujo, Actividad
from apps.userstory.forms import UserStoryModelForm

from django.core.mail import send_mail
from django.conf import settings


def menu_userstory(request):
    """
        Sirve para acceder al menu de userstory
    """

    return render(request, 'userstory/menu_userstory.html')


def crear_userstory(request):
    """
        Crea un nuevo userstory
    """

    if request.method == 'POST':
        form = UserStoryModelForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('userstory:listar_userstories'))

    form = UserStoryModelForm()
    context = {'form':form}
    return render(request, 'userstory/crear_userstory.html', context)


def modificar_userstory(request, userstory_id):
    '''
        Modifica un userstory
    '''

    userstory = UserStory.objects.get(pk=userstory_id)
    form = UserStoryModelForm(instance=userstory)

    if request.method == 'POST':
        form = UserStoryModelForm(request.POST, instance=userstory)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('userstory:listar_userstories'))

    context = {'form':form, 'userstory_id':userstory_id}
    return render(request, 'userstory/modificar_userstory.html', context)



def modificar_en_flujo(request, userstory_id):
    '''
        Modifica un userstory seleccionado desde el desplegue de flujo 
    '''

    userstory = UserStory.objects.get(pk=userstory_id)
    flujo = userstory.flujo
    lista_actividades = Actividad.objects.filter(flujo=flujo).order_by('id')
    form = UserStoryModelForm(instance=userstory)

    if request.method=='POST':
        form = UserStoryModelForm(request.POST, instance=userstory)

        if form.is_valid():
            subject = 'Cambios en ' + form.cleaned_data.get('nombre')
            mensaje = '\n'

            # mensaje += form.

            mensaje += '\nUsuario: ' + str(request.user)

            # if userstory.nombre != form.cleaned_data.get('nombre'):
            mensaje += '\nUserstory: ' + form.cleaned_data.get('nombre')

            # if userstory.estado != form.cleaned_data.get('estado'):
            mensaje += '\nEstado: ' + form.cleaned_data.get('estado')

            # if userstory.prioridad != form.cleaned_data.get('prioridad'):
            mensaje += '\nPrioridad: ' + form.cleaned_data.get('prioridad')

            # mensaje = str(form.fields['nombre'])


            send_mail(subject, mensaje, settings.EMAIL_HOST_USER,
            ['is2.r12.2015@gmail.com'])

            form.save()
            context = {'flujo_id':flujo.id}
            return HttpResponseRedirect(reverse('flujo:desplegar_flujo', kwargs=context))


    context = {'form':form, 'userstory_id':userstory_id, 
            'flujo':flujo, 'lista_actividades':lista_actividades}
    return render(request, 'userstory/modificar_en_flujo.html', context)







def eliminar_userstory(request, userstory_id):
    '''
        Elimina un userstory
    '''

    userstory = UserStory.objects.get(pk=userstory_id)
    userstory.delete()
    return HttpResponseRedirect(reverse('userstory:listar_userstories'))


def listar_userstories(request):
    '''
        Lista los userstories 
    '''

    lista_userstories = UserStory.objects.all().order_by('nombre')
    context = {'lista_userstories':lista_userstories}
    return render(request, 'userstory/listar_userstories.html', context)



