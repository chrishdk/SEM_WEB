from django.urls import path
from .views import reporte,inicio,empleado,usuarios, formempleado,formr,modemp,solicitud,formsolicitud,forminsumo,modins,modificarusuario,modificarasignacion,prueba,prueba_emp

urlpatterns = [
    path('', inicio, name="inicio"),
    path('reporte/', reporte, name="reporte"),
    path('usuarios/', usuarios, name="usuarios"),
    path('empleado/', empleado, name="empleado"),
    path('formempelado/', formempleado, name="formempelado"),
    path('formr/', formr, name="formr"),
    path('formsolicitud/', formsolicitud, name="formsoli"),
    path('solicitud/', solicitud, name="solicitud"),
    path('formins/', forminsumo, name="formins"),
    path('modins/<id_insumo>/', modins, name="modins"),
    path('modificarusuario/<usuario>/', modificarusuario, name="modificarusuario"),
    path('modificarasignacion/', modificarasignacion, name="modificarasignacion"),
    path('modificar_empleado/<rut>/', modemp, name="modemp"),
    path('prueba/', prueba, name="prueba"),
    path('prueba_emp/', prueba_emp, name="prueba_emp"),
]