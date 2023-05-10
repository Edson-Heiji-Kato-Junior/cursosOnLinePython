from django.shortcuts import render
from .models import Produto

def index(request):
 #   produtos = Produto.objects.all()

    context = {'curso'  : 'Programação Web com Django Framework',
               'outros' : 'Django é Topp!!!!'
               }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')
