import unittest

class Sale:
    def __init__(self, product, quantity, total_price):
        self.product = product
        self.quantity = quantity
        self.total_price = total_price

class SalesManager:
    def __init__(self):
        self.sales = []

    def make_sale(self, sale):
        self.sales.append(sale)

    def calculate_total_sales(self):
        return sum(sale.total_price for sale in self.sales)

class SalesManagerTest(unittest.TestCase):
    def setUp(self):
        # Se ejecuta antes de cada prueba
        self.sales_manager = SalesManager()
        self.product1 = {'name': 'Camiseta', 'price': 20}
        self.product2 = {'name': 'Pantalón', 'price': 30}
        self.sale1 = Sale(self.product1, 2, 40)
        self.sale2 = Sale(self.product2, 1, 30)

    def test_make_sale(self):
        self.sales_manager.make_sale(self.sale1)
        self.assertEqual(len(self.sales_manager.sales), 1)
        self.assertEqual(self.sales_manager.sales[0], self.sale1)

    def test_calculate_total_sales(self):
        self.sales_manager.make_sale(self.sale1)
        self.sales_manager.make_sale(self.sale2)
        total_sales = self.sales_manager.calculate_total_sales()
        self.assertEqual(total_sales, 70)

if __name__ == '__main__':
    unittest.main()