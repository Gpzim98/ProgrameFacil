from django.http import HttpResponse


def home(request):
    return HttpResponse('Ola Mundo')

def clientes(request):
    return HttpResponse('Maria, Jose, Joao')

def cliente_detalhe(request, id):
    return HttpResponse(id)

def cliente_por_nome(request, nome):
    return HttpResponse('Ola %s' % nome)
