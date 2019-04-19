from django.contrib import admin
from Pag.models import Pag

class PagAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('name','headers')
admin.site.register(Pag, PagAdmin)
# Register your models here.
