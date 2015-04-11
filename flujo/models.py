from django.db import models

class Flujo(models.Model):
	nombre = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre

class Actividad(models.Model):
	nombre = models.CharField(max_length=200)
	flujo = models.ForeignKey(Flujo)

	def __str__(self):
		return self.nombre
