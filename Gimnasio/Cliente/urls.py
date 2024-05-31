from django.urls import path
from . import views

urlpatterns = [
    path('', views.paginaprincipal, name='paginaprincipal'),
    path('opciones-entrenamiento/', views.opcion_entrenamiento, name='opcion_entrenamiento'),
    path('turno/', views.turno, name='turno'),
    path('profesores/', views.profesores, name='profesores'),
    path('about-me/', views.about_me, name='about_me'),
    path('cliente/', views.cliente_detalle, name='cliente_detalle'),
    path('inscripcion-entrenamiento/<int:entrenamiento_id>/', views.inscripcion_entrenamiento, name='inscripcion_entrenamiento'),
]
