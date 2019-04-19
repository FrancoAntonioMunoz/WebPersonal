from django.db import models


def image_Datos1(isinstance, filename):
    return 'Datos/image/' + filename
def image_Datos2(isinstance, filename):
    return 'Datos/image/' + filename
def image_Datos3(isinstance, filename):
    return 'Datos/image/' + filename

class Datos(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True,verbose_name='Nombre Personal')
    descent=models.CharField(max_length=240,null=True,blank=True,verbose_name='Url')
    image1=models.ImageField(upload_to=image_Datos1)
    descent1=models.CharField(max_length=240,null=True,blank=True,verbose_name='Url')
    image2=models.ImageField(upload_to=image_Datos2)
    descent2=models.CharField(max_length=240,null=True,blank=True,verbose_name='Url')
    image3=models.ImageField(upload_to=image_Datos3)
    state=models.CharField(max_length=240,default="Activo")
    created= models.DateTimeField(auto_now_add=True,verbose_name='Fecha Creación')
    updated= models.DateTimeField(auto_now=True,verbose_name='Fecha Actualización')

    class Meta:
        verbose_name='Dato y rede social'
        verbose_name_plural='Datos y redes sociales'
        ordering=['name']#con-name es alrevez el orden asc o descendente
    def _str_(self):
        return self.name
# Create your models here.

