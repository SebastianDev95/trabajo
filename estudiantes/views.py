# estudiantes/views.py
from django.shortcuts import render, redirect
from .forms import EstudianteForm

def registro_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
   
        form = EstudianteForm()
    return render(request, 'estudiantes/formulario.html', {'form': form})