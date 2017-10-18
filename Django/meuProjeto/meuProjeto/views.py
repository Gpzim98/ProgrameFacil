from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    sexo = 'm'
    nome = 'Alfredo'
    lista = [
        {'nome': 'Pedro', 'sexo': 'm'},
        {'nome': 'Maria', 'sexo': 'f'},
        {'nome': 'Joaquina', 'sexo': 'f'},
        {'nome': 'Joao', 'sexo': 'm'},
    ]
    data = {'lista': lista, 'sexo': sexo, 'nome': nome }
    return render(request, 'index.html', data)
