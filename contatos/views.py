import imp
from django.shortcuts import render
from .models import Contato

# Create your views here.

def index(request):
    contatos = Contato.objects.all() #selecionando os dados da minha base de dados. 
    return render(request, 'contatos/index.html', {'contatos': contatos})


