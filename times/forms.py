from django import forms
from .models import Time

class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        # campos que o usuário pode preencher
        fields = ['nome', 'ano_fundacao', 'pais', 'estado', 'cidade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_fundacao': forms.NumberInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
        }