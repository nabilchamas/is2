from django.db import models

class BurndownchartDato(models.Model):

    burndown_estimado = models.IntegerField()
    burndown_actual = models.IntegerField()
    sprint_dias = models.IntegerField()
