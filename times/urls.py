from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_times, name='listar_times'),
    path('novo/', views.cadastrar_time, name='cadastrar_time'),
    path('editar/<int:pk>/', views.editar_time, name='editar_time'),
    path('deletar/<int:pk>/', views.deletar_time, name='deletar_time'),
]