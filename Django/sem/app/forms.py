from django import forms
from .models import Empresa,Empleado

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        #fields = ['empresa', 'direccion','n_direccion']
        fields = '__all__'


