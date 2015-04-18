from django.db import models
from apps.proyecto.models import Proyecto


class Sprint(models.Model):
	ESTADOS = (
		('Activo', 'Activo'),
		('No activo', 'No activo'),
		)


	nombre = models.CharField(max_length=200)
	proyecto = models.ForeignKey(Proyecto)
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()
	estado = models.CharField(max_length=15, choices=ESTADOS)
	descripcion = models.TextField(max_length=200)

	def __str__(self):
		return self.nombre



