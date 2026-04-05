from django.shortcuts import render, redirect 
from .models import Time
from .forms import TimeForm

def listar_times(request):
    # Buscamos todos os times cadastrados
    times = Time.objects.all()
    # Enviamos para o template dentro de um dicionário
    return render(request, 'times/listar_times.html', {'times': times})

def cadastrar_time(request):
    if request.method == "POST":
        form = TimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_times') # Volta para a lista após salvar
    else:
        form = TimeForm()
    
    return render(request, 'times/form_time.html', {'form': form})