#Pruebas Librería computación Cuántica: Números complejos
#Sara Sofia Gonzalez Mora

import unittest
import math
from libreria import *  

class TestLibreria(unittest.TestCase):
    
    def test_sumar_basico(self):
        self.assertEqual(sumar((1,2), (3,4)), (4,6))
    def test_sumar_cero(self):
        self.assertEqual(sumar((0,0), (5,0)), (5,0))
    
    def test_restar_basico(self):
        self.assertEqual(restar((3,4), (1,2)), (2,2))
    def test_restar_cero(self):
        self.assertEqual(restar((5,5), (5,5)), (0,0))
    
    def test_producto_basico(self):
        self.assertEqual(producto((1,2), (3,4)), (-5,10))
    def test_producto_i(self):
        self.assertEqual(producto((0,1), (0,1)), (-1,0))  # i * i = -1
    
    def test_division_basica(self):
        resultado = division((1,2), (3,4))
        self.assertAlmostEqual(resultado[0], -0.2, places=1)
        self.assertAlmostEqual(resultado[1], 1.4, places=1)
    def test_division_uno(self):
        self.assertAlmostEqual(division((3,4), (3,4))[0], 1.0)
    
    def test_modulo_clasico(self):
        self.assertAlmostEqual(modulo((3,4)), 5.0)
    def test_modulo_cero(self):
        self.assertEqual(modulo((0,0)), 0.0)
    
    def test_conjugado_basico(self):
        self.assertEqual(conjugado((3,4)), (3,-4))
    def test_conjugado_real(self):
        self.assertEqual(conjugado((5,0)), (5,0))
    
    def test_cartesiano_polar_clasico(self):
        mod, fase = cartesiano_a_polar((3,4))
        self.assertAlmostEqual(mod, 5.0)
        self.assertAlmostEqual(fase, 0.927, places=3)
    def test_cartesiano_polar_cero(self):
        self.assertEqual(cartesiano_a_polar((0,0)), (0.0, 0.0))
    
    def test_polar_cartesiano(self):
        resultado = polar_a_cartesiano((5, 0.927))
        self.assertAlmostEqual(resultado[0], 3.0, places=1)
        self.assertAlmostEqual(resultado[1], 4.0, places=1)
    def test_polar_cartesiano_cero(self):
        self.assertEqual(polar_a_cartesiano((0,0)), (0.0, 0.0))
    
    def test_fase(self):
        self.assertAlmostEqual(fase((3,4)), 0.927, places=3)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
