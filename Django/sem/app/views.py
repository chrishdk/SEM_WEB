from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'app/login.html')

def inicio(request):
    return render(request,'app/inicio.html')

def reporte(request):
    return render(request,'app/reportes.html')