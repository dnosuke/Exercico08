from django import forms
from .models import Despesa


class DespesaForm(forms.ModelForm):

    cliente = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',}
    ))
    produto = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',}
    ))
    fornecedor = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', }
    ))

    descricao = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', }
    ))

    class Meta:
        model = Despesa
        fields = ('cliente', 'produto', 'fornecedor', 'descricao',)

