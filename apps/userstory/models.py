from django.db import models
from apps.proyecto.models import Proyecto
from apps.flujo.models import Flujo, Actividad
from apps.sprint.models import Sprint

class UserStory(models.Model):
	ESTADOS = (
		('Todo', 'To do'),
		('Doing', 'Doing'),
		('Done', 'Done'),
		)

	nombre = models.CharField(max_length=200)
	proyecto = models.ForeignKey(Proyecto)
	sprint = models.ForeignKey(Sprint, null=True)
	flujo = models.ForeignKey(Flujo, null=True)
	actividad = models.ForeignKey(Actividad)
	estado = models.CharField(max_length=200, choices=ESTADOS)

	def __str__(self):
		return self.nombre






