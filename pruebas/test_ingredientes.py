import unittest
import models.funciones as Funciones
from models.ingredientes import Ingredientes


class TestIngredientes(unittest.TestCase):

    def test_ingrediente_es_sano(self):
        ingrediente = Ingredientes("CHOCOLATE", 5000, 90, False, 7, "DULCE")
        resultado = Funciones.ingrediente_es_sano(ingrediente.calorias, ingrediente.es_vegetariano)
        self.assertEqual(resultado, True)

    def test_abastecer_ingrediente(self):
        inventario = 10
        ingrediente = Ingredientes("CHOCOLATE", 5000, 90, False, 7, "DULCE")
        resultado = ingrediente.inventario
        self.assertEqual(resultado, inventario)

    def test_renovar_complemento(self):
        inventario = 10
        ingrediente = Ingredientes("CHOCOLATE", 5000, 90, False, 7, "DULCE")
        resultado = ingrediente.inventario
        self.assertEqual(resultado, inventario)