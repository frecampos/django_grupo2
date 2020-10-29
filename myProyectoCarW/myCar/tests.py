from django.test import TestCase
import unittest
from .models import Insumos
# Create your tests here.
class TestCadenas(unittest.TestCase):

    def test_iguales(self):        
        self.assertEquals('ii','ii')

    def test_distinto(self):
        self.assertFalse('hola' in 'este es un Hola mundo')

    def grabar(self):
        valor = 0
        try:
            insumo = Insumos(
                nombre="caja", 
                precio=100,
                descripcion="es grande"
                ,stock=1
            )
            insumo.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)
        
if __name__ =="__main__":
    unittest.main()