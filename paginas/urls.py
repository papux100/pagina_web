from django.urls import path
from .views import VistaPaginaDeInicio, VistaPaginaDeAcerca

urlpatterns = [
    path('', VistaPaginaDeInicio.as_view(),name='inicio'),
    path('acerca/', VistaPaginaDeAcerca.as_view(),name='acerca'),
]
