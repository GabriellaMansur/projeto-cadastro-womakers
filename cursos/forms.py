from django import forms
from cursos.models import Cursos

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'nivel', 'carga_horaria', 'data_do_curso', 'descricao']