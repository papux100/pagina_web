#from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class PruebaSecilla(SimpleTestCase):
    def test_codigo_de_estado_de_la_paginaDeInicio(self):
        respuesta = self.client.get('/')
        self.assertEqual(respuesta.status_code, 200)

    def test_codigo_de_estado_de_acercaDe(self):
        respuesta = self.client.get('/acerca/')
        self.assertEqual(respuesta.status_code, 200)

class PruebasPaginaDeInicio(SimpleTestCase):
    def test_la_url_existe_en_la_ubicacion_correcta(self):
        respuesta = self.client.get('/')
        self.assertEqual(respuesta.status_code, 200)
    
    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertEqual(respuesta.status_code, 200)
    
    def test_nombre_correcto_de_la_platilla(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertTemplateUsed(respuesta,"inicio.html")

    def test_contenido_de_la_platilla(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertContains(respuesta,"<h1>Pagina de inicio</h1>")

class PruebasPaginaAcercaDe(SimpleTestCase):
    def test_la_url_existe_en_la_ubicacion_correcta(self):
        respuesta = self.client.get('/acerca/')
        self.assertEqual(respuesta.status_code, 200)
    
    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse('acerca'))
        self.assertEqual(respuesta.status_code, 200)

    def test_nombre_correcto_de_la_platilla(self):
        respuesta = self.client.get(reverse("acerca"))
        self.assertTemplateUsed(respuesta,"acerca.html")

    def test_contenido_de_la_platilla(self):
        respuesta = self.client.get(reverse("acerca"))
        self.assertContains(respuesta,"<h1>Pafina Acerca de</h1>")

