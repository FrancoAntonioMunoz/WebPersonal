from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,'Datos/home.html/')
def about(request):
    return render(request,'Datos/about.html/')
def portfolio(request):
    return render(request,'Datos/portfolio.html/')

def contact(request):
    return render(request,'Datos/contact.html/')
