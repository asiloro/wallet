import unittest
from carteiropy import calculadora


class TestSum(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calculadora.soma(2,8), 11, "O teste falhou, a soma dos dois numeros não resula em 11")
