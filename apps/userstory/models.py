from django.db import models
from apps.proyecto.models import Proyecto
from apps.flujo.models import Flujo, Actividad
from apps.sprint.models import Sprint
from django.contrib.auth.models import User

class UserStory(models.Model):
	ESTADOS = (
		('Todo', 'To do'),
		('Doing', 'Doing'),
		('Done', 'Done'),
		)

	PRIORIDADES = (
		('Baja', 'Baja'),
		('Media', 'Media'),
		('Alta', 'Alta'),
		)

	nombre = models.CharField(max_length=200)
	proyecto = models.ForeignKey(Proyecto)
	sprint = models.ForeignKey(Sprint, null=True)
	flujo = models.ForeignKey(Flujo, null=True)
	actividad = models.ForeignKey(Actividad)
	desarrollador = models.ForeignKey(User, null=True)
	estado = models.CharField(max_length=200, choices=ESTADOS)
	prioridad = models.CharField(max_length=200, choices=PRIORIDADES, null=True)

	def __str__(self):
		return self.nombre






