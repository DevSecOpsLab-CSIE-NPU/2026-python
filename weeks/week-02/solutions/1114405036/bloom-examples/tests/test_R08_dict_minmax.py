import unittest

class TestDictMinMax(unittest.TestCase):
    def setUp(self):
        self.prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}
    def test_zip_values_keys(self):
        zipped = list(zip(self.prices.values(), self.prices.keys()))
        self.assertEqual(len(zipped), 3)
        self.assertIn((45.23, 'ACME'), zipped)
        self.assertIn((612.78, 'AAPL'), zipped)
        self.assertIn((10.75, 'FB'), zipped)
    def test_min_price_and_key(self):
        result = min(zip(self.prices.values(), self.prices.keys()))
        price, key = result
        self.assertEqual(price, 10.75)
        self.assertEqual(key, 'FB')
    def test_max_price_and_key(self):
        result = max(zip(self.prices.values(), self.prices.keys()))
        price, key = result
        self.assertEqual(price, 612.78)
        self.assertEqual(key, 'AAPL')
    def test_sorted_by_price(self):
        sorted_result = sorted(zip(self.prices.values(), self.prices.keys()))
        prices_only = [price for price, key in sorted_result]
        self.assertEqual(prices_only, [10.75, 45.23, 612.78])
        keys_only = [key for price, key in sorted_result]
        self.assertEqual(keys_only, ['FB', 'ACME', 'AAPL'])
    def test_min_key_by_value(self):
        result = min(self.prices, key=lambda k: self.prices[k])
        self.assertEqual(result, 'FB')
    def test_max_key_by_value(self):
        result = max(self.prices, key=lambda k: self.prices[k])
        self.assertEqual(result, 'AAPL')
    def test_sorted_keys_by_value(self):
        sorted_keys = sorted(self.prices, key=lambda k: self.prices[k])
        self.assertEqual(sorted_keys, ['FB', 'ACME', 'AAPL'])
    def test_empty_dict(self):
        empty = {}
        zipped = list(zip(empty.values(), empty.keys()))
        self.assertEqual(zipped, [])
    def test_single_entry(self):
        single = {'GOOG': 2800.50}
        result = min(zip(single.values(), single.keys()))
        self.assertEqual(result, (2800.50, 'GOOG'))
        result = max(zip(single.values(), single.keys()))
        self.assertEqual(result, (2800.50, 'GOOG'))
    def test_reverse_sort_by_price(self):
        sorted_result = sorted(zip(self.prices.values(), self.prices.keys()), reverse=True)
        prices_only = [price for price, key in sorted_result]
        self.assertEqual(prices_only, [612.78, 45.23, 10.75])
    def test_zip_different_structures(self):
        values = [1, 2, 3]
        keys = ['a', 'b']
        zipped = list(zip(values, keys))
        self.assertEqual(zipped, [(1, 'a'), (2, 'b')])
    def test_dict_comprehension_from_zip(self):
        zipped = zip(self.prices.values(), self.prices.keys())
        new_dict = {key: price for price, key in zipped}
        self.assertEqual(new_dict['ACME'], 45.23)
        self.assertEqual(new_dict['AAPL'], 612.78)

if __name__ == '__main__':
    unittest.main()