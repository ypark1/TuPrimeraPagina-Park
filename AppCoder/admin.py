from django.contrib import admin
from AppCoder import models


# Registramos los modelos


admin.site.register(models.Curso)
admin.site.register(models.Profesor)
admin.site.register(models.Estudiante)