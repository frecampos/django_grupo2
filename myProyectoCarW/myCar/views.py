from django.shortcuts import render
from .models import SliderIndex,MisionVision

# utilizar la tabla de Usuarios (User)
from django.contrib.auth.models import User
# libreria de authenticated
from django.contrib.auth import authenticate, logout, login as login_aut
# uso de un decorador para impedir el acceso a paginas
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    autos = SliderIndex.objects.all()
    return render(request,'web/Inicio2.html',{'autos':autos})

def galeria(request):
    return render(request,'web/Galeria2.html')

def formulario(request):
    if request.POST:
        nombre = request.POST.get("nombres")
        apellido = request.POST.get("apellido")
        email = request.POST.get("correo")
        usuario = request.POST.get("usuario")
        pass1 = request.POST.get("passw1")
        pass2 = request.POST.get("passw2")
        try:
            u = User.objects.get(username=usuario)
            return render(request,'web/Formulario2.html',{'msg':'usuario existe'})
        except:            
            if pass1!=pass2:
                return render(request,'web/Formulario2.html',{'msg':'password incorrectas'})
            u = User()
            u.first_name= nombre
            u.last_name = apellido
            u.email= email
            u.username = usuario
            u.set_password(pass1)
            u.save()
            return render(request,'web/Formulario2.html',{'msg':'grabo usuario'})
    return render(request,'web/Formulario2.html')

def MisionyVision(request):
    myv = MisionVision.objects.all()
    return render(request,'web/Objetivo.html',{'myv':myv})

def logout_v(request):
    logout(request)
    autos = SliderIndex.objects.all()
    return render(request,'web/Inicio2.html',{'autos':autos})

def login(request):
    if request.POST:
        usuario = request.POST.get("usuario")
        password = request.POST.get("passw1")
        us = authenticate(request, username=usuario,password=password)
        if us is not None and us.is_active:
            login_aut(request,us)
            autos = SliderIndex.objects.all()
            return render(request,'web/Inicio2.html',{'autos':autos})
        else:
            return render(request,'web/login.html',{'msg':'usuario / pass incorrecta'})
    return render(request,'web/login.html')