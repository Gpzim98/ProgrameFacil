from django.conf.urls import url, include
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos, 
    lista_movrotativos,
    lista_mensalista,
    lista_movmensalista
)

urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    url(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    url(r'^mov-rot/$', lista_movrotativos, 
        name='core_lista_movrotativos'),
    url(r'^mensalistas/$', lista_mensalista, 
        name='core_lista_mensalista'),
    url(r'^mov-mensal/$', lista_movmensalista, 
        name='core_lista_movmensalista'),
]
