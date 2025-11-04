# estudiantes/forms.py
from django import forms
from .models import Estudiante
import re

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'edad', 'correo']

    def clean_nombre(self):
        """
        Validación: El nombre no puede contener números.
        """
        nombre = self.cleaned_data.get('nombre')
        if re.search(r'\d', nombre):
            raise forms.ValidationError("El nombre no puede contener números.")
        return nombre

    def clean_edad(self):
        """
        Validación: La edad debe estar entre 5 y 100 años.
        """
        edad = self.cleaned_data.get('edad')
        if edad < 5:
            raise forms.ValidationError("La edad debe ser mayor o igual a 5 años.")
        
        # --- NUEVA VALIDACIÓN AÑADIDA ---
        if edad > 100:
            raise forms.ValidationError("La edad no puede ser mayor a 100 años.")
        # --- FIN DE LA VALIDACIÓN ---
        
        return edad

    # --- NUEVA FUNCIÓN AÑADIDA ---
    def clean_correo(self):
        """
        Validación: El correo no debe estar repetido en la base de datos.
        """
        correo = self.cleaned_data.get('correo')
        
        # Comprobamos si ya existe un Estudiante con ese correo
        if Estudiante.objects.filter(correo=correo).exists():
            raise forms.ValidationError("Este correo electrónico ya ha sido registrado.")
        
        return correo
    # --- FIN DE LA FUNCIÓN ---