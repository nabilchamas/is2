from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required, permission_required

from apps.perfil.forms import PerfilModelForm

@login_required
def menu_perfil(request):
	return render(request, 'perfil/menu_perfil.html')

@login_required
@permission_required('auth.add_group')
def crear_perfil(request):
	if request.method == 'GET':
		form = PerfilModelForm()

	else:
		form = PerfilModelForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('perfil:listar_perfiles'))

	return render(request, 'perfil/crear_perfil.html', {'form':form})

@login_required
@permission_required('auth.change_group')
def modificar_perfil(request, perfil_id):
	perfil = Group.objects.get(pk=perfil_id)
	form = PerfilModelForm(instance=perfil)

	if request.method=='POST':
		form = PerfilModelForm(request.POST, instance=perfil)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('perfil:listar_perfiles'))

	context = {'form':form, 'perfil_id':perfil_id}
	return render(request, 'perfil/modificar_perfil.html', context)

@login_required
@permission_required('auth.delete_group')
def eliminar_perfil(request, perfil_id):
	perfil = Group.objects.get(pk=perfil_id)
	perfil.delete()
	return HttpResponseRedirect(reverse('perfil:listar_perfiles'))


@login_required
def listar_perfiles(request):
	lista_perfiles = Group.objects.all()
	context = {'lista_perfiles':lista_perfiles}
	return render(request, 'perfil/listar_perfiles.html', context)




