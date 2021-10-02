from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.db import transaction
from django.contrib import messages



# Create your views here.

#Vista del Inicio
def index(request):
    titulo = 'BARBER SHOP'
    template = loader.get_template('index.html')

    if request.method == "GET":
        print("METODO GET")
    
    if request.method == "POST":
        print("METODO POST")
    
    context = {
        'titulo' : titulo,
    }
    return HttpResponse(template.render(context,request))

#Vista de Clientes

def clientes(request):
    titulo = 'BARBER SHOP'
    template = loader.get_template('clientes.html')
    lista_clientes = Cliente.objects.all().order_by('-identificador')

    if request.method == "GET":
        print("METODO GET")

    if request.method == "POST":
        nombre = request.POST.get("nombre", None)
        apellido = request.POST.get("apellido", None)
        direccion = request.POST.get("direccion", None)
        telefono = request.POST.get("telefono", None)
        añadir_cliente = request.POST.get("añadir_cliente", None)
        eliminar_cliente = request.POST.get("eliminar_cliente", None)
        modificar_cliente = request.POST.get("modificar_cliente", None)
        identificador = request.POST.get("identificador", None)

        if modificar_cliente:
            datosCliente = Cliente.objects.get(identificador = identificador)
            with transaction.atomic():
                datosCliente.nombre = nombre
                datosCliente.apellido = apellido
                datosCliente.direccion = direccion
                datosCliente.telefono = telefono
                datosCliente.save()
                messages.success(request,"El Cliente ha sido Modificado Correctamente")

        if eliminar_cliente:
            with transaction.atomic():
                Cliente.objects.filter(identificador = eliminar_cliente).delete()
                messages.error(request,"Cliente Eliminado Correctamente")

        if añadir_cliente:
            with transaction.atomic():
                nuevo_cliente = Cliente.objects.create(
                    nombre = nombre,
                    apellido = apellido,
                    direccion = direccion,
                    telefono = telefono,
                )
                messages.info(request,"El Cliente se ha Agregrado Correctamente")
    context = {
        'titulo' : titulo,
        'lista_clientes' : lista_clientes,
    }
    return HttpResponse(template.render(context,request))

#Vista de Barberos

def barberos(request):
    titulo = 'BARBER SHOP'
    template = loader.get_template('barberos.html')
    lista_barberos = Barbero.objects.all().order_by("-identificador")

    if request.method == "GET":
        print("METODO GET")
    
    if request.method == "POST":
        print("METODO POST")
    
    context = {
        'titulo' : titulo,
        'lista_barberos' : lista_barberos,
    }
    return HttpResponse(template.render(context,request))

#Vista de las Tarifas

def tarifas(request):
    titulo = 'BARBER SHOP'
    template = loader.get_template('tarifas.html')

    if request.method == "GET":
        print("METODO GET")
    
    if request.method == "POST":
        print("METODO POST")
    
    context = {
        'titulo' : titulo,
    }
    return HttpResponse(template.render(context,request))
    
#Vista de las Citas

def citas(request):
    titulo = 'BARBER SHOP'
    template = loader.get_template('citas.html')

    if request.method == "GET":
        print("METODO GET")
    
    if request.method == "POST":
        print("METODO POST")
    
    context = {
        'titulo' : titulo,
    }
    return HttpResponse(template.render(context,request))

#Vista de facturas

def facturas(request):
    titulo = 'BARBER SHOP'
    template = loader.get_template('facturas.html')

    if request.method == "GET":
        print("METODO GET")
    
    if request.method == "POST":
        print("METODO POST")
    
    context = {
        'titulo' : titulo,
    }
    return HttpResponse(template.render(context,request))