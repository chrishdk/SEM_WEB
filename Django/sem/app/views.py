from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
import cx_Oracle
from .forms import EmpresaForm,ReporteForm
from django.contrib.auth.decorators import login_required
from PIL import Image
from io import BytesIO
import base64
from django.contrib import messages


# Inicio
@login_required(login_url='/accounts/login')
def inicio(request):
    reporte_mes = contar_reportes_mes_actual()
    reporte_dia = contar_reportes_dia_actual()
    reporte_no_asignados = contar_reportes_no_asignados()

    data = {
        'reporte_mes': reporte_mes,
        'reporte_dia': reporte_dia,
        'reporte_no_asignados': reporte_no_asignados,
    }

    return render(request, 'app/index.html', data)


def contar_reportes_mes_actual():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    cantidad = cursor.var(int)
    cursor.callproc('contar_reportes_mes_actual', [cantidad])

    return cantidad.getvalue()


def contar_reportes_dia_actual():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    cantidad = cursor.var(int)
    cursor.callproc('contar_reportes_dia_actual', [cantidad])

    return cantidad.getvalue()


def contar_reportes_no_asignados():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    cantidad = cursor.var(int)
    cursor.callproc('contar_reportes_no_asignados', [cantidad])

    return cantidad.getvalue()



@login_required(login_url='/accounts/login')
def empleado(request):
    datos_empleado = sp_listar_empleado()
    arreglo = []
    for i in datos_empleado:
        imagen = i[9]
        if imagen is not None:
            imagen_base64 = str(base64.b64encode(imagen.read()), 'utf-8')
        else:
            imagen_base64 = None

        data = {
            'data': i,
            'imagen': imagen_base64
        }
        arreglo.append(data)

    data = {
        'empleado': arreglo,
        'cargo': listado_cargo,
        'sucursal': listado_sucursal
    }


    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'nuevo':
            rut = request.POST.get('rut')
            dv = request.POST.get('dv')
            p_nombre = request.POST.get('p_nombre')
            s_nombre = request.POST.get('s_nombre')
            p_apellido = request.POST.get('p_apellido')
            s_apellido = request.POST.get('s_apellido')
            email = request.POST.get('email')
            cargo = request.POST.get('cargo')
            sucursal = request.POST.get('sucursal')
            imagen = request.FILES.get('imagen')

            if imagen is not None:
                image = Image.open(imagen)
                max_size = (500, 500)
                image.thumbnail(max_size)

                image_buffer = BytesIO()
                image.save(image_buffer, format='JPEG')
                image_data = image_buffer.getvalue()
                salida = SP_AGREGAR_EMPLEADO(rut, dv, p_nombre, s_nombre, p_apellido, s_apellido, email, cargo, sucursal, image_data)
                print(salida, 'salida')
                messages.success(request, '¡El mensaje se muestra correctamente!')
                return redirect('empleado')
            else:
                image_data = None
                salida = SP_AGREGAR_EMPLEADO(rut, dv, p_nombre, s_nombre, p_apellido, s_apellido, email, cargo, sucursal, image_data)
                print(salida, 'salida')
                messages.warning(request, '¡ERROR!')
                return redirect('empleado')

            
        elif accion == 'modificar':
            rut = request.POST.get('rut')
            dv = request.POST.get('dv')
            p_nombre = request.POST.get('p_nombre')
            s_nombre = request.POST.get('s_nombre')
            p_apellido = request.POST.get('p_apellido')
            s_apellido = request.POST.get('s_apellido')
            email = request.POST.get('email')
            cargo = request.POST.get('cargo')
            sucursal = request.POST.get('sucursal')
            imagen = request.FILES.get('imagen')

             # Redimensionar imagen
            if imagen is not None:
                image = Image.open(imagen)
                max_size = (500, 500)
                image.thumbnail(max_size)

                image_buffer = BytesIO()
                image.save(image_buffer, format='JPEG')
                image_data = image_buffer.getvalue()

                salida = SP_MODIFICAR_EMPLEADO(rut, dv, p_nombre, s_nombre, p_apellido, s_apellido, email, cargo, sucursal, image_data)
                print(salida, 'salida')
                if salida == 1:
                    messages.success(request, 'Modificacion exitosa de empleado')
                    return redirect('empleado')
                else:
                    messages.warning(request, 'Error al ingresar datos de empleado')
                    return redirect('empleado')

            else:
                image_data = None
                salida = SP_MODIFICAR_EMPLEADO(rut, dv, p_nombre, s_nombre, p_apellido, s_apellido, email, cargo, sucursal, image_data)
                print(salida, 'salida')
                if salida == 1:
                    
                    messages.success(request, 'Modificacion exitosa de empleado')
                    return redirect('empleado')
                else:
                    messages.warning(request, 'Error al ingresar datos de empleado')
                    return redirect('empleado')

    return render(request, 'app/emp.html', data)

