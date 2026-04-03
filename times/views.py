from django.shortcuts import render
from .models import Time

def listar_times(request):
    # Buscamos todos os times cadastrados
    times = Time.objects.all()
    # Enviamos para o template dentro de um dicionário
    return render(request, 'times/listar_times.html', {'times': times})