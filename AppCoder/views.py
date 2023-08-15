from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from django.http import HttpResponse
from .models import Curso, Estudiante, Profesor, Entregable
from .forms import CursoFormulario, ProfesorForm, SearchForm, EstudianteFormulario

def padre(request):
    return render(request, 'padre.html')

#def index(request):
    #return render(request, 'index.html')

def inicio(request):
    return render(request, 'inicio.html')


def crear_curso(request):
      if request.method == "POST":
            form = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(form)
            if form.is_valid:
                form.save()
                return redirect('Inicio') # vuela al padre o a donde quieran
      else:
            form = CursoFormulario() # Formulario vacio para construir el html
      return render(request, 'curso_form.html', {"form": form})
        
def crear_profesor(request):
      if request.method == "POST":
            form = ProfesorForm(request.POST) # Aqui me llega la informacion del html
            print(form)
            if form.is_valid:
                form.save()
                return redirect('Inicio') # vuela al padre o a donde quieran
      else:
            form = ProfesorForm() # Formulario vacio para construir el html
      return render(request, 'profesor_form.html', {"form": form})

def crear_estudiante(request):
      if request.method == "POST":
            form = EstudianteFormulario(request.POST) # Aqui me llega la informacion del html
            print(form)
            if form.is_valid:
                form.save()
                return redirect('Inicio') # vuela al padre o a donde quieran
      else:
            form = EstudianteFormulario() # Formulario vacio para construir el html
      return render(request, 'estudiantes_form.html', {"form": form})

def buscar_cursos_por_nombre(request):
    cursos = []
    form = SearchForm(request.GET) 
    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        if nombre:
            cursos = Curso.objects.filter(nombre__icontains=nombre)
    return render(request, 'buscar_cursos.html', {'form': form, 'cursos': cursos})
    

  
#def cursoFormulario(request):
 #   if request.method == 'POST':
  #      mi_formulario = cursoFormulario(request.POST)  # Aqui me llega la informacion del html
        
   #     print(mi_formulario)
        
    #    if mi_formulario.is_valid():
     #       informacion = mi_formulario.cleaned_data
      #      curso = Curso(informacion["curso"], informacion["camada"])
       #     curso.save()
        #    return render(request, "inicio.html")
    #else:
     #   mi_formulariom = cursoFormulario()
      #  return render(request, 'cursos_formulario.html', {'mi_formulario': mi_formulario})  
    
#def EstudianteForm(request):
 #   if request.method == 'POST':
  #      mi_form = EstudianteForm(request.POST)  # Aqui me llega la informacion del html
   ##    if mi_form.is_valid():
     #       informacion = mi_form.cleaned_data
      #      estudiante = Estudiante(informacion["nombre"], informacion["email"])
       #     estudiante.save()
        #    return render(request, "inicio.html")
    #else:
     #   mi_form = EstudianteForm()
      #  return render(request, 'estudiantes_formulario.html', {'form': mi_form})  
   

def estudiantes(request):
    return render(request, 'estudiantes.html')


def entregables(request):
    return render(request, 'entregables.html')