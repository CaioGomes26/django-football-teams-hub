from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_times, name='listar_times'),
    path('novo/', views.cadastrar_time, name='cadastrar_time'),
]