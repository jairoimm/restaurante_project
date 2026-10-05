from django import forms
from .models import Plato

class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'disponible']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Hamburguesa Especial'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del plato...'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Comida rápida, Bebidas'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")
        return precio