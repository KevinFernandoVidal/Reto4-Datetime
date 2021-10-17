from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import login_form, persona_form, register_form, login_form
from .models import Persona
# Create your views here.

def login_view(request):
    ema = ""
    cla = ""
    if request.method == 'POST':
        for_l = login_form(request.POST)
        if for_l.is_valid():
            ema = for_l.cleaned_data['email']
            cla = for_l.cleaned_data['clave']
            usuario = authenticate(username=ema, password=cla)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('/')
            else:
                men = 'Sus credeciales son incorrectas'
    else:
        for_l = login_form()
    return render (request, 'usuario/login.html', locals())

def register_view(request):
    if request.method == 'POST':
        form_u = register_form(request.POST)
        form_p = persona_form(request.POST)
        if form_u.is_valid() and form_p.is_valid():
            email = form_u.cleaned_data['email']
            clave_1 = form_u.cleaned_data['clave_1']
            clave_2 = form_u.cleaned_data['clave_2']
            u = User.objects.create_user(username= email, password= clave_2, is_superuser=False, is_staff=True)        
            p = form_p.save(commit=False)
            u.save()
            p.id_user = u
            p.save()
            usuario = authenticate(username=email, password=clave_2)
            login(request, usuario)
            return redirect ('/')
    else:
        form_u = register_form(request.POST)
        form_p = persona_form(request.POST)
    return render(request, 'usuario/register.html', locals())

def logout_view(request):
    logout(request)
    return redirect ('/login/')

def update_view(request):
    persona = Persona.objects.get(id = request.user.id)
    if request.method == 'POST':
        form_p = persona_form(request.POST, instance=persona)
        if form_p.is_valid():
            form_p.save()
            return redirect('/')
    else:
        form_p = persona_form(instance=persona)
    return render (request, 'usuario/updte_user.html', locals())