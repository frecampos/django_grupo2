from django.shortcuts import render
from .models import SliderIndex,MisionVision,Insumos

# utilizar la tabla de Usuarios (User)
from django.contrib.auth.models import User
# libreria de authenticated
from django.contrib.auth import authenticate, logout, login as login_aut
# uso de un decorador para impedir el acceso a paginas
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def index(request):
    autos = SliderIndex.objects.all()
    return render(request,'web/Inicio2.html',{'autos':autos})

@login_required(login_url='/login/')
def galeria(request):
    return render(request,'web/Galeria2.html')

@login_required(login_url='/login/')
@permission_required('myCar.change_insumos',login_url='/login/')
def modificar_insumo(request):
    if request.POST:
        nombre = request.POST.get("nombreInsumo")
        precio = request.POST.get("precio")
        desc   = request.POST.get("descrip")
        stock  = request.POST.get("stock")
        try:
            insumo = Insumos.objects.get(nombre=nombre)
            insumo.precio = precio
            insumo.descripcion = desc
            insumo.stock = stock
            insumo.save()
            msg='Datos Modificados'
        except:
            msg='No Existe Insumo'
    insu = Insumos.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':insu,'msg':msg})    
        

@login_required(login_url='/login/')
@permission_required('myCar.view_insumos',login_url='/login/')
def buscar_insumo(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        return render(request,'web/Form_Insumo_mod.html',{'insumo':insumo})
    except:
        msg='No Encontro Insumo'
    insu = Insumos.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':insu,'msg':msg})

@login_required(login_url='/login/')
@permission_required('myCar.view_insumos',login_url='/login/')
@permission_required('myCar.delete_insumos',login_url='/login/')
def eliminar(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        insumo.delete()
        msg='Elimino'
    except:
        msg='No Elimino'
    insu = Insumos.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':insu,'msg':msg})

@login_required(login_url='/login/')
@permission_required('myCar.view_insumos',login_url='/login/')
def admin_insumos(request):
    insu = Insumos.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':insu})

@login_required(login_url='/login/')
@permission_required('myCar.add_insumos',login_url='/login/')
def insumos(request):
    if request.POST:
        nombre = request.POST.get("nombreInsumo")
        precio = request.POST.get("precio")
        desc   = request.POST.get("descrip")
        stock  = request.POST.get("stock")

        insumo = Insumos(
            nombre=nombre,
            precio=precio,
            descripcion=desc,
            stock=stock
        )
        insumo.save()
        return render(request,'web/Formulario-Insumo.html',{'msg':'grabo insumo'})    
    return render(request,'web/Formulario-Insumo.html')

@login_required(login_url='/login/')
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