from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from apps.sprint.models import Sprint
from apps.sprint.forms import SprintModelForm



def menu_sprint(request):
	"""
		Sirve para acceder al menu de sprint
	"""

	return render(request, 'sprint/menu_sprint.html')




def crear_sprint(request):
	"""
		Crea un nuevo sprint
	"""

	if request.method == 'POST':
		form = SprintModelForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('sprint:listar_sprints'))

	form = SprintModelForm()
	context = {'form':form}
	return render(request, 'sprint/crear_sprint.html', context)


def modificar_sprint(request, sprint_id):
	'''
		Modifica un sprint
	'''

	sprint = Sprint.objects.get(pk=sprint_id)
	form = SprintModelForm(instance=sprint)

	if request.method == 'POST':
		form = SprintModelForm(request.POST, instance=sprint)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('sprint:listar_sprints'))

	context = {'form':form, 'sprint_id':sprint_id}
	return render(request, 'sprint/modificar_sprint.html', context)





def eliminar_sprint(request, sprint_id):
	'''
		Elimina un sprint
	'''
	sprint = Sprint.objects.get(pk=sprint_id)
	sprint.delete()
	return HttpResponseRedirect(reverse('sprint:listar_sprints'))



def listar_sprints(request):
	'''
		Lista los sprints
	'''

	lista_sprints = Sprint.objects.all().order_by('nombre')
	context = {'lista_sprints':lista_sprints}
	return render(request, 'sprint/listar_sprints.html', context)







