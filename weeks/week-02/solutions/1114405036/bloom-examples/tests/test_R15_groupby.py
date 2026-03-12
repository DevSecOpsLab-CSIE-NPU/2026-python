import unittest
from itertools import groupby
from operator import itemgetter

class TestGroupBy(unittest.TestCase):
    def test_groupby_basic(self):
        rows = [
            {'date': '07/01/2012', 'address': 'NYC'},
            {'date': '07/01/2012', 'address': 'SF'},
            {'date': '07/02/2012', 'address': 'LA'},
            {'date': '07/02/2012', 'address': 'Boston'}
        ]
        rows.sort(key=itemgetter('date'))
        
        groups = {}
        for date, items in groupby(rows, key=itemgetter('date')):
            groups[date] = list(items)
        
        self.assertEqual(len(groups), 2)
        self.assertEqual(len(groups['07/01/2012']), 2)
        self.assertEqual(len(groups['07/02/2012']), 2)
    
    def test_groupby_count_items_per_group(self):
        data = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
        result = {k: len(list(g)) for k, g in groupby(data)}
        
        self.assertEqual(result['a'], 2)
        self.assertEqual(result['b'], 2)
        self.assertEqual(result['c'], 3)
    
    def test_groupby_consecutive_items(self):
        data = [1, 1, 1, 2, 2, 3, 3, 3, 3]
        groups = []
        for k, g in groupby(data):
            groups.append((k, list(g)))
        
        self.assertEqual(len(groups), 3)
        self.assertEqual(groups[0], (1, [1, 1, 1]))
        self.assertEqual(groups[1], (2, [2, 2]))
        self.assertEqual(groups[2], (3, [3, 3, 3, 3]))
    
    def test_groupby_with_key_function(self):
        words = ['apple', 'apricot', 'banana', 'berry', 'cherry']
        result = {}
        for letter, group in groupby(words, key=lambda x: x[0]):
            result[letter] = list(group)
        
        self.assertEqual(len(result['a']), 2)
        self.assertEqual(len(result['b']), 2)
        self.assertEqual(len(result['c']), 1)
    
    def test_groupby_not_presorted(self):
        data = [1, 2, 1, 2, 1]
        groups = {}
        for k, g in groupby(data):
            if k not in groups:
                groups[k] = []
            groups[k].extend(list(g))
        
        # Without sorting, consecutive check fails
        self.assertEqual(len(groups[1]), 3)
        self.assertEqual(len(groups[2]), 2)
    
    def test_groupby_dict_list(self):
        rows = [
            {'category': 'A', 'value': 1},
            {'category': 'A', 'value': 2},
            {'category': 'B', 'value': 3},
            {'category': 'B', 'value': 4}
        ]
        
        result = {}
        for cat, items in groupby(rows, key=itemgetter('category')):
            result[cat] = [item['value'] for item in items]
        
        self.assertEqual(result['A'], [1, 2])
        self.assertEqual(result['B'], [3, 4])
    
    def test_groupby_sum_values(self):
        data = [1, 1, 2, 2, 2, 3, 3]
        result = {k: sum(g) for k, g in groupby(data)}
        
        self.assertEqual(result[1], 2)
        self.assertEqual(result[2], 6)
        self.assertEqual(result[3], 6)
    
    def test_groupby_strings_by_length(self):
        words = ['a', 'aa', 'bb', 'cc', 'ddd', 'eee']
        words.sort(key=len)
        
        result = {}
        for length, group in groupby(words, key=len):
            result[length] = list(group)
        
        self.assertEqual(result[1], ['a'])
        self.assertEqual(result[2], ['aa', 'bb', 'cc'])
        self.assertEqual(result[3], ['ddd', 'eee'])
    
    def test_groupby_preserves_order(self):
        data = ['a', 'a', 'b', 'b', 'a', 'a']
        keys = [k for k, g in groupby(data)]
        
        self.assertEqual(keys, ['a', 'b', 'a'])
    
    def test_groupby_empty_list(self):
        result = list(groupby([]))
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
