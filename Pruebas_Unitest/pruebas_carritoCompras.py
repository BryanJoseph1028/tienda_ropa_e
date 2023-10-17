import unittest

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        return sum(item['price'] for item in self.items)

class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        # Se ejecuta antes de cada prueba
        self.cart = ShoppingCart()
        self.item1 = {'name': 'Camiseta', 'price': 20}
        self.item2 = {'name': 'Pantalón', 'price': 30}

    def test_add_item(self):
        self.cart.add_item(self.item1)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0], self.item1)

    def test_remove_item(self):
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)

        self.cart.remove_item(self.item1)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0], self.item2)

    def test_calculate_total(self):
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)

        total = self.cart.calculate_total()
        self.assertEqual(total, 50)

if __name__ == '__main__':
    unittest.main()