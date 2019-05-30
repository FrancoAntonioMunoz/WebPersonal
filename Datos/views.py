from django.shortcuts import render, HttpResponse
from Pag.models import Pag
from Datos.models import Datos
from Project.models import Project
# Create your views here.

def home(request,pag_id=None):
    try:
        pages= Pag.objects.get(pk=pag_id)
        datos= Datos.objects.get(pk=1)
    except:
        datos= Datos.objects.get(pk=1)
        pages= Pag.objects.get(name='Inicio')
    return render(request,"Datos/home.html",{'pages':pages,'datos':datos})
def about(request):
    datos= Datos.objects.get(pk=1)
    pages= Pag.objects.get(name='Acerca de')
    return render(request,'Datos/about.html/',{'pages':pages,'datos':datos})
def portfolio(request):
    datos= Datos.objects.get(pk=1)
    pages= Pag.objects.get(name='Portafolio')
    proyects = Project.objects.all()
    return render(request,'Datos/portfolio.html/',{'pages':pages,'proyects':proyects,'datos':datos})
def contact(request):
    datos= Datos.objects.get(pk=1)
    pages= Pag.objects.get(name='Conctacto') #estoy pasando directamente ya que en la bd contact es la pk=1
    return render(request,'Datos/contact.html/',{'pages':pages,'datos':datos})
def projectView(request,project_id):
    datos= Datos.objects.get(pk=1)
    proyect = Project.objects.get(pk=project_id)
    return render(request,"Datos/projectView.html",{'proyect':proyect,'datos':datos})     
