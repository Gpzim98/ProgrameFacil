from django.contrib import admin
from .models import Empregado, Telefone, CPF, Departamento


admin.site.register(Empregado)
admin.site.register(Telefone)
admin.site.register(Departamento)
admin.site.register(CPF)