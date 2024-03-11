from base.forms import CadastroForm
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def cadastro(resquest):
    if resquest.method == 'GET':
        form = CadastroForm()
    return render (resquest, 'cadastro.html')