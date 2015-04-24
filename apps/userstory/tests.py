from django.test import TestCase
from django.test import Client
from apps.flujo.models import Flujo, Actividad
from apps.proyecto.models import Proyecto
from apps.flujo.forms import FlujoModelForm
from apps.userstory.models import UserStory
from apps.userstory.forms import UserStoryModelForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

class UserStoryTestCase(TestCase):
    """
        La clase encapsula los test unitarios correspondientes a UserStory
    """

    def crear_actividad(self, nombre="Actividad 1"):
        """
            Crea una nueva Actividad
            @param nombre: Nombre de la Actividad
            @return: Actividad
        """        
        return Actividad.objects.create(nombre=nombre, flujo=self.crear_flujo(nombre))
    
    def crear_flujo(self, nombre="Flujo Prueba"):
        """
            Crea un nuevo flujo 
            @param nombre: Nombre del Flujo
            @return: Flujo
        """        
        return Flujo.objects.create(nombre=nombre)
    
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
 
    def crear_user_story(self, nombre="Story 1"):
        """
            Crea un nuevo user story
            @param nombre: Nombre del user story
            @return: UserStory
        """        
        return UserStory.objects.create(nombre=nombre, actividad=self.crear_actividad(), proyecto=self.crear_proyecto())
    
    def test_creacion_user_story(self):
        """
            Test para verificar la correcta creacion de un User Story
        """
        u = self.crear_user_story()
        self.assertTrue(isinstance(u, UserStory))
        self.assertEqual(u.__str__(), u.nombre)
        print("Test de creacion de User Story exitoso")
        
    def test_asignar_flujo_a_user_story(self):
        """
            Test para verificar la correcta asignacion de un flujo a un user story
        """
        f = self.crear_flujo()
        u = self.crear_user_story()
        u.flujo = f
        self.assertTrue(isinstance(u.flujo, Flujo))
        self.assertEqual(u.flujo.__str__(), f.__str__())
        print("Test de asignacion de User Story a Flujo exitoso")
        
    def test_asignar_actividad_a_user_story(self):
        """
            Test para verificar la correcta asignacion de la actividad a un user story
        """
        a = self.crear_actividad()
        u = self.crear_user_story()
        u.actividad = a
        self.assertTrue(isinstance(u.actividad, Actividad))
        self.assertEqual(u.actividad.__str__(), a.__str__())
        print("Test de asignacion de User Story a Actividad exitoso")
        
    def test_asignar_proyecto_a_user_story(self):
        """
            Test para verificar la correcta asignacion de un proyecto a un user story
        """
        p = self.crear_proyecto()
        u = self.crear_user_story()
        u.proyecto = p
        self.assertTrue(isinstance(u.proyecto, Proyecto))
        self.assertEqual(u.proyecto.__str__(), p.__str__())
        print("Test de asignacion de User Story a Proyecto exitoso")
 
     
    def test_formulario_invalido(self):
         
        """
            Test para verificar cuando un formulario de creacion de user stories es invalido
        """
         
        u = self.crear_user_story(nombre="X")
        data = {'nombre': u.nombre }
        form = UserStoryModelForm(data=data)
        self.assertFalse(form.is_valid())
        print("Test de formulario de creacion de user story invalido exitoso")
         

    def test_listar_user_stories(self):
        '''
         Test para ver si se listan correctamente los user stories
        '''
        c = Client()
        c.login(username='nabil', password='123')
        resp = c.get('/userstory/listar_userstories/', follow=True)
        self.assertEqual(resp.status_code, 200)
        print("Test de listado de user stories exitoso")
        
