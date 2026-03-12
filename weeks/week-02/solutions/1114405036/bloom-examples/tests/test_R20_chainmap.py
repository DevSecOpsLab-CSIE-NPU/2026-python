import unittest
from collections import ChainMap

class TestChainMap(unittest.TestCase):
    def setUp(self):
        self.a = {'x': 1, 'z': 3}
        self.b = {'y': 2, 'z': 4}
        self.c = ChainMap(self.a, self.b)
    
    def test_chainmap_access_first_dict(self):
        self.assertEqual(self.c['x'], 1)
    
    def test_chainmap_access_second_dict(self):
        self.assertEqual(self.c['y'], 2)
    
    def test_chainmap_priority_first_dict(self):
        self.assertEqual(self.c['z'], 3)
    
    def test_chainmap_update_affects_first_dict(self):
        self.c['x'] = 10
        self.assertEqual(self.a['x'], 10)
        self.assertEqual(self.c['x'], 10)
    
    def test_chainmap_new_key(self):
        self.c['w'] = 5
        self.assertIn('w', self.a)
        self.assertEqual(self.c['w'], 5)
    
    def test_chainmap_keys(self):
        keys = set(self.c.keys())
        expected = {'x', 'y', 'z'}
        self.assertEqual(keys, expected)
    
    def test_chainmap_values(self):
        values = list(self.c.values())
        self.assertIn(1, values)
        self.assertIn(2, values)
        self.assertIn(3, values)
    
    def test_chainmap_items(self):
        items = dict(self.c.items())
        self.assertEqual(items['x'], 1)
        self.assertEqual(items['y'], 2)
        self.assertEqual(items['z'], 3)
    
    def test_chainmap_maps_attribute(self):
        self.assertEqual(len(self.c.maps), 2)
        self.assertIs(self.c.maps[0], self.a)
        self.assertIs(self.c.maps[1], self.b)
    
    def test_chainmap_missing_key(self):
        with self.assertRaises(KeyError):
            self.c['missing']
    
    def test_chainmap_get_with_default(self):
        result = self.c.get('missing', 'default')
        self.assertEqual(result, 'default')
    
    def test_chainmap_three_dicts(self):
        d1 = {'a': 1}
        d2 = {'b': 2}
        d3 = {'c': 3}
        cm = ChainMap(d1, d2, d3)
        
        self.assertEqual(cm['a'], 1)
        self.assertEqual(cm['b'], 2)
        self.assertEqual(cm['c'], 3)
    
    def test_chainmap_priority_order(self):
        d1 = {'x': 1, 'y': 2}
        d2 = {'x': 10, 'z': 3}
        cm = ChainMap(d1, d2)
        
        self.assertEqual(cm['x'], 1)
        self.assertEqual(cm['y'], 2)
        self.assertEqual(cm['z'], 3)
    
    def test_chainmap_parent_changes_visible(self):
        self.b['y'] = 20
        self.assertEqual(self.c['y'], 20)
    
    def test_chainmap_new_in_first_dict(self):
        self.a['new_key'] = 100
        self.assertEqual(self.c['new_key'], 100)
    
    def test_chainmap_delete(self):
        del self.c['x']
        self.assertNotIn('x', self.a)
        with self.assertRaises(KeyError):
            self.c['x']

if __name__ == '__main__':
    unittest.main()
