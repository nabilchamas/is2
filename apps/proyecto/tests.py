from django.test import TestCase
from django.test import Client
from apps.proyecto.models import Proyecto
from apps.proyecto.forms import ProyectoModelForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

class ProyectoTestCase(TestCase):
    """
        Encapsula los tests de proyecto
    """
    
    
    def crear_proyecto(self, nombre="SGP", codigo="123", descripcion="Proyecto para la materia IS2", cliente="Carolina"):
        """
            Para crear un proyecto
        """        
        return Proyecto.objects.create(nombre=nombre, codigo=codigo, descripcion=descripcion, cliente=cliente)
 
    def test_creacion_proyecto(self):
        """
            Test para verificar la correcta creacion de un proyecto
        """
        p = self.crear_proyecto()
        self.assertTrue(isinstance(p, Proyecto))
        self.assertEqual(p.__str__(), p.nombre)
        print("Test de creacion de proyecto exitoso")
 
#     def test_formulario_valido(self):
# 
#         """
#             Test para verificar cuando un formulario de creacion de proyectos es valido
#         """
#         p = Proyecto.objects.create(nombre="X", codigo="321", descripcion="Proyecto X", cliente="Miguel")
#         data = {'model': p.nombre, 'codigo': p.codigo, 'descripcion': p.descripcion , 'descripcion': p.descripcion }
#         form = ProyectoModelForm(data=data)
#         self.assertTrue(form.is_valid())
#         print("Test de formulario de proyecto valido exitoso")
     
    def test_formulario_invalido(self):
         
        """
            Test para verificar cuando un formulario de creacion de proyectos es invalido
        """
         
        p = Proyecto.objects.create(nombre="X", codigo="321", descripcion="Proyecto X", cliente="Miguel")
        data = {'nombre': p.nombre, 'codigo': p.codigo, 'descripcion': p.descripcion , 'descripcion': p.descripcion }
        form = ProyectoModelForm(data=data)
        self.assertFalse(form.is_valid())
        print("Test de formulario de proyecto invalido exitoso")
         
         
    def test_llamada_a_view_negar_anonimo(self):
        
        """
            Test para verificar que se impide el acceso al apartado proyecto
            como usuario anonimo
        """
        response = self.client.get('/proyecto/', follow=True)
        self.assertRedirects(response, '/inicio/?next=/proyecto/')
        response = self.client.post('/proyecto/', follow=True)
        self.assertRedirects(response, '/inicio/?next=/proyecto/')
        print("Test de restriccion de acceso a proyecto de un usuario anonimo exitoso")

    def test_listar_proyectos(self):
        '''
         Test para ver si se listan correctamente los proyectos
        '''
        c = Client()
        c.login(username='nabil', password='123')
        resp = c.get('/proyecto/listar_proyectos/', follow = True)
        self.assertEqual(resp.status_code, 200)
        print("Test de listado de proyectos exitoso")
        
    