def SP_AGREGAR_EMPLEADO(rut, dv, p_nombre, s_nombre, p_apellido, s_apellido, email, cargo, sucursal, imagen):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    if imagen is not None:
        cursor.callproc("SP_AGREGAR_EMPLEADO_IMG", [rut, dv, p_nombre, s_nombre, p_apellido, s_apellido, email, cargo, sucursal, imagen, salida])
        print(salida.getvalue(), 'salida')
    else:
        cursor.callproc("SP_AGREGAR_EMPLEADO", [rut, dv, p_nombre, s_nombre, p_apellido, s_apellido, email, cargo, sucursal, salida])
        print(salida.getvalue(), 'salida')
    
    return salida.getvalue()


def SP_MODIFICAR_EMPLEADO(rut, dv, p_nombre, s_nombre, p_apellido, s_apellido, email, cargo, sucursal, imagen):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    if imagen is not None:
        cursor.callproc("SP_MODIFICAR_EMPLEADO_IMG", [rut, dv, p_nombre, s_nombre, p_apellido, s_apellido, email, cargo, sucursal, imagen,salida])
    else:
        cursor.callproc("SP_MODIFICAR_EMPLEADO", [rut, dv, p_nombre, s_nombre, p_apellido, s_apellido, email, cargo, sucursal,salida])
    return salida.getvalue()


def sp_listar_empleado():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_EMPLEADO", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista






@login_required(login_url='/accounts/login')
def reporte(request):
    datos_reportes = listar_reporte()
    arreglo = []

    for i in datos_reportes:
        imagen = i[10]
        if imagen is not None:
            imagen_base64 = str(base64.b64encode(imagen.read()), 'utf-8')
        else:
            imagen_base64 = None

        data = {
            'data': i,
            'imagen': imagen_base64
        }
        arreglo.append(data)

    data = {
        'reporte': arreglo,
        'usuarios': SP_LISTAR_USUARIO(),
        'prioridad': SP_LISTAR_PRIORIDAD(),
        'piso': SP_LISTAR_PISO(),
        'sector': SP_LISTAR_SECTOR(),
        'estado': SP_LISTAR_ESTADO_R(),
        'sucursal': listado_sucursal(),
        }
    
    if request.method == 'POST':
        accion = request.POST.get('accion')
        if accion == 'nuevo':
            id_reporte = request.POST.get('id_reporte')
            titulo = request.POST.get('titulo')
            descripcion = request.POST.get('descripcion')
            fecha_ingreso = request.POST.get('fecha_ingreso')
            usuario_usuario = request.POST.get('usuario_usuario')
            prioridad_id_prioridad = request.POST.get('prioridad_id_prioridad')
            piso_id_piso = request.POST.get('piso_id_piso')
            sector_id_sector = request.POST.get('sector_id_sector')
            estado_r_id_estado = request.POST.get('estado_r_id_estado')
            sucursal_id_sucursal = request.POST.get('sucursal_id_sucursal')
            imagen = request.FILES.get('imagen')
            asignado = request.POST.get('asignado')

            if imagen is not None:
                image = Image.open(imagen)
                max_size = (500, 500)
                image.thumbnail(max_size)

                image_buffer = BytesIO()
                image.save(image_buffer, format='JPEG')
                image_data = image_buffer.getvalue()

                salida = SP_AGREGAR_REPORTE(
                    titulo,
                    descripcion,
                    fecha_ingreso,
                    usuario_usuario,
                    prioridad_id_prioridad,
                    piso_id_piso,
                    sector_id_sector,
                    estado_r_id_estado,
                    sucursal_id_sucursal,
                    image_data)
                return redirect('reporte')
            else:
                image_data = None
                salida = SP_AGREGAR_REPORTE(
                    titulo,
                    descripcion,
                    fecha_ingreso,
                    usuario_usuario,
                    prioridad_id_prioridad,
                    piso_id_piso,
                    sector_id_sector,
                    estado_r_id_estado,
                    sucursal_id_sucursal,
                    image_data)
                return redirect('reporte')

        elif accion == 'asignar':
            id_reporte = request.POST.get('id_reporte')
            asignado = request.POST.get('asignado')

            salida = SP_ASIGNAR_REPORTE(id_reporte,asignado)

            messages.success(request, '¡El reporte se agregó correctamente!')
            return redirect('reporte')
    return render(request, 'app/reporte.html', data)


