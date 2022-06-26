from django.shortcuts import render
from .models import Familiares

# class Familiares(models.Model):
#     cedula = models.IntegerField()
#     nombre = models.CharField(max_length=30)
#     fecha_nacimiento = models.DateField()

def principal(request):

    familiar1 = Familiares(cedula=25554447,nombre='Miguelo',fecha_nacimiento='07/11/1999')
    familiar2 = Familiares(cedula=34446669,nombre='',fecha_nacimiento='04/11/1950')
    familiar3 = Familiares(cedula=53222247,nombre='Mercio',fecha_nacimiento='12/12/1932')

    lista_familiares = [familiar1, familiar2, familiar3]

    return render(request, 'index.html', {'home': lista_familiares})
