import unittest

class TestDictSubset(unittest.TestCase):
    def setUp(self):
        self.prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}
        self.tech_names = {'AAPL', 'IBM'}
    
    def test_dict_comprehension_value_filter(self):
        p1 = {k: v for k, v in self.prices.items() if v > 200}
        self.assertEqual(p1, {'AAPL': 612.78, 'IBM': 205.55})
    
    def test_dict_comprehension_key_filter(self):
        p2 = {k: v for k, v in self.prices.items() if k in self.tech_names}
        self.assertEqual(p2, {'AAPL': 612.78, 'IBM': 205.55})
    
    def test_dict_subset_low_values(self):
        result = {k: v for k, v in self.prices.items() if v < 100}
        self.assertEqual(result, {'ACME': 45.23})
    
    def test_dict_subset_exact_value(self):
        prices = {'a': 100, 'b': 200, 'c': 100}
        result = {k: v for k, v in prices.items() if v == 100}
        self.assertEqual(result, {'a': 100, 'c': 100})
    
    def test_dict_subset_multiple_conditions(self):
        data = {'x': 10, 'y': 20, 'z': 30, 'w': 5}
        result = {k: v for k, v in data.items() if v > 10 and k != 'z'}
        self.assertEqual(result, {'y': 20})
    
    def test_dict_subset_key_list(self):
        keep_keys = ['AAPL', 'IBM']
        result = {k: v for k, v in self.prices.items() if k in keep_keys}
        self.assertEqual(result, {'AAPL': 612.78, 'IBM': 205.55})
    
    def test_dict_subset_exclude_keys(self):
        exclude = {'ACME'}
        result = {k: v for k, v in self.prices.items() if k not in exclude}
        self.assertEqual(result, {'AAPL': 612.78, 'IBM': 205.55})
    
    def test_dict_subset_empty_result(self):
        result = {k: v for k, v in self.prices.items() if v > 1000}
        self.assertEqual(result, {})
    
    def test_dict_subset_all_match(self):
        result = {k: v for k, v in self.prices.items() if v > 0}
        self.assertEqual(result, self.prices)
    
    def test_dict_subset_string_values(self):
        data = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
        result = {k: v for k, v in data.items() if len(v) > 5}
        self.assertEqual(result, {'b': 'banana', 'c': 'cherry'})
    
    def test_dict_subset_value_transformation(self):
        data = {'x': 10, 'y': 20, 'z': 30}
        result = {k: v * 2 for k, v in data.items() if v > 15}
        self.assertEqual(result, {'y': 40, 'z': 60})
    
    def test_dict_subset_using_keys_method(self):
        exclude = {'ACME', 'AAPL'}
        result = {k: self.prices[k] for k in self.prices.keys() - exclude}
        self.assertEqual(result, {'IBM': 205.55})

if __name__ == '__main__':
    unittest.main()
