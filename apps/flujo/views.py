from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required, permission_required


from apps.flujo.models import Flujo, Actividad
from apps.flujo.forms import FlujoModelForm, ActividadModelForm


@login_required
def menu_flujo(request):
    return render(request, 'flujo/menu_flujo.html')

@login_required
@permission_required('flujo.add_flujo')
def crear_flujo(request):
	form = FlujoModelForm()

	if request.method == 'POST':
		form = FlujoModelForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('flujo:listar_flujos'))

	return render(request, 'flujo/crear_flujo.html', {'form':form})


def modificar_flujo(request, flujo_id):
	flujo = Flujo.objects.get(pk=flujo_id)
	form = FlujoModelForm(instance=flujo)

	if request.method=='POST':
		form = FlujoModelForm(request.POST, instance=flujo)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('flujo:listar_flujos'))

	context = {'form':form, 'flujo_id':flujo_id}
	return render(request, 'flujo/modificar_flujo.html', context)





def eliminar_flujo(request, flujo_id):
	flujo = Flujo.objects.get(pk=flujo_id)
	flujo.delete()
	return HttpResponseRedirect(reverse('flujo:listar_flujos'))


def listar_flujos(request):
	lista_flujos = Flujo.objects.all().order_by('pk')
	context = {'lista_flujos':lista_flujos}
	return render(request, 'flujo/listar_flujos.html', context)

	

def desplegar_flujo(request, flujo_id):
	flujo = Flujo.objects.get(pk=flujo_id)
	lista_actividades = Actividad.objects.filter(flujo=flujo).order_by('pk')
	context = {'flujo':flujo, 'lista_actividades':lista_actividades}
	return render(request, 'flujo/desplegar_flujo.html', context)








# Actividades


@login_required
def menu_actividad(request):
    return render(request, 'flujo/menu_actividad.html')

def crear_actividad(request):
	form = ActividadModelForm()

	if request.method == 'POST':
		form = ActividadModelForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('flujo:listar_actividades'))

	return render(request, 'flujo/crear_actividad.html', {'form':form})

def modificar_actividad(request, actividad_id):
	actividad = Actividad.objects.get(pk=actividad_id)
	form = ActividadModelForm(instance=actividad)

	if request.method=='POST':
		form = ActividadModelForm(request.POST, instance=actividad)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('flujo:listar_actividades'))

	context = {'form':form, 'actividad_id':actividad_id}
	return render(request, 'flujo/modificar_actividad.html', context)





def eliminar_actividad(request, actividad_id):
	actividad = Actividad.objects.get(pk=actividad_id)
	actividad.delete()
	return HttpResponseRedirect(reverse('flujo:listar_actividades'))


def listar_actividades(request):
	lista_actividades = Actividad.objects.all().order_by('pk')
	context = {'lista_actividades':lista_actividades}
	return render(request, 'flujo/listar_actividades.html', context)



