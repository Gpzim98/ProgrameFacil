from django.conf.urls import url
from django.contrib import admin
from .views import home

urlpatterns = [
    url(r'^home/', home, name='core_home'),
    url(r'^admin/', admin.site.urls),
]
