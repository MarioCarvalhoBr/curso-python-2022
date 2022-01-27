import unittest
from main import Retangulo, Circulo
class CirculoTeste(unittest.TestCase):
    def test_raio(self):
        cir = Circulo(10)
        valor_esperado = 10
        valor_retornado = cir.raio
        self.assertEqual(valor_esperado, valor_retornado, "Erro ao guardar o raio na classe Circulo")

class RetanguloTeste(unittest.TestCase):
    def setUp(self):
        self.ret = Retangulo(10.6,2)

    def test_area(self):
        rec1 = Retangulo(10, 5)
        valor_esperado = 50
        valor_real = rec1.area()
        self.assertEqual(valor_esperado , valor_real, "Erro na funcao area() da classe Retangulo() ")
    
    def test_perimetro(self):
        rec1 = Retangulo(10, 5)
        valor_esperado = 30
        valor_real = rec1.perimetro()
        self.assertEqual(valor_esperado , valor_real, "Erro na funcao perimetro() da classe Retangulo() ")
    
    def test_base(self):
        rec1 = Retangulo(10, 5)
        valor_esperado = 10
        valor_real = rec1.base
        self.assertEqual(valor_esperado , valor_real, "Erro ao acessar a base da classe Retangulo ")
    
    def test_valida(self):
        rec1 = Retangulo(0, 5)
        valor_real = rec1.valida()
        self.assertFalse(valor_real, "Erro ao acessar a funcao valida() da classe Retangulo ")
    
    def test_valida2(self):
        rec1 = Retangulo(10, 5)
        valor_real = rec1.valida()
        self.assertTrue(valor_real, "Erro ao acessar a funcao valida() da classe Retangulo ")
    
    def test_instancia(self):
        self.assertIsInstance(self.ret.base, float, msg=None)

unittest.main()