from base.forms import CadastroForm
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def cadastro(resquest):
    sucesso = False
    if resquest.method == 'GET':
        form = CadastroForm()
    else:
        form = CadastroForm(resquest.POST)
        if form.is_valid():
            sucesso = True
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render (resquest, 'cadastro.html')