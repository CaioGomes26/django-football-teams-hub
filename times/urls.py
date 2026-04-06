from django.urls import path
from . import views

# times/urls.py
urlpatterns = [
    path('', views.listar_times, name='listar_times'),
    path('cadastrar/', views.cadastrar_time, name='cadastrar_time'),
    path('editar/<int:pk>/', views.editar_time, name='editar_time'),
    path('deletar/<int:pk>/', views.deletar_time, name='deletar_time'),
]