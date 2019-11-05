from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Lista # Importar models Lista
from .forms import CadastrarForm  # Importar CadastraForm de forms.py
from django.utils import timezone

def index(request):
    grid = Lista.objects.all()
    hoje = timezone.localdate()

    for item in grid:
        vencimento = item.expire_date.date()
        dias = (vencimento - hoje).days
        if dias > 1:
            item.dias = "Vence em {} dias".format(str(dias))
            item.save()
        if dias < 5 and dias >1:
            item.atencao = True
            item.save()
        else:
            item.atencao = False
            item.save()

        print(item.atencao)

    context = {
        'grid': grid,
        'hoje': hoje,
    }
    return render(request, 'lista/index.html', context)

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
