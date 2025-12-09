from msilib.schema import ListView

from django.shortcuts import render
from django.views import View


# Create your views here.
# Vista principal de la web
def indexVacaciones(request):
    context = {'titulo_ventana': 'Vacaciones', 'titulo_pagina': 'Home'}
    return render(request, 'indexVacaciones.html', context)
