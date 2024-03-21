from django.shortcuts import render
from cursos.forms import CursoForm
# Create your views here.

def criar_curso(request):
    form = CursoForm(request.POST or None)
    sycesso = False
    if form.isvalid():
        form.save()
        sucesso = True
    contexto = {
        'form': form,
        'sucesso': sucesso,
    }
    return