def SP_AGREGAR_REPORTE(titulo,descripcion,fecha_ingreso,usuario_usuario,prioridad_id_prioridad,piso_id_piso,sector_id_sector,estado_r_id_estado,sucursal_id_sucursal,imagen):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    if imagen is not None:
        cursor.callproc("SP_AGREGAR_REPORTE_IMG", [titulo,descripcion,fecha_ingreso,usuario_usuario,prioridad_id_prioridad,piso_id_piso,sector_id_sector,estado_r_id_estado,sucursal_id_sucursal,imagen])
        print("asdf:", titulo)
    else:
        cursor.callproc("SP_AGREGAR_REPORTE",[titulo,descripcion,fecha_ingreso,usuario_usuario,prioridad_id_prioridad,piso_id_piso,sector_id_sector,estado_r_id_estado,sucursal_id_sucursal])
        print("asdfsin:", titulo)
    return salida.getvalue()


def SP_MODIFICAR_reporte(id_repote,
                         titulo,
                         descripcion,
                         usuario_usuario,
                         prioridad_id_prioridad,
                         piso_id_piso,
                         sector_id_sector,
                         estado_r_id_estado,
                         sucursal_id_sucursal,
                         imagen,
                         asignado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_MODIFICAR_reporte", [id_repote,
                                             titulo,
                                             descripcion,
                                             usuario_usuario,
                                             prioridad_id_prioridad,
                                             piso_id_piso,
                                             sector_id_sector,
                                             estado_r_id_estado,
                                             sucursal_id_sucursal,
                                             imagen,
                                             asignado])
    return salida.getvalue()


