from django.urls import path
from .views import home, inicio

urlpatterns = [
    path('', home, name="login"),
    path('inicio/', inicio, name="inicio")
]