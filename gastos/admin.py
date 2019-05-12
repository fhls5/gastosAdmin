from django.contrib import admin

# Register your models here.
from .models import Gastos
from .models import Categorias

#admin.site.register(Gastos)
class GastosAdmin(admin.ModelAdmin):
    fields = ['monto', 'categoria']

admin.site.register(Gastos, GastosAdmin)

class CategoriasAdmin(admin.ModelAdmin):
    fields = ['nombre']

admin.site.register(Categorias, CategoriasAdmin)