from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')


def contato(request):
    return render(request, 'website/contato.html')


def servicos(request):
    return render(request, 'website/servicos.html')