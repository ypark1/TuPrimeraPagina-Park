from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from .models import Curso, Estudiante, Profesor, Entregable
from .forms import PostForm, BuscarForm


def cursos(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'cursos.html', {'form': form})

def profesores(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'profesores.html', {'form': form})
    



# Create your views here.


