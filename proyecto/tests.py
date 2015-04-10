from django.test import TestCase
from proyecto.models import Proyecto
from proyecto.forms import ProyectoModelForm
from django.core.urlresolvers import reverse

class ProyectoTestCase(TestCase):
    
    
    def crear_proyecto(self, nombre="SGP", codigo="123", descripcion="Proyecto para la materia IS2", cliente="Carolina"):
        return Proyecto.objects.create(nombre=nombre, codigo=codigo, descripcion=descripcion, cliente=cliente)

    def test_creacion_proyecto(self):
        p = self.crear_proyecto()
        self.assertTrue(isinstance(p, Proyecto))
        self.assertEqual(p.__str__(), p.nombre)
        print("Test de creacion de proyecto exitoso")
        
#     def test_proyecto_list_view(self):
#         w = self.crear_proyecto()
#         url = reverse("proyecto.views.menu_proyecto")
#         resp = self.client.get(url)
#         self.assertEqual(resp.status_code, 200)
#         self.assertIn(w.title, resp.content)
#         print("Test de acceso a proyectos exitoso")

#     def test_valid_form(self):
#         p = Proyecto.objects.create(nombre="X", codigo="321", descripcion="Proyecto X", cliente="Miguel")
#         data = {'model': p.nombre, 'codigo': p.codigo, 'descripcion': p.descripcion , 'descripcion': p.descripcion }
#         form = ProyectoModelForm(data=data)
#         self.assertTrue(form.is_valid())
#         print("Test de formulario de creacion de proyecto exitoso")
    
    def test_invalid_form(self):
        p = Proyecto.objects.create(nombre="X", codigo="321", descripcion="Proyecto X", cliente="Miguel")
        data = {'nombre': p.nombre, 'codigo': p.codigo, 'descripcion': p.descripcion , 'descripcion': p.descripcion }
        form = ProyectoModelForm(data=data)
        self.assertFalse(form.is_valid())
        print("Test de formulario invalido de proyecto exitoso")
