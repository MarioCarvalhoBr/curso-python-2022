import unittest
from main import Retangulo

class RetanguloTeste(unittest.TestCase):
    def setUp(self):
        self.ret = Retangulo(0,0)
    def test_valida(self):
        ret3 = Retangulo(0,0)

        self.assertEqual(False, ret3.valida(), "Erro na função de validar o retângulo")
        self.assertEqual(ret3.valida(), self.ret.valida(), "Erro na função de validar o retângulo")
    
    def test_area(self):
        ret3 = Retangulo(10,10)
        self.assertEqual(100, ret3.area(), "Erro na função de calcular a área area")
    
    def test_base(self):
        ret3 = Retangulo(30,10)
        self.assertEqual(30, ret3.base, "Classe Retangulo.py não está armazendo corretamente o valor da base")

    def test_altura(self):
        ret3 = Retangulo(30,10)
        self.assertEqual(10, ret3.altura, "Classe Retangulo.py não está armazendo corretamente o valor da altura")
    
    def test_instancia(self):
        rect = Retangulo(10, 10)

        self.assertIsInstance(rect, Retangulo, msg="Erro na instancia do objeto da classe Retangulo")
    def test_testaLista(self):
        rec1 = Retangulo(10, 10)
        rec2 = Retangulo(30, 10)
        lista1 = [rec1, rec2]
        lista2 = [rec1, rec2]
        self.assertListEqual(lista1, lista2, "Erro nas listas")
if __name__ == "__main__":
    unittest.main()