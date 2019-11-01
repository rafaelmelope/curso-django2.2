from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Lista # Importar models Lista
from .forms import CadastrarForm  # Importar CadastraForm de forms.py

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    grid = Lista.objects.all()
    return render(request, 'lista/index.html', {'grid': grid})


def cadatrar_new(request):
    form = CadastrarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, 'lista/new.html', {'form': form})

def cadastrar_update(request, id):
    item = get_object_or_404(Lista, pk=id)
    form = CadastrarForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, 'lista/new.html', {'form': form})

def cadastrar_delete(request, id):
    item = get_object_or_404(Lista, pk=id)
    form = CadastrarForm(request.POST or None, instance=item)

    if request.method == 'POST':
        item.delete()
        return redirect("index")

    return render(request, 'lista/delete.html', {'produto': item.title})
