from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from usuario import views
from django.test.client import RequestFactory

class UsuarioTestCase(TestCase):
    
    def setUp(self):
        """
        Funcion que inicializa los datos para el test
        """
        self.factory = RequestFactory        
        
    def test_crea_usuario(self):
        
        """
            Test para verificar la correcta creacion de un usuario
        """
        
        u = User.objects.create_user('user1', 'user1@domain.com', 'user1')
        self.assertTrue(isinstance(u,User))
        print('Test de crear usuario, exitoso')
        

