from django.shortcuts import render, redirect
from .models import Lista
from .forms import CadastrarForm

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    grid = Lista.objects.all()
    return render(request, 'lista/index.html', {'grid': grid})


def cadatrar_new(request):
    form = CadastrarForm(request.POST, None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, 'lista/new.html', {'form': form})