from django.test import TestCase
from apps.usuario import views
from django.contrib.auth.models import User
from django.test import Client


class InicioTestCase(TestCase):
    
    def setUp(self):
        """
        Funcion que inicializa el test con Datos de Prueba
        """
        self.client = Client()
        self.username = 'admin'
        self.email = 'admin@gmail.com'
        self.password = 'admin'
        self.test_user = User.objects.create_user(self.username, self.email, self.password)
    
    def test_inicio(self):
        """
            Test para verificar si va a la pagina de inicio
        """
        resp = self.client.get("/inicio/")
        self.assertEqual(resp.status_code, 200)
        print('Test inicio de la aplicacion exitoso')
        
 
    def test_login(self):
        """
            Test para verificar si realiza el login
        """  
        resp = self.client.get('/inicio/')
        self.assertEqual(resp.status_code, 200)
        resp= self.client.post('/inicio/', {'username': 'nabil', 'password': '123'}, follow = True)
        self.assertEqual(resp.status_code, 200)
        print('Test login exitoso')
        
    def test_logout(self):
        """
            Test para verificar si realiza el logout
        """  
        resp = self.client.get('/inicio/salir/')
        self.assertEqual(resp.status_code, 200)
        print('Test logout exitoso')