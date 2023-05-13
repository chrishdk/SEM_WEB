from django.shortcuts import render
from django.db import connection
import cx_Oracle
from .forms import ReporteForm



# Create your views here.

def login(request):
    return render(request,'app/login.html')

def inicio(request):
    return render(request,'app/inicio.html')

def formr(request):
    # data = {
    #     'empleado_id_empleado':listado_empleado(),
    # }
    # agregar_reporte(4,'kenny del futuro', 'asdf', 2)
    # if request.method == 'POST':
    #     id_reporte = request.POST.get('id_reporte')

    #     titulo = request.POST.get('titulo')
    #     descripcion = request.POST.get('descripcion')
    #     empleado_id_empleado = request.POST.get('empleado_id_empleado')
    #     salida = agregar_reporte(id_reporte,titulo,descripcion,empleado_id_empleado)
        
    #     if salida == 1:
    #         data['mensaje'] = 'Registro exitoso'
    #     else:
    #         data['mensaje'] = 'Registro fallido'

    # return render(request,'app/form_rep.html', data)
    return render(request,'app/form_rep.html')




def formempleado(request):
    return render(request,'app/form_emp.html')


def reporte(request):
        # print (listado_usuarios())

    data = {
        'reporte':listado_reporte()
    }

    return render(request,'app/reporte.html', data)




def usuarios(request):
    # print (listado_usuarios())
    data = {
        'usuarios':listado_usuarios()
    }
    # agregar_usuario(4,'kenny del futuro', 60, 'su casa')
    return render(request,'app/usuarios.html', data)





def empleado(request):
    # print (listado_usuarios())

    data = {
        'usuarios':listado_empleado()
    }
    # agregar_usuario(4,'kenny del futuro', 60, 'su casa')
    return render(request,'app/emp.html', data)











def listado_usuarios():
    django_cursor =connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_USUARIOS", [out_cur])
    lista =[]
    for fila in out_cur:
        lista.append(fila)
    
    return lista


def listado_empleado():
    django_cursor =connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_EMPLEADOS", [out_cur])
    lista =[]
    for fila in out_cur:
        lista.append(fila)
    
    return lista




def listado_reporte():
    django_cursor =connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_REPORTE", [out_cur])
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



def agregar_reporte(id_reporte, titulo,descripcion,empleado_id_empleado):
    django_cursor =connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("sp_ingresar_reporte", [id_reporte, titulo,descripcion,empleado_id_empleado])
    return salida.getvalue()


