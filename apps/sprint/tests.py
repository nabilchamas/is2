from django.test import TestCase
from django.test import Client
from apps.flujo.models import Flujo, Actividad
from apps.proyecto.models import Proyecto
from apps.flujo.forms import FlujoModelForm
from apps.userstory.models import UserStory
from apps.userstory.forms import UserStoryModelForm
from apps.sprint.models import Sprint
from apps.sprint.forms import SprintModelForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group
import datetime
from time import timezone

class SprintTestCase(TestCase):
    """
        Clase que encapsula los test unitarios de Sprint
    """
    
    def crear_proyecto(self, nombre="SGP", codigo="123", descripcion="Proyecto para la materia IS2", cliente="Carolina"):
        """
            Crea un nuevo proyecto
            @param nombre: Nombre del proyecto
            @param codigo: Codigo de identificacion del proyecto
            @param descripcion: Descripcion breve del proyecto
            @param cliente:Cliente del proyecto
            @return: Proyecto
        """        
        return Proyecto.objects.create(nombre=nombre, codigo=codigo, descripcion=descripcion, cliente=cliente)
 
    def crear_sprint(self, nombre="Sprint 1", descripcion="Sprint de prueba"):
        """
            Crea un nuevo Sprint
            @param nombre: Nombre del Sprint
            @param descripcion: Un breve detalle referente al Sprint
            @return: Sprint
        """        
        return Sprint.objects.create(nombre=nombre, descripcion=descripcion, proyecto=self.crear_proyecto(), fecha_inicio= "2015-01-23" , fecha_fin= "2016-01-23")
    
    def test_creacion_sprint(self):
        """
            Test para verificar la correcta creacion de un Sprint
        """
        s = self.crear_sprint()
        self.assertTrue(isinstance(s, Sprint))
        self.assertEqual(s.__str__(), s.nombre)
        print("Test de creacion de Sprint exitoso")
        
    def test_asignar_proyecto_a_sprint(self):
        """
            Test para verificar la correcta asignacion del sprint a un proyecto
        """
        p = self.crear_proyecto()
        s = self.crear_sprint()
        s.proyecto = p
        self.assertTrue(isinstance(s.proyecto, Proyecto))
        self.assertEqual(s.proyecto.__str__(), p.__str__())
        print("Test de asignacion de Sprint a Proyecto exitoso")
 
     
    def test_formulario_invalido(self):
          
        """
            Test para verificar cuando un formulario de creacion de sprints es invalido
        """
          
        u = self.crear_sprint("A", "AA")
        data = {'nombre': u.nombre }
        form = SprintModelForm(data=data)
        self.assertFalse(form.is_valid())
        print("Test de formulario de creacion de sprint invalido exitoso")
         

    def test_listar_sprints(self):
        '''
         Test para ver si se listan correctamente los sprints
        '''
        c = Client()
        c.login(username='nabil', password='123')
        resp = c.get('/sprint/listar_sprints/', follow=True)
        self.assertEqual(resp.status_code, 200)
        print("Test de listado de sprints exitoso")
