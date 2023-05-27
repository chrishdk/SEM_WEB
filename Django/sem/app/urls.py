from django.urls import path
from .views import reporte,inicio,empleado,usuarios, formempleado,formr,modemp,solicitud,formsolicitud,forminsumo,modins,modificarusuario

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
    path('modificar_empleado/<rut>/', modemp, name="modemp"),
]