from django.db import models


class Familiares(models.Model):
    cedula = models.IntegerField()
    nombre = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()



