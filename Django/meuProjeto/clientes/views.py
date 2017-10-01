from django.shortcuts import render
from django.http import HttpResponse


def clientes(request):
    return HttpResponse('Maria, Jose, Joao')

def cliente_detalhe(request, id):
    return HttpResponse(id)

def cliente_por_nome(request, nome):
    return HttpResponse('Ola %s' % nome)
