from django.contrib import admin
from Project.models import Project

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('name','description')
admin.site.register(Project, ProjectAdmin)
# Register your models here.
