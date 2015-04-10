from django.test import TestCase
from django.contrib.auth.models import User, Group
from django.test import Client

class PerfilTestCase(TestCase):
    
    def test_crea_perfil(self):
        
        """
            Test para verificar la correcta creacion de un rol
        """
        u = Group.objects.create(name = "ADMINISTRACION" )
        self.assertTrue(isinstance(u,Group))
        print('Test de crear perfil, exitoso')
        
    def test_listar_perfiles(self):
        '''
         Test para ver si se listan correctamente los usuarios
        '''
        c = Client()
        c.login(username='nabil', password='123')
        resp = c.get('/perfil/listar_perfiles/', follow = True)
        self.assertEqual(resp.status_code, 200)
        print("Test de listado de perfiles exitoso")