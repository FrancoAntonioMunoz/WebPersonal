from django.db import models

# Create your models here.
def image_project(isinstance, filename):
    return 'Project/image/' + filename

class Project(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True,verbose_name='Nombre Proyecto')
    descent=models.CharField(max_length=240,null=True,blank=True,verbose_name='Bajada')#bajada(Descripcion corta)
    description=models.TextField(max_length=500,null=True,blank=True,verbose_name='Descripción')
    image=models.ImageField(upload_to=image_project)
    state=models.CharField(max_length=240,default="Activo")
    created= models.DateTimeField(auto_now_add=True,verbose_name='Fecha Creación')
    updated= models.DateTimeField(auto_now=True,verbose_name='Fecha Actualización')

    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'
        ordering=['name']#con-name es alrevez el orden asc o descendente
    def _str_(self):
        return self.name
