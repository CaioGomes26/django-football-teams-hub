from django.shortcuts import render, redirect, get_object_or_404
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
    
    return render(request, 'times/form_time.html', {'form': form, 'titulo': 'Cadastrar Novo Time'})

def editar_time(request, pk):
    time = get_object_or_404(Time, pk=pk)
    if request.method == 'POST':
        form = TimeForm(request.POST, instance=time)
        if form.is_valid():
            form.save()
            return redirect('listar_times')
    else:
        form = TimeForm(instance=time)
    return render(request, 'times/form_time.html', {'form': form, 'titulo': 'Editar Time'})

def deletar_time(request, pk):
    time = get_object_or_404(Time, pk=pk)
    if request.method == 'POST':
        time.delete()
        return redirect('listar_times')
    return render(request, 'times/confirm_delete.html', {'time': time})

def home(request):
    total_times = Time.objects.count()
    return render(request, 'times/home.html', {'total_times': total_times})