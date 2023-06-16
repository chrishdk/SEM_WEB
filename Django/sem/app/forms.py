from django import forms
from .models import Empresa,Empleado,Reporte

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        #fields = ['empresa', 'direccion','n_direccion']
        fields = '__all__'


class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = '__all__'


