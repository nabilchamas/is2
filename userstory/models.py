from django.db import models
from proyecto.models import Proyecto
from flujo.models import Flujo, Actividad

class UserStory(models.Model):
	ESTADOS = (
		('Todo', 'To do'),
		('Doing', 'Doing'),
		('Done', 'Done'),
		)

	nombre = models.CharField(max_length=200)
	proyecto = models.ForeignKey(Proyecto)
	flujo = models.ForeignKey(Flujo, null=True)
	actividad = models.ForeignKey(Actividad)
	estado = models.CharField(max_length=200, choices=ESTADOS)

	def __str__(self):
		return self.nombre






