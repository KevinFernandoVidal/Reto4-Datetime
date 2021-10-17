from apps.parking.models import Factura_servicio
from django import forms
from django.contrib.auth.models import User
from .models import Persona


class login_form (forms.Form):
    email     = forms.EmailField()
    clave     = forms.CharField(label='Contraseña' ,widget=forms.PasswordInput(render_value=False))

class register_form (forms.Form):
    email      = forms.EmailField()
    clave_1    = forms.CharField(label='Contraseña' ,widget=forms.PasswordInput(render_value=False))
    clave_2    = forms.CharField(label='Confirme la contraseña' ,widget=forms.PasswordInput(render_value=False))

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            c = User.objects.get(username = email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('El Email ingresado, ya se encuentra registrado')

    def clean_clave_2 (self):
        clave_1 = self.cleaned_data['clave_1']
        clave_2 = self.cleaned_data['clave_2']
        if clave_1 == clave_2:
            return clave_2
        else:
            raise forms.ValidationError ('las contraseñas no coinciden, por favor Intente nuevamente')

class persona_form (forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        exclude = ['id_user']


        