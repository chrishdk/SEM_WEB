from django.shortcuts import render
from django.db import connection
import cx_Oracle
from .forms import ReporteForm
from django.contrib.auth.decorators import login_required
import base64



# Create your views here.
@login_required(login_url='/accounts/login')
def inicio(request):
    return render(request,'app/index.html')



# def inicio(request):
#     return render(request,'app/inicio.html')
@login_required(login_url='/accounts/login')
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



@login_required(login_url='/accounts/login')
def formempleado(request):
    return render(request,'app/form_emp.html')



@login_required(login_url='/accounts/login')
def reporte(request):

    datos_reportes = listar_reporte()

    arreglo = []

    for i in datos_reportes:
            data ={
                'data': i,
                'imagen': str(base64.b64encode(i[9].read()),'utf-8')
        }
            arreglo.append(data)

    
    data = {
        'reporte':arreglo
    }

    return render(request,'app/reporte.html', data)



@login_required(login_url='/accounts/login')
def usuarios(request):
    data = {
        
    }

    return render(request,'app/usuarios.html', data)




@login_required(login_url='/accounts/login')
def empleado(request):
    data = {
        'empleados':sp_listar_empleado()
    }

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

# listo
def sp_listar_empleado():
    django_cursor =connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_empleado", [out_cur])
    lista =[]
    for fila in out_cur:
        lista.append(fila)
    
    return lista



# listo
def listar_reporte():
    django_cursor =connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_reporte", [out_cur])
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


