from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from userstory.models import UserStory
from userstory.forms import UserStoryModelForm


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

        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('userstory:menu_userstory'))

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

    lista_userstories = UserStory.objects.all()
    context = {'lista_userstories':lista_userstories}
    return render(request, 'userstory/listar_userstories.html', context)



