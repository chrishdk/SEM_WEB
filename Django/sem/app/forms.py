from django import forms
from .models import Reporte

class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        # fields = ['nombre', 'descripcion', 'imagen']
        fields = '__all__'