import unittest
from task1_prerequisites import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.p1 = Product("Laptop", 1200.0, [5, 3, 2])
        self.p2 = Product("Mouse", 25.5, [50, 20, 30])

    def test_total_stock(self):
        # 測試總庫存計算 (Topic 08: sum with generator)
        self.assertEqual(self.p1.total_stock, 10)
        self.assertEqual(self.p2.total_stock, 100)

    def test_stock_value(self):
        # 測試庫存價值計算
        self.assertEqual(self.p1.stock_value, 12000.0)
        self.assertEqual(self.p2.stock_value, 2550.0)

    def test_sorting(self):
        # 測試排序邏輯 (Topic 09)
        products = [self.p1, self.p2]
        sorted_products = sorted(products, key=lambda x: x.stock_value, reverse=True)
        self.assertEqual(sorted_products[0].name, "Laptop")

    def test_filtering(self):
        # 測試過濾邏輯 (Topic 08)
        products = [self.p1, self.p2]
        low_stock = [p.name for p in products if p.total_stock < 20]
        self.assertIn("Laptop", low_stock)
        self.assertNotIn("Mouse", low_stock)

if __name__ == "__main__":
    unittest.main()
