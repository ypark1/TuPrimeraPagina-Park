from django.urls import path
from . import views

urlpatterns = [
    #path('index/', views.index, name='index'),
    path('padre/', views.padre, name='padre'),
    #path('', views.inicio, name='Inicio'),
    #path('cursos/', views.cursos, name='Cursos'),
    #path('profesores/', views.profesores, name='Profesores'),
    path('estudiantes/', views.crear_estudiante, name='Estudiantes'),
    #path('estudiantes_formulario/', views.estudiantes_formulario, name='estudiantes_formulario'),
    path('cursos/', views.crear_curso, name='Cursos'),
    ##path('buscar/', views.buscar, name='buscar'),
    path('profesores', views.crear_profesor, name='Profesores'),
    path('', views.buscar_cursos_por_nombre, name='Inicio'),
]
