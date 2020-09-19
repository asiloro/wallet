import unittest
from carteiropy import calculadora


class TestSum(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calculadora.soma(2,6), 8, "Should be 8")
        self.assertEqual(calculadora.soma(3,8), 11, "Should be 11")
