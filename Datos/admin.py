from django.contrib import admin
from Datos.models import Datos

class DatosAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('name','state')
admin.site.register(Datos, DatosAdmin)

# Register your models here.
