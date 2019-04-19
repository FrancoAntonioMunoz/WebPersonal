from django.db import models

def image_Pag(isinstance, filename):
    return 'Pag/image/' + filename

class Pag(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True,verbose_name='Titulo')
    headers=models.CharField(max_length=240,null=True,blank=True,verbose_name='Encabezado')
    content=models.TextField(max_length=500,null=True,blank=True,verbose_name='Contenido')
    image=models.ImageField(upload_to=image_Pag,null=True,blank=True)
    state=models.CharField(max_length=240,default="Activo")
    created= models.DateTimeField(auto_now_add=True,verbose_name='Fecha Creación')
    updated= models.DateTimeField(auto_now=True,verbose_name='Fecha Actualización')

    class Meta:
        verbose_name='Pagina'
        verbose_name_plural='Paginas'
        ordering=['name']#con-name es alrevez el orden asc o descendente
    def _str_(self):
        return self.name
