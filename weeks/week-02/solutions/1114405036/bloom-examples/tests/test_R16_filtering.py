import unittest
from itertools import compress

class TestFiltering(unittest.TestCase):
    def test_list_comprehension_basic(self):
        mylist = [1, 4, -5, 10]
        result = [n for n in mylist if n > 0]
        self.assertEqual(result, [1, 4, 10])
    
    def test_list_comprehension_even(self):
        mylist = [1, 2, 3, 4, 5, 6]
        result = [n for n in mylist if n % 2 == 0]
        self.assertEqual(result, [2, 4, 6])
    
    def test_generator_expression(self):
        mylist = [1, 4, -5, 10]
        pos = (n for n in mylist if n > 0)
        result = list(pos)
        self.assertEqual(result, [1, 4, 10])
    
    def test_generator_lazy(self):
        mylist = [1, 4, -5, 10]
        gen = (n for n in mylist if n > 0)
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 4)
        self.assertEqual(next(gen), 10)
    
    def test_filter_with_function(self):
        values = ['1', '2', '-3', '-', 'N/A']
        
        def is_int(val):
            try:
                int(val)
                return True
            except ValueError:
                return False
        
        result = list(filter(is_int, values))
        self.assertEqual(result, ['1', '2', '-3'])
    
    def test_filter_with_lambda(self):
        mylist = [1, 4, -5, 10]
        result = list(filter(lambda x: x > 0, mylist))
        self.assertEqual(result, [1, 4, 10])
    
    def test_compress_basic(self):
        addresses = ['a1', 'a2', 'a3']
        counts = [0, 3, 10]
        more5 = [n > 5 for n in counts]
        
        result = list(compress(addresses, more5))
        self.assertEqual(result, ['a3'])
    
    def test_compress_multiple_true(self):
        addresses = ['a1', 'a2', 'a3', 'a4']
        selectors = [True, False, True, False]
        result = list(compress(addresses, selectors))
        self.assertEqual(result, ['a1', 'a3'])
    
    def test_compress_all_true(self):
        data = [1, 2, 3]
        selectors = [True, True, True]
        result = list(compress(data, selectors))
        self.assertEqual(result, [1, 2, 3])
    
    def test_compress_all_false(self):
        data = [1, 2, 3]
        selectors = [False, False, False]
        result = list(compress(data, selectors))
        self.assertEqual(result, [])
    
    def test_filter_vs_comprehension_speed(self):
        mylist = list(range(1000))
        
        result1 = [x for x in mylist if x > 500]
        result2 = list(filter(lambda x: x > 500, mylist))
        
        self.assertEqual(result1, result2)
    
    def test_nested_comprehension(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = [x for row in matrix for x in row if x > 5]
        self.assertEqual(result, [6, 7, 8, 9])
    
    def test_set_comprehension(self):
        mylist = [1, 2, 2, 3, 3, 3]
        result = {x for x in mylist if x > 1}
        self.assertEqual(result, {2, 3})
    
    def test_dict_comprehension_filtering(self):
        prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}
        result = {k: v for k, v in prices.items() if v > 200}
        self.assertEqual(result, {'AAPL': 612.78, 'IBM': 205.55})
    
    def test_generator_memory_efficiency(self):
        # Generator uses less memory than list
        big_list = range(1000000)
        gen = (x for x in big_list if x > 999990)
        first = next(gen)
        self.assertEqual(first, 999991)

if __name__ == '__main__':
    unittest.main()
