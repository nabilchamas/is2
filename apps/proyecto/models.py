from django.db import models

class Proyecto(models.Model):
	nombre = models.CharField(max_length=200)
	codigo = models.IntegerField(default=0)
	fecha_inicio = models.DateField(null=True)
	fecha_fin = models.DateField(null=True)
	cliente = models.CharField(max_length=200)
	descripcion = models.TextField(max_length=200)

	def __str__(self):
		return self.nombre