import unittest
from carteiropy import calculadora


class TestSum(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calculadora.soma(3,8), 21, "Should be 11")
