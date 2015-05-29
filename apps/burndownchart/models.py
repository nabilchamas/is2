from django.db import models
from apps.proyecto.models import Proyecto

class BurndownchartDato(models.Model):

    burndown_estimado = models.IntegerField()
    burndown_actual = models.IntegerField()
    sprint_dias = models.IntegerField()
    proyecto = models.ForeignKey(Proyecto)