def SP_ASIGNAR_REPORTE(id_reporte,asignado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_ASIGNAR_REPORTE", [id_reporte,asignado])
    return salida.getvalue()


def listar_reporte():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_reporte", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista




@login_required(login_url='/accounts/login')
def solicitud(request):
    data_solicitud = SP_LISTAR_SOLICITUD()

    data = {
        'solicitud': data_solicitud,
        'usuarios' : SP_LISTAR_USUARIO(),
        'sucursal' : listado_sucursal(),
        'insumos'  : SP_LISTAR_INSUMO(),
    }
    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'nuevo':
            solicitud = request.POST.get('solicitud')
            sucursal = request.POST.get('sucursal')
            solicitado = request.POST.get('solicitado')
            
            salida = SP_AGREGAR_SOLICITUD(solicitud, sucursal, solicitado)

            return redirect('solicitud')
            
        elif accion == 'estado':
            ID_SOLICITUD = request.POST.get('ID_SOLICITUD')
            ESTADO_S_ID_ESTADO_SOLICITUD = request.POST.get('ESTADO_S_ID_ESTADO_SOLICITUD')

            salida = SP_MODIFICAR_SOLICITUD_ESTADO(ID_SOLICITUD,ESTADO_S_ID_ESTADO_SOLICITUD)
            return redirect('solicitud')

    return render(request, 'app/solicitud.html', data)


def SP_MODIFICAR_SOLICITUD_ESTADO(ID_SOLICITUD,ESTADO_S_ID_ESTADO_SOLICITUD):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_MODIFICAR_SOLICITUD_ESTADO", [ID_SOLICITUD,ESTADO_S_ID_ESTADO_SOLICITUD])
    return salida.getvalue()


def SP_LISTAR_SOLICITUD():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_SOLICITUD", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def SP_LISTAR_SOLICITUD():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_SOLICITUD", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def SP_AGREGAR_SOLICITUD(solicitud,sucursal,solicitado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_AGREGAR_SOLICITUD", [solicitud,sucursal,solicitado,salida])
    return salida.getvalue()






@login_required(login_url='/accounts/login')
def insumo(request):
    data_insumos = SP_LISTAR_INSUMO()

    data = {
         'insumos': data_insumos,
         'sucursal': listado_sucursal()
     }
    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'nuevo':
            insumo = request.POST.get('insumo')
            stock = request.POST.get('stock')
            color = request.POST.get('color')
            sucursal = request.POST.get('sucursal')
            
            salida = SP_AGREGAR_INSUMO(insumo,stock,color,sucursal)
            if salida == 1:
                messages.success(request, 'Ingreso exitoso de insumo')
                return redirect('insumo')
            else:
                messages.warning(request, 'Ingreso FALLIDO de insumo')
            
            
        elif accion == 'modificar':
            id_insumo = request.POST.get('id_insumo')
            insumo = request.POST.get('insumo')
            stock = request.POST.get('stock')
            color = request.POST.get('color')
            sucursal = request.POST.get('sucursal')

            salida = SP_MODIFICAR_INSUMO(id_insumo,insumo,stock,color,sucursal)
            if salida == 1:
                messages.success(request, 'Modificacion exitosa de insumo')
                return redirect('insumo')
            else:
                messages.warning(request, 'Modificacion FALLIDA de insumo')
            
        
        elif accion == 'add':
            id_insumo = request.POST.get('id_insumo')
            addstock = request.POST.get('addstock')

            salida = SP_MODIFICAR_INSUMO_SUMAR(id_insumo,addstock)
            if salida == 1:
                messages.success(request, 'Modificacion exitosa de Stock')
                return redirect('insumo')
            else:
                messages.warning(request, 'Modificacion FALLIDA de Stock')
            

    return render(request, 'app/insumo.html',data)


def SP_LISTAR_INSUMO():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("SP_LISTAR_INSUMO", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def SP_AGREGAR_INSUMO(insumo,stock,color,sucursal):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_AGREGAR_INSUMO", [insumo,stock,color,sucursal,salida])
    return salida.getvalue()


def SP_MODIFICAR_INSUMO(id_insumo,insumo,stock,color,sucursal):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_MODIFICAR_INSUMO", [id_insumo,insumo,stock,color,sucursal,salida])
    return salida.getvalue()


def SP_MODIFICAR_INSUMO_SUMAR(id_insumo,addstock):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_MODIFICAR_INSUMO_SUMAR", [id_insumo,addstock,salida])
    return salida.getvalue()




@login_required(login_url='/accounts/login')
def usuarios(request):
    data_usuarios = SP_LISTAR_USUARIO()

    data = {
        'usuarios': data_usuarios
    }

    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'nuevo':
            

            return redirect('usuarios')
            
        elif accion == 'estado':
            usuario = request.POST.get('usuario')
            estado_u_id_estado_u = request.POST.get('estado_u_id_estado_u')

            salida = SP_MODIFICAR_USUARIO_ESTADO(usuario,estado_u_id_estado_u)
            

            return redirect('usuarios')
        
    return render(request, 'app/usuarios.html', data)


def SP_MODIFICAR_USUARIO_ESTADO(usuario,estado_u_id_estado_u):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_MODIFICAR_USUARIO_ESTADO", [usuario,estado_u_id_estado_u])
    return salida.getvalue()


def SP_LISTAR_USUARIO():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_USUARIO", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def SP_MODIFICAR_USUARIO(usuario, contrasena, empleado_rut, estado_u_id_estado_u):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_MODIFICAR_USUARIO", [usuario,
                                             contrasena,
                                             empleado_rut,
                                             estado_u_id_estado_u])
    return salida.getvalue()


@login_required(login_url='/accounts/login')
def historial(request):
    data_historial = SP_LISTAR_HISTORIAL()

    data = {
        'historial': data_historial,
    }
    return render(request, 'app/historial.html', data)


def SP_LISTAR_HISTORIAL():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_HISTORIAL", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista






def listado_sucursal():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_sucursal", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def listado_cargo():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_cargo", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista





def SP_LISTAR_PRIORIDAD():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PRIORIDAD", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def SP_LISTAR_PISO():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PISO", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def SP_LISTAR_SECTOR():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_SECTOR", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def SP_LISTAR_ESTADO_R():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_ESTADO_R", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista








@login_required(login_url='/accounts/login')
def prueba(request):
    datos_empleado = sp_listar_empleado()
    arreglo = []

    for i in datos_empleado:
        imagen = i[9]
        if imagen is not None:
            imagen_base64 = str(base64.b64encode(imagen.read()), 'utf-8')
        else:
            imagen_base64 = None

        data = {
            'data': i,
            'imagen': imagen_base64
        }
        arreglo.append(data)

    data = {
        'empleado': arreglo,
        'cargo': listado_cargo,
        'sucursal': listado_sucursal
    }


    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'nuevo':
            rut = request.POST.get('rut')
            dv = request.POST.get('dv')
            p_nombre = request.POST.get('p_nombre')
            s_nombre = request.POST.get('s_nombre')
            p_apellido = request.POST.get('p_apellido')
            s_apellido = request.POST.get('s_apellido')
            email = request.POST.get('email')
            cargo = request.POST.get('cargo')
            sucursal = request.POST.get('sucursal')
            imagen = request.FILES.get('imagen')

            if imagen is not None:
                image = Image.open(imagen)
                max_size = (500, 500)
                image.thumbnail(max_size)

                image_buffer = BytesIO()
                image.save(image_buffer, format='JPEG')
                image_data = image_buffer.getvalue()
                salida = SP_AGREGAR_EMPLEADO(rut, dv, p_nombre, s_nombre, p_apellido, s_apellido, email, cargo, sucursal, image_data)
                print(salida, 'salida')
                messages.success(request, '¡El mensaje se muestra correctamente!')
                return redirect('prueba')
            else:
                image_data = None
                salida = SP_AGREGAR_EMPLEADO(rut, dv, p_nombre, s_nombre, p_apellido, s_apellido, email, cargo, sucursal, image_data)
                print(salida, 'salida')
                messages.warning(request, '¡ERROR!')
                return redirect('prueba')

            
        elif accion == 'modificar':
            rut = request.POST.get('rut')
            dv = request.POST.get('dv')
            p_nombre = request.POST.get('p_nombre')
            s_nombre = request.POST.get('s_nombre')
            p_apellido = request.POST.get('p_apellido')
            s_apellido = request.POST.get('s_apellido')
            email = request.POST.get('email')
            cargo = request.POST.get('cargo')
            sucursal = request.POST.get('sucursal')
            imagen = request.FILES.get('imagen')

             # Redimensionar imagen
            if imagen is not None:
                image = Image.open(imagen)
                max_size = (500, 500)
                image.thumbnail(max_size)

                image_buffer = BytesIO()
                image.save(image_buffer, format='JPEG')
                image_data = image_buffer.getvalue()

                salida = SP_MODIFICAR_EMPLEADO(rut, dv, p_nombre, s_nombre, p_apellido, s_apellido, email, cargo, sucursal, image_data)
                print(salida, 'salida')
                if salida == 1:
                    messages.success(request, 'Modificacion exitosa de empleado')
                    return redirect('prueba')
                else:
                    messages.warning(request, 'Error al ingresar datos de empleado')
                    return redirect('prueba')

            else:
                image_data = None
                salida = SP_MODIFICAR_EMPLEADO(rut, dv, p_nombre, s_nombre, p_apellido, s_apellido, email, cargo, sucursal, image_data)
                print(salida, 'salida')
                if salida == 1:
                    
                    messages.success(request, 'Modificacion exitosa de empleado')
                    return redirect('prueba')
                else:
                    messages.warning(request, 'Error al ingresar datos de empleado')
                    return redirect('prueba')

    return render(request, 'app/prueba.html', data)


@login_required(login_url='/accounts/login')
def prueba_emp(request):

    


    return render(request, 'app/prueba_emp.html')



def handler404(request, exception):

    return render(request, 'app/error/error404.html')



















































































# Formulario de empleados
@login_required(login_url='/accounts/login')
def formr(request):
    if request.method == 'POST':
        id_repote = request.POST.get('id_repote')
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha_ingreso = request.POST.get('fecha_ingreso')
        usuario_usuario = request.POST.get('usuario_usuario')
        prioridad_id_prioridad = request.POST.get('prioridad_id_prioridad')
        piso_id_piso = request.POST.get('piso_id_piso')
        sector_id_sector = request.POST.get('sector_id_sector')
        estado_r_id_estado = request.POST.get('estado_r_id_estado')
        sucursal_id_sucursal = request.POST.get('sucursal_id_sucursal')
        imagen = request.FILES['imagen'].read()
        asignado = request.POST.get('asignado')

        salida = SP_AGREGAR_REPORTE(
            id_repote,
            titulo,
            descripcion,
            fecha_ingreso,
            usuario_usuario,
            prioridad_id_prioridad,
            piso_id_piso,
            sector_id_sector,
            estado_r_id_estado,
            sucursal_id_sucursal,
            imagen,
            asignado)

    return render(request, 'app/form_rep.html')


# formulario de solicitudes
@login_required(login_url='/accounts/login')
def formsolicitud(request):
    if request.method == 'POST':
        id_solicitud = request.POST.get('id_solicitud')
        solicitud = request.POST.get('solicitud')
        fecha = request.POST.get('fecha')
        estado_s_id_estado_solicitud = request.POST.get(
            'estado_s_id_estado_solicitud')
        sucursal_id_sucursal = request.POST.get('sucursal_id_sucursal')
        usuario_usuario = request.POST.get('usuario_usuario')

        salida = SP_AGREGAR_SOLICITUD(
            id_solicitud,
            solicitud,
            fecha,
            estado_s_id_estado_solicitud,
            sucursal_id_sucursal,
            usuario_usuario)

    return render(request, 'app/form_soli.html', )


@login_required(login_url='/accounts/login')
def formempleado(request):

    data = {
        'cargo': listado_cargo(),
        'sucursal': listado_sucursal(),

    }
    if request.method == 'POST':
        rut = request.POST.get('rut')
        dv = request.POST.get('dv')
        p_nombre = request.POST.get('p_nombre')
        s_nombre = request.POST.get('s_nombre')
        p_apellido = request.POST.get('p_apellido')
        s_apellido = request.POST.get('s_apellido')
        email = request.POST.get('email')
        cargo = request.POST.get('cargo')
        sucursal = request.POST.get('sucursal')
        imagen = request.FILES['imagen'].read()

        salida = agregar_empleado(
            rut, dv, p_nombre, s_nombre, p_apellido, s_apellido, email, cargo, sucursal, imagen)

    return render(request, 'app/form_emp.html', data)


@login_required(login_url='/accounts/login')
def modemp(request, rut):

    # producto = get_object_or_404(Empleado, id=id)

    datos_empleados = sp_listar_empleado_f(rut)

    arreglo = []
    for i in datos_empleados:
        data = {
            'data': i,
            'imagen': str(base64.b64encode(i[9].read()), 'utf-8')
        }
        arreglo.append(data)
    data = {
        'empleado': arreglo,
        'cargo': listado_cargo(),
        'sucursal': listado_sucursal()

    }

    if request.method == 'POST':
        rut = request.POST.get('rut')
        dv = request.POST.get('dv')
        p_nombre = request.POST.get('p_nombre')
        s_nombre = request.POST.get('s_nombre')
        p_apellido = request.POST.get('p_apellido')
        s_apellido = request.POST.get('s_apellido')
        email = request.POST.get('email')
        cargo = request.POST.get('cargo')
        sucursal = request.POST.get('sucursal')
        imagen = request.FILES['imagen']

        # Redimensionar imagen
        max_size = (500, 500)
        image = Image.open(imagen)
        image.thumbnail(max_size)

        # Convertir la imagen redimensionada a bytes
        image_buffer = BytesIO()
        image.save(image_buffer, format='JPEG')
        image_data = image_buffer.getvalue()

        salida = SP_MODIFICAR_EMPLEADO(
            rut, dv, p_nombre, s_nombre, p_apellido, s_apellido, email, cargo, sucursal, image_data)
        return redirect('empleado')

    return render(request, 'app/mod_emp.html', data)


@login_required(login_url='/accounts/login')
def modificarasignacion(request, idreporte):

    datos_reporte = sp_listar_reporte_f(id_reporte)

    data = {
        'usuario': datos_reporte

    }

    if request.method == 'POST':
        id_reporte = request.POST.get('id_reporte')
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha_ingreso = request.POST.get('fecha_ingreso')
        usuario_usuario = request.POST.get('usuario_usuario')

        salida = SP_MODIFICAR_reporte(id_reporte,
                                      titulo,
                                      descripcion,
                                      fecha_ingreso,
                                      usuario_usuario)

    return render(request, 'app/mod_asig_reporte.html')



# def sp_listar_reporte_f(id_reporte):
#     django_cursor = connection.cursor()
#     cursor = django_cursor.connection.cursor()
#     out_cur = django_cursor.connection.cursor()

#     cursor.callproc("SP_LISTAR_reporte_F", [out_cur, id_reporte])
#     lista = []
#     for fila in out_cur:
#         lista.append(fila)
#     return lista

# def sp_listar_usuario_f(usuario):
#     django_cursor = connection.cursor()
#     cursor = django_cursor.connection.cursor()
#     out_cur = django_cursor.connection.cursor()

#     cursor.callproc("SP_LISTAR_USUARIO_F", [out_cur, usuario])
#     lista = []
#     for fila in out_cur:
#         lista.append(fila)
#     return lista

@login_required(login_url='/accounts/login')
def modificarusuario(request, usuario):

    # producto = get_object_or_404(Empleado, id=id)

    datos_usuario = sp_listar_usuario_f(usuario)

    data = {
        'usuario': datos_usuario

    }

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')
        empleado_rut = request.POST.get('empleado_rut')
        estado_u_id_estado_u = request.POST.get('estado_u_id_estado_u')

        salida = SP_MODIFICAR_USUARIO(
            usuario, contrasena, empleado_rut, estado_u_id_estado_u)

    return render(request, 'app/mod_usuario.html', data)


@login_required(login_url='/accounts/login')
def modins(request, id_insumo):

    # producto = get_object_or_404(Empleado, id=id)

    datos_insumos = sp_listar_insumo_f(id_insumo)

    data = {
        'insumo': datos_insumos

    }

    if request.method == 'POST':
        id_insumo = request.POST.get('id_insumo')
        insumo = request.POST.get('insumo')
        stock = request.POST.get('stock')
        color = request.POST.get('color')
        sucursal_id_sucursal = request.POST.get('sucursal_id_sucursal')

        salida = SP_MODIFICAR_INSUMO(
            id_insumo, insumo, stock, color, sucursal_id_sucursal)

    return render(request, 'app/mod_insumo.html', data)


# listo
def sp_listar_insumo_f(id_insumo):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_INSUMO_F", [out_cur, id_insumo])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

@login_required(login_url='/accounts/login')
def forminsumo(request):
    if request.method == 'POST':
        id_insumo = request.POST.get('id_solicitud')
        insumo = request.POST.get('solicitud')
        stock = request.POST.get('fecha')
        color = request.POST.get('estado_s_id_estado_solicitud')
        sucursal_id_sucursal = request.POST.get('sucursal_id_sucursal')

        salida = SP_AGREGAR_INSUMO(
            id_insumo,
            insumo,
            stock,
            color,
            sucursal_id_sucursal)

    return render(request, 'app/form_ins.html')

# def listado_usuarios():
#     django_cursor =connection.cursor()
#     cursor = django_cursor.connection.cursor()
#     out_cur = django_cursor.connection.cursor()

#     cursor.callproc("SP_LISTAR_USUARIOS", [out_cur])
#     lista =[]
#     for fila in out_cur:
#         lista.append(fila)
#     return lista

# listo



# def SP_IMAGEN_EMPELADO_F():
#     django_cursor = connection.cursor()
#     cursor = django_cursor.connection.cursor()
#     out_cur = django_cursor.connection.cursor()

#     cursor.callproc("SP_IMAGEN_EMPELADO_F", [out_cur])
#     lista = []
#     for fila in out_cur:
#         lista.append(fila)
#     return lista

# listo
# def sp_listar_empleado_f(rut):
#     django_cursor = connection.cursor()
#     cursor = django_cursor.connection.cursor()
#     out_cur = django_cursor.connection.cursor()

#     cursor.callproc("SP_LISTAR_EMPLEADO_F", [out_cur, rut])
#     lista = []
#     for fila in out_cur:
#         lista.append(fila)
#     return lista
