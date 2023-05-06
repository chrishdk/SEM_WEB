from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/login.html')

def inicio(request):
    return render(request, 'app/inicio.html')