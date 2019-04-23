from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
import json
from gastos.models import Usuario
from gastos.models import Estado
from gastos.models import Categorias
from gastos.models import Gastos


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@requires_csrf_token
def agregar_usuario(request): # funciona
    post_data = request.body
    data = json.loads(post_data)
    estado_id = Estado.objects.get(id=data.get("id"))
    nombre = data.get('nombre')
    contrasena = data.get('contrasena')

    usuario = Usuario(nombre=nombre, contrasena=contrasena, estado=estado_id)
    usuario.save()

    return HttpResponse("Se creo el usuario")


def obtener_usuario(request): # funciona
    data = request.GET
    id = data.get('id')
    usuario = Usuario.objects.get(id=id)

    return HttpResponse("Se obuvo el usuario")


@requires_csrf_token
def agregar_estado(request): # funciona
    post_data = request.body
    data = json.loads(post_data)
    nombre = data.get("nombre")
    descripcion = data.get("descripcion")

    estado = Estado(nombre=nombre, descripcion=descripcion)
    estado.save()

    return HttpResponse("Se creo el Estado")


@requires_csrf_token
def agregar_categoria(request): # funciona
    post_data = request.body
    data = json.loads(post_data)
    nombre = data.get("nombre")
    usuario = Usuario.objects.get(id=data.get("usuario_id"))
    estado = Estado.objects.get(id=data.get("estado_id"))

    categoria = Categorias(nombre=nombre, usuario=usuario, estado=estado)
    categoria.save()

    return HttpResponse("Se creo la Categoria")


#@requires_csrf_token
def agregar_gasto(request):
    post_data = request.body
    data = json.loads(post_data)
    monto = data.get("monto")
    fecha = data.get("fecha")
    categoria = Categorias.objects.get(id=data.get("categoria_id"))
    usuario = Usuario.objects.get(id=data.get("usuario_id"))
    estado = Estado.objects.get(id=data.get("estado_id"))

    gasto = Gastos(monto=monto, fecha=fecha, categoria=categoria, usuario=usuario, estado=estado)
    gasto.save()

    return HttpResponse("Se creo el Gasto")
