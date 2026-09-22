from django import forms
from .models import Plato

class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato

        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'disponible']

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")
        return precio