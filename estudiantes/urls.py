# estudiantes/urls.py
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
 
    path('', views.registro_estudiante, name='registro_estudiante'),
 
    path(
        'exito/',
        TemplateView.as_view(template_name="estudiantes/exito.html"),
        name='exito'
    ),
]