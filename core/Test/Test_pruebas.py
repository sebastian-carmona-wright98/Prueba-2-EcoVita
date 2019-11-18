from django.test import TestCase
from django.db import models

# Create your tests here.
class test_prueba(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: ejecutar los datos, en cuales no se deben modificar.")
        pass

    def setUp(self):
        print("setUp: el funcionamiento, si que las prueba se logran con exito.")
        pass

    def test_falso_is_false(self):
        print("Methodo: la prueba si es falsa.")
        self.assertFalse(False)

    def test_falso_is_false(self):
        print("Method0: la prueba si es verdadera.")
        self.assertTrue(False)

    def test_si_funciona(self):
        print("Methodo: la prueba si que el metodo se mantiene con los datos u/o se detiene.")
        self.assertEqual(self.Nombre == 'jose humito', self.Direccion =='avenida 5 de abril #32112', self.Telefono == '9834937847', self.Mail == 'joset77@hotmail.com')
