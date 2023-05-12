from django.urls import path
from .views import login,reporte,inicio,usuarios

urlpatterns = [
    path('', login, name="login"),
    path('reporte/', reporte, name="reporte"),
    path('inicio/', inicio, name="inicio"),
    path('usuarios/', usuarios, name="usuarios"),


]