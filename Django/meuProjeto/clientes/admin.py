from django.contrib import admin
from .models import Empregado, Telefone, CPF, Departamento

# fields
# list_display
# list_filter
# search_fields

class EmpregadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco', 'email')
    list_filter = ('departamentos', )
    search_fields = ('id', 'nome', 'email', 'departamentos__nome')


admin.site.register(Empregado, EmpregadoAdmin)
admin.site.register(Telefone)
admin.site.register(Departamento)
admin.site.register(CPF)