from django import forms
from website.models import *

class InsereTarefaForm(forms.ModelForm):
    Opcoes = [
        ('Baixa', 'Baixa'),
        ('Media', 'Média'),
        ('Alta', 'Alta'),
    ]
    Op = [
        ('Pendente', 'Pendente'),
    ]

    prioridade = forms.ChoiceField(choices=Opcoes, widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices=Op,widget=forms.Select(attrs={'class': 'form-control'}))  

    class Meta:
        model = Tarefa

        fields = [
            'descricao',
            'setor',
            'prioridade',
            'data',
            'status'
        ]

        exclude = []