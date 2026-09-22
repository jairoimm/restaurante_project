from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Plato
from .forms import PlatoForm


# Create your views here.

#Pagina principal
def inicio(request):

    return render(
        request, 
        'platos/inicio.html'
    )

#Listar
def lista_platos(request):

    platos = Plato.objects.all()

    return render(
        request, 
        'platos/lista.html',
        {'platos': platos}
    )


#Crear
def crear_plato(request):

    if request.method == 'POST':

        form = PlatoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                'lista_platos'
            )
    else:

        form = PlatoForm()

    return render(
        request, 
        'platos/crear.html',
        {'form': form}
    )

#Editar
def editar_plato(request, id):
    
    plato = get_object_or_404(
        Plato, 
        id=id
    )

    if request.method == 'POST':

        form = PlatoForm(
            request.POST, 
            instance=plato)

        if form.is_valid():

            form.save()

            return redirect('lista_platos')
    else:

        form = PlatoForm(
            instance=plato
            )

    return render(
        request, 
        'platos/editar.html',
        {'form': form}
    )

#Eliminar
def eliminar_plato(request, id):
    plato = get_object_or_404(
        Plato, 
        id=id
    )

    if request.method == 'POST':

        plato.delete()

        return redirect(
            'lista_platos'
            )

    return render(
        request, 
        'platos/eliminar.html',
        {'plato': plato}
    )

