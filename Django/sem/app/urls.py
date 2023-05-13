from django.urls import path
from .views import login,reporte,inicio,empleado,usuarios, formempleado,formr

urlpatterns = [
    path('', login, name="login"),
    path('reporte/', reporte, name="reporte"),
    path('inicio/', inicio, name="inicio"),
    path('usuarios/', usuarios, name="usuarios"),
    path('empleado/', empleado, name="empleado"),
    path('formempelado/', formempleado, name="formempelado"),
    path('formr/', formr, name="formr"),
]