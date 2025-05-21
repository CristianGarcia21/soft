import unittest

from .restaurante import Restaurante


class PlatoMock:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class MenuMock:
    def __init__(self, platos):
        self._platos = {plato.nombre: plato for plato in platos}

    def obtener_plato(self, nombre_plato):
        return self._platos.get(nombre_plato, None)

class TestRestauranteAgregarPlatoAPedido(unittest.TestCase):
    def setUp(self):
        self.plato1 = PlatoMock("Taco", 50)
        self.plato2 = PlatoMock("Burrito", 80)
        self.menu = MenuMock([self.plato1, self.plato2])
        self.restaurante = Restaurante(self.menu)
        self.pedido = self.restaurante.crear_pedido()

    def test_agregar_plato_existente(self):
        resultado = self.restaurante.agregar_plato_a_pedido(self.pedido, "Taco")
        self.assertTrue(resultado)
        self.assertIn(self.plato1, self.pedido.platos)

    def test_agregar_plato_inexistente(self):
        resultado = self.restaurante.agregar_plato_a_pedido(self.pedido, "Pizza")
        self.assertFalse(resultado)
        self.assertEqual(len(self.pedido.platos), 0)

    def test_agregar_varios_platos(self):
        self.restaurante.agregar_plato_a_pedido(self.pedido, "Taco")
        self.restaurante.agregar_plato_a_pedido(self.pedido, "Burrito")
        self.assertIn(self.plato1, self.pedido.platos)
        self.assertIn(self.plato2, self.pedido.platos)
        self.assertEqual(len(self.pedido.platos), 2)

if __name__ == "__main__":
    unittest.main()