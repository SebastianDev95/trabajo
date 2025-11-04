# estudiantes/forms.py
from django import forms
from .models import Estudiante
import re # Importamos re para la validación del nombre

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'edad', 'correo']

    def clean_nombre(self):
        """
        Validación personalizada para el campo 'nombre'.
        Asegura que el nombre no contenga números[cite: 15].
        """
        nombre = self.cleaned_data.get('nombre')
        # Usamos una expresión regular para buscar cualquier dígito
        if re.search(r'\d', nombre):
            raise forms.ValidationError("El nombre no puede contener números.")
        return nombre

    def clean_edad(self):
        """
        Validación personalizada para el campo 'edad'.
        Asegura que la edad sea mayor o igual a 5[cite: 16].
        """
        edad = self.cleaned_data.get('edad')
        if edad < 5:
            raise forms.ValidationError("La edad debe ser mayor o igual a 5 años.")
        return edad