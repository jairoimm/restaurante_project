from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Plato

class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'disponible']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Hamburguesa Especial', 'maxlength': '100'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción detallada del plato (mín. 10 caracteres)...'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00', 'step': '0.01'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Comida rápida, Bebidas', 'maxlength': '50'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        error_messages = {
            'nombre': {
                'required': 'El nombre del plato es obligatorio.',
                'max_length': 'El nombre no puede exceder los 100 caracteres.',
            },
            'descripcion': {
                'required': 'La descripción es obligatoria.',
            },
            'precio': {
                'required': 'El precio es obligatorio.',
                'invalid': 'Ingrese un valor numérico válido para el precio.',
            },
            'categoria': {
                'required': 'La categoría es obligatoria.',
                'max_length': 'La categoría no puede exceder los 50 caracteres.',
            }
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre del plato debe tener al menos 3 caracteres.")
        
        # Validar unicidad (ignorando mayúsculas/minúsculas o exacto)
        qs = Plato.objects.filter(nombre__iexact=nombre)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Ya existe un plato registrado con este nombre.")
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion', '').strip()
        if len(descripcion) < 10:
            raise forms.ValidationError("La descripción debe tener al menos 10 caracteres para detallar adecuadamente el plato.")
        return descripcion

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None:
            if precio <= 0:
                raise forms.ValidationError("El precio debe ser un valor mayor que cero (0).")
            if precio > 999999.99:
                raise forms.ValidationError("El precio ingresado es demasiado alto.")
        return precio

    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria', '').strip()
        if len(categoria) < 2:
            raise forms.ValidationError("La categoría debe tener al menos 2 caracteres.")
        return categoria


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=20,
        min_length=3,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario', 'maxlength': '20'}),
        error_messages={
            'max_length': 'El usuario no puede superar los 20 caracteres.',
            'min_length': 'El usuario debe tener al menos 3 caracteres.',
            'required': 'El campo usuario es obligatorio.'
        }
    )
    password = forms.CharField(
        max_length=15,
        min_length=4,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'maxlength': '15'}),
        error_messages={
            'max_length': 'La contraseña no puede superar los 15 caracteres.',
            'min_length': 'La contraseña debe tener al menos 4 caracteres.',
            'required': 'El campo contraseña es obligatorio.'
        }
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].max_length = 20
        self.fields['username'].widget.attrs['maxlength'] = '20'
        self.fields['password'].max_length = 15
        self.fields['password'].widget.attrs['maxlength'] = '15'
