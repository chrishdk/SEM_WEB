from django.urls import path
from .views import reporte,inicio,empleado,usuarios,solicitud,prueba,prueba_emp,insumo,historial,export_to_excel,administracion
from django.contrib import admin

urlpatterns = [
    path('', inicio, name="inicio"),
    path('reporte/', reporte, name="reporte"),
    path('usuarios/', usuarios, name="usuarios"),
    path('empleado/', empleado, name="empleado"),
    path('insumo/', insumo, name="insumo"),
    path('historial/', historial, name="historial"),
    # path('formempelado/', formempleado, name="formempelado"),
    # path('formr/', formr, name="formr"),
    # path('formsolicitud/', formsolicitud, name="formsoli"),
    path('solicitud/', solicitud, name="solicitud"),
    # path('formins/', forminsumo, name="formins"),
    # path('modins/<id_insumo>/', modins, name="modins"),
    # path('modificarusuario/<usuario>/', modificarusuario, name="modificarusuario"),
    # path('modificarasignacion/', modificarasignacion, name="modificarasignacion"),
    # path('modificar_empleado/<rut>/', modemp, name="modemp"),
    path('prueba/', prueba, name="prueba"),
    path('pepe/', prueba_emp, name="prueba_emp"),
    path('export/', export_to_excel, name='export_to_excel'),
    path('administracion/', administracion, name="administracion"),
]