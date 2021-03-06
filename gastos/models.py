from django.db import models

#from django.db import models desce aca
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils import timezone #agregado

#desce aca
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
#hasta aca

class Estado(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=50)


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)  # Tiene que referenciar a la columna de la tabla Estado


class Categorias(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)    # Tiene que referenciar a la columna de la tabla Estado


class Gastos(models.Model):
    monto = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)  # Solamente tiene que Date no DateTime
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Probablemente esta columna este demás
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)   # Tiene que referenciar a la columna de la tabla Estado
