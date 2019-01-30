from django.shortcuts import render
from .models import Despesa
from .forms import DespesaForm
from django.shortcuts import redirect


def home(request):
    return render(request, 'core/index.html',)


def form(request):
    if request.method == "POST":
        form = DespesaForm(request.POST)
        if form.is_valid():
            despesa = form.save(commit=False)
            despesa.save()
            return redirect('form')
    else:
        form = DespesaForm()
    return render(request, 'core/base_form.html', {'form': form})


def lista(request):
    despesa = Despesa.objects.all().order_by('cliente')
    return render(request, 'core/base_lista.html', {"despesa": despesa})


def login(request):
    return render(request, 'core/login.html', {"login": login})


