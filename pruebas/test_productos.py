import unittest
import models.funciones as Funciones
from models.ingredientes import Ingredientes
from models.productos import Productos
from models.heladeria import Heladeria

class TestProductos(unittest.TestCase):

    def test_calcular_calorias_copa(self):
        ingrediente1 = Ingredientes("CHOCOLATE", 5000, 90, False, 7, "DULCE")
        ingrediente2 = Ingredientes("MANI", 10000, 100, False, 8, "NEUTRO")
        lista_ingredientes = [ingrediente1, ingrediente2]
        copa = Productos("COPA", 50000, "1", 2, lista_ingredientes)
        resultado = copa.calcular_calorias()
        self.assertEqual(resultado,  285.0)

    def test_contar_calorias_malteada(self):
        ingrediente1 = Ingredientes("CHOCOLATE", 5000, 90, False, 7, "DULCE")
        ingrediente2 = Ingredientes("MANI", 10000, 100, False, 8, "NEUTRO")
        lista_ingredientes = [ingrediente1, ingrediente2]
        malteada = Productos("COPA", 50000, "1", 2, lista_ingredientes)
        resultado = malteada.calcular_calorias()
        self.assertEqual(resultado,  500)

    def test_calcular_costo_producto(self):
        ingrediente1 = Ingredientes("CHOCOLATE", 5000, 90, False, 7, "DULCE")
        ingrediente2 = Ingredientes("MANI", 10000, 100, False, 8, "NEUTRO")
        lista_ingredientes = [ingrediente1, ingrediente2]
        copa = Productos("COPA", 50000, "1", 2, lista_ingredientes)
        resultado = copa.calcular_costo()
        self.assertEqual(resultado,  2500.0)

    def test_calcular_rentabilidad(self):
        ingrediente1 = Ingredientes("CHOCOLATE", 5000, 90, False, 7, "DULCE")
        ingrediente2 = Ingredientes("MANI", 10000, 100, False, 8, "NEUTRO")
        lista_ingredientes = [ingrediente1, ingrediente2]
        copa = Productos("COPA", 50000, "1", 2, lista_ingredientes)
        resultado = copa.calcular_rentabilidad()
        self.assertEqual(resultado, 5000.0)