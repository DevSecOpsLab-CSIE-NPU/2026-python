import unittest

class TestGeneratorAggregate(unittest.TestCase):
    def test_sum_with_generator(self):
        nums = [1, 2, 3]
        result = sum(x * x for x in nums)
        self.assertEqual(result, 14)
    
    def test_max_with_generator(self):
        nums = [1, 2, 3, 4, 5]
        result = max(x * 2 for x in nums)
        self.assertEqual(result, 10)
    
    def test_min_with_generator(self):
        nums = [1, 2, 3, 4, 5]
        result = min(x * 2 for x in nums)
        self.assertEqual(result, 2)
    
    def test_join_with_generator(self):
        s = ('ACME', 50, 123.45)
        result = ','.join(str(x) for x in s)
        self.assertEqual(result, 'ACME,50,123.45')
    
    def test_list_with_generator(self):
        nums = [1, 2, 3]
        result = list(x * x for x in nums)
        self.assertEqual(result, [1, 4, 9])
    
    def test_set_with_generator(self):
        nums = [1, 2, 2, 3, 3, 3]
        result = set(x * 2 for x in nums)
        self.assertEqual(result, {2, 4, 6})
    
    def test_dict_with_generator(self):
        nums = [1, 2, 3]
        result = {x: x * x for x in nums}
        self.assertEqual(result, {1: 1, 2: 4, 3: 9})
    
    def test_any_with_generator(self):
        nums = [0, 0, 1, 0]
        result = any(x > 0 for x in nums)
        self.assertTrue(result)
    
    def test_all_with_generator(self):
        nums = [1, 2, 3, 4]
        result = all(x > 0 for x in nums)
        self.assertTrue(result)
    
    def test_all_with_generator_false(self):
        nums = [1, 2, 0, 4]
        result = all(x > 0 for x in nums)
        self.assertFalse(result)
    
    def test_min_portfolio_shares(self):
        portfolio = [
            {'name': 'AOL', 'shares': 20},
            {'name': 'YHOO', 'shares': 75},
            {'name': 'GOOG', 'shares': 50}
        ]
        min_shares = min(s['shares'] for s in portfolio)
        self.assertEqual(min_shares, 20)
    
    def test_min_portfolio_with_min_function(self):
        portfolio = [
            {'name': 'AOL', 'shares': 20},
            {'name': 'YHOO', 'shares': 75},
            {'name': 'GOOG', 'shares': 50}
        ]
        min_item = min(portfolio, key=lambda s: s['shares'])
        self.assertEqual(min_item['name'], 'AOL')
        self.assertEqual(min_item['shares'], 20)
    
    def test_max_with_generator_on_portfolio(self):
        portfolio = [
            {'name': 'AOL', 'shares': 20},
            {'name': 'YHOO', 'shares': 75},
            {'name': 'GOOG', 'shares': 50}
        ]
        max_shares = max(s['shares'] for s in portfolio)
        self.assertEqual(max_shares, 75)
    
    def test_sum_nested_generator(self):
        matrix = [[1, 2, 3], [4, 5], [6]]
        total = sum(x for row in matrix for x in row)
        self.assertEqual(total, 21)
    
    def test_generator_memory_efficient_large_sum(self):
        # Generator doesn't create intermediate list
        result = sum(x for x in range(1000000) if x % 2 == 0)
        expected = sum(x for x in range(1000000) if x % 2 == 0)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
