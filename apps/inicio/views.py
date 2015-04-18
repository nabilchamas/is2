from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required

def autenticar(request):
	logout(request)
	if request.method=='POST':

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('inicio:menu'))
		# else:
		# 	return HttpResponseRedirect('/account/invalid')
	# else:
		#context = {}
		#context.update(csrf(request))

	return render(request, 'inicio/autenticar.html')

@login_required
def menu(request):
	return render(request, 'inicio/menu.html')


def salir(request):
	logout(request)
	return render(request, 'inicio/autenticar.html')
