from django.shortcuts import render

from .models import Discografia

def index(request):
    todos_los_proyectos =  Discografia.objects.all()
    return render(request, 'app/modulo.html', {'discografia': todos_los_proyectos})