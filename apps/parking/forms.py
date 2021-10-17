from django import forms
from django.contrib.auth.models import User
from .models import Factura, Vehiculo, Factura_servicio

class vehiculo_form(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        exclude = ['propietario',]


class factura_servicio_form(forms.ModelForm):
    class Meta:
        model = Factura_servicio
        fields = ['servicio','cantidad','vehiculo','hora_inicio','hora_fin']
        exclude = ['subtotal', 'factura']
        widgets = {
        'hora_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        'hora_fin'   : forms.DateTimeInput(attrs={'type': 'datetime-local'}),}
