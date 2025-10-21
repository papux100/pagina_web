from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class VistaPaginaDeInicio(TemplateView):
    template_name='inicio.html'
    
class VistaPaginaDeAcerca(TemplateView):
    template_name='acerca.html'