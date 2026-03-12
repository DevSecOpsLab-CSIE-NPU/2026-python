import unittest

class TestDictSets(unittest.TestCase):
    def setUp(self):
        self.a = {'x': 1, 'y': 2, 'z': 3}
        self.b = {'w': 10, 'x': 11, 'y': 2}
    
    def test_common_keys(self):
        common = self.a.keys() & self.b.keys()
        self.assertEqual(common, {'x', 'y'})
    
    def test_keys_difference(self):
        diff = self.a.keys() - self.b.keys()
        self.assertEqual(diff, {'z'})
    
    def test_keys_difference_other_way(self):
        diff = self.b.keys() - self.a.keys()
        self.assertEqual(diff, {'w'})
    
    def test_common_items(self):
        common = self.a.items() & self.b.items()
        self.assertEqual(common, {('y', 2)})
    
    def test_dict_comprehension_exclude_keys(self):
        c = {k: self.a[k] for k in self.a.keys() - {'z', 'w'}}
        self.assertEqual(c, {'x': 1, 'y': 2})
    
    def test_empty_keys_intersection(self):
        d = {'p': 100}
        common = self.a.keys() & d.keys()
        self.assertEqual(common, set())
    
    def test_keys_union(self):
        union = self.a.keys() | self.b.keys()
        self.assertEqual(union, {'x', 'y', 'z', 'w'})
    
    def test_symmetric_difference(self):
        sym_diff = self.a.keys() ^ self.b.keys()
        self.assertEqual(sym_diff, {'z', 'w'})
    
    def test_subset_check(self):
        small = {'x', 'y'}
        self.assertTrue(small <= self.a.keys())
    
    def test_superset_check(self):
        large = {'x', 'y', 'z', 'w'}
        self.assertTrue(large >= self.a.keys())

if __name__ == '__main__':
    unittest.main()
