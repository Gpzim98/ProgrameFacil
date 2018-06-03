"""meuProjeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import home
from clientes.views import clientes, cliente_detalhe, cliente_por_nome
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', home),
    url(r'^clientes$', clientes),
    url(r'^cliente/(?P<id>\d+)$', cliente_detalhe),
    url(r'^cliente/(?P<nome>\w+)$', cliente_por_nome),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

