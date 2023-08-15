from django import forms
from .models import Profesor, Estudiante, Curso

class CursoFormulario(forms.ModelForm):
    class Meta:
       model = Curso
       fields = '__all__'
    
class ProfesorForm(forms.ModelForm):
   class Meta:
       model = Profesor
       fields = '__all__'
       
class EstudianteFormulario(forms.ModelForm):
    class Meta:
       model = Estudiante
       fields = '__all__'
       
class SearchForm(forms.Form):
    nombre = forms.CharField(required=False)