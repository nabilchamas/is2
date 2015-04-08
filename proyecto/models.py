from django.db import models

class Proyecto(models.Model):
	nombre = models.CharField(max_length=200)
	codigo = models.IntegerField(default=0)
	descripcion = models.CharField(max_length=200)
	cliente = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre