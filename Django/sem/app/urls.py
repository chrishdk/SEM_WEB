from django.urls import path
from .views import login,reporte,inicio

urlpatterns = [
    path('', login, name="login"),
    path('reporte/', reporte, name="reporte"),
    path('inicio/', inicio, name="inicio"),


]