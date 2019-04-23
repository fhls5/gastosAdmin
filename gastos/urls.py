from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar_usuario', views.agregar_usuario, name='agregar_usuario'),
    path('obtener_usuario', views.obtener_usuario, name='obtener_usuario'),
    path('agregar_estado', views.agregar_estado, name='agregar_estado'),
    path('agregar_categoria', views.agregar_categoria, name='agregar_categoria'),
    path('agregar_gasto', views.agregar_gasto, name='agregar_gasto'),
]