from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from usuario import views
from django.test.client import RequestFactory

class UsuarioTestCase(TestCase):
    
    def setUp(self):
        """
        Funcion que inicializa el test con Datos de Prueba sobre usuarios
        """
        self.factory = RequestFactory
        self.user =  User.objects.create_user(
            username='admin', email='admin@doamin.com', password='admin')
        
        
    def test_crea_usuario(self):
        u = User.objects.create_user('user1', 'user1@domain.com', 'user1')
        self.assertTrue(isinstance(u,User))
        print('Test de crear usuario, exitoso')
        

