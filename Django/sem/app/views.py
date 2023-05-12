from django.shortcuts import render
from django.db import connection
import cx_Oracle

# Create your views here.

def login(request):
    return render(request,'app/login.html')

def inicio(request):
    return render(request,'app/inicio.html')

def reporte(request):
    return render(request,'app/reportes.html')

def usuarios(request):
    print (listado_usuarios())

    data = {
        'usuarios':listado_usuarios()
    }
    agregar_usuario(4,'kenny del futuro', 60, 'su casa')
    return render(request,'app/usuarios.html', data)

def listado_usuarios():
    django_cursor =connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_USUARIOS", [out_cur])
    lista =[]
    for fila in out_cur:
        lista.append(fila)
    
    return lista




def agregar_usuario(id, nombre, edad, direccion):
    django_cursor =connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_AGREGAR_USUARIO", [id, nombre, edad, direccion, salida])
    return salida.getvalue()
