from django.test import TestCase
from django.test import Client
from apps.flujo.models import Flujo, Actividad
from apps.proyecto.models import Proyecto
from apps.flujo.forms import FlujoModelForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

class FlujoTestCase(TestCase):
    """
        La clase encapsula los tests unitarios correspondientes a Flujo
    """

    def crear_actividad(self, nombre="Actividad 1"):
        """
            Crea una actividad con el nombre por defecto de "Actividad 1"
            @param param: Nombre de la actividad
            @return: La nueva actividad
        """        
        return Actividad.objects.create(nombre = nombre, flujo = self.crear_flujo(nombre))
    
    
    def test_creacion_actividad(self):
        """
            Test para verificar la correcta creacion de una Actividad
        """
        a = self.crear_actividad()
        self.assertTrue(isinstance(a, Actividad))
        self.assertEqual(a.__str__(), a.nombre)
        print("Test de creacion de Actividad exitoso")
    
    def crear_flujo(self, nombre="Flujo Prueba"):
        """
            Crea un flujo
            @param nombre: Nombre del flujo
            @return: El flujo creado
        """        
        return Flujo.objects.create(nombre=nombre)
    
    def crear_proyecto(self, nombre="SGP", codigo="123", descripcion="Proyecto para la materia IS2", cliente="Carolina"):
        """
            Para crear un proyecto
            @param nombre: Nombre del Proyecto
            @param codigo: Codigo de identificacion del proyecto
            @param descripcion: Descriipcion breve del proyecto
            @param cliente: Cliente del proyecto
            @return: Proyecto
        """        
        return Proyecto.objects.create(nombre=nombre, codigo=codigo, descripcion=descripcion, cliente=cliente)
 
    def test_creacion_flujo(self):
        """
            Test para verificar la correcta creacion de un Flujo
        """
        f = self.crear_flujo()
        self.assertTrue(isinstance(f, Flujo))
        self.assertEqual(f.__str__(), f.nombre)
        print("Test de creacion de Flujo exitoso")
        
    def test_asignar_proyecto_a_flujo(self):
        """
            Test para verificar la correcta asignacion del Proyecto a un Flujo
        """
        f = self.crear_flujo()
        f.proyecto = self.crear_proyecto()
        self.assertTrue(isinstance(f.proyecto, Proyecto))
        self.assertEqual(f.proyecto.__str__(), f.proyecto.nombre)
        print("Test de asignacion de Proyecto a Flujo exitoso")
        
        
    def test_asignar_flujo_a_actividad(self):
        """
            Test para verificar la correcta asociacion de una Actividad a un Flujo
        """
        f = self.crear_flujo()
        a = self.crear_actividad()
        a.flujo = f
        self.assertTrue(isinstance(a.flujo, Flujo))
        self.assertEqual(a.flujo.__str__(), f.__str__())
        print("Test de asignacion de Actividad a Flujo exitoso")
 
     
    def test_formulario_invalido(self):
         
        """
            Test para verificar cuando un formulario de creacion de flujos es invalido
        """
         
        f = Flujo.objects.create(nombre="X")
        data = {'nombre': f.nombre}
        form = FlujoModelForm(data=data)
        self.assertFalse(form.is_valid())
        print("Test de formulario de creacion de flujo valido exitoso")
         

    def test_listar_flujos(self):
        '''
         Test para ver si se listan correctamente los flujos
        '''
        c = Client()
        c.login(username='nabil', password='123')
        resp = c.get('/flujo/listar_flujos/', follow = True)
        self.assertEqual(resp.status_code, 200)
        print("Test de listado de flujos exitoso")
        