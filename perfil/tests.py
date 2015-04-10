from django.test import TestCase
from django.contrib.auth.models import User, Group

class PerfilTestCase(TestCase):
    
    def test_crea_perfil(self):
        
        """
            Test para verificar la correcta creacion de un rol
        """
        u = Group.objects.create(name = "ADMINISTRACION" )
        self.assertTrue(isinstance(u,Group))
        print('Test de crear perfil, exitoso')