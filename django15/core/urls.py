from django.conf.urls import url
from core.views import home, lista, novo, atualiza, deletar


urlpatterns = [
    url(r'^$', home),
    url(r'^lista-todos/$', lista, name='lista_todos'),
    url(r'^novo/$', novo),
    url(r'^atualizar/(?P<id>\d+)/$', atualiza, name='atualizar'),
    url(r'^deletar/(?P<id>\d+)/$', deletar, name='deletar'),
]
	
