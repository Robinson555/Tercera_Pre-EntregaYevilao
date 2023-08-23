from django.shortcuts import render
from .models import Gatos, Perros, Fecha_Ingreso, Clientes
from django.http import HttpResponse
from .forms import PerrosForm, GatosForm, Fecha_IngresoForm, ClienteForm 

# Create your views here.

def inicio(request):
    return render(request, "AppProyecto/inicio.html")

#SECCION VIEWS PERROS

def crear_perro(request):
    if request.method=="POST":
        form=PerrosForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            edad=info["edad"]
            raza=info["raza"]
            perros=Perros(nombre=nombre,edad=edad,raza=raza)
            Perros.save()
            formulario_perros=PerrosForm()
            return render(request,"AppProyecto/perros.html", {"mensaje":"Paciente Creado", "formulario":formulario_perro})
        else:
            return render(request,"AppProyecto/perros.html", {"mensaje":"Datos no validos"}) 
    else:
        formulario_perros=PerrosForm()

    return render(request,"AppProyecto/perros.html", {"formulario":formulario_perros})

#SECCION VIEWS GATOS

def crear_gato(request):
    if request.method=="POST":
        form=GatosForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            edad=info["edad"]
            gatos=Gatos(nombre=nombre,edad=edad)
            Gatos.save()
            formulario_gatos=GatosForm()
            return render(request,"AppProyecto/gatos.html", {"mensaje":"Paciente Creado", "formulario":formulario_gatos})
        else:
            return render(request,"AppProyecto/gatos.html", {"mensaje":"Datos no validos"}) 
    else:
        formulario_gatos=GatosForm()

    return render(request,"AppProyecto/gatos.html", {"formulario":formulario_gatos})

#SECCION VIEWS PERROS

def fecha_ingreso(request):
    if request.method=="POST":
        form=Fecha_IngresoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            dni=info["dni"]
            fecha_ingreso=info["fecha_ingreso"]
            fecha_ingreso=fecha_ingreso(dni=dni,fecha_ingreso=fecha_ingreso)
            cliente.save()
            formulario_fecha_ingreso=Fecha_IngresoForm()
            return render(request,"AppProyecto/fecha_ingreso.html", {"mensaje":"Cliente Ingresado a la Plataforma", "formulario":ingreso})
        else:
            return render(request,"AppProyecto/fecha_ingreso.html", {"mensaje":"Datos no validos"}) 
    else:
        formulario_fecha_ingreso=Fecha_IngresoForm()

    return render(request,"AppProyecto/fechaIngreso.html", {"formulario":formulario_fecha_ingreso})

#SECCION VIEWS CLIENTES

def clientes(request):
    if request.method=="POST":
        form=ClienteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            dni=info["dni"]
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            cliente=Cliente(dni=dni,nombre=nombre,apellido=apellido,email=email)
            cliente.save()
            formulario_cliente=ClienteForm()
            return render(request,"AppProyecto/clientes.html", {"mensaje":"Cliente Creado", "formulario":formulario_cliente})
        else:
            return render(request,"AppProyecto/clientes.html", {"mensaje":"Datos no validos"}) 
    else:
        formulario_cliente=ClienteForm()

    return render(request,"AppProyecto/clientes.html", {"formulario":formulario_cliente})
