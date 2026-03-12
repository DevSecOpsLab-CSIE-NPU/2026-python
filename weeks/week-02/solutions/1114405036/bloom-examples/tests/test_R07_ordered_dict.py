import unittest
from collections import OrderedDict
import json

class TestOrderedDict(unittest.TestCase):
    def setUp(self):
        self.d = OrderedDict()
    def test_insertion_order_preserved(self):
        self.d['foo'] = 1
        self.d['bar'] = 2
        self.d['baz'] = 3
        keys = list(self.d.keys())
        self.assertEqual(keys, ['foo', 'bar', 'baz'])
    def test_access_order_unchanged(self):
        self.d['first'] = 1
        self.d['second'] = 2
        _ = self.d['first']
        keys = list(self.d.keys())
        self.assertEqual(keys, ['first', 'second'])
    def test_json_serialization(self):
        self.d['foo'] = 1
        self.d['bar'] = 2
        json_str = json.dumps(self.d)
        self.assertEqual(json_str, '{"foo": 1, "bar": 2}')
    def test_json_deserialization(self):
        json_str = '{"foo": 1, "bar": 2}'
        d = json.loads(json_str, object_pairs_hook=OrderedDict)
        keys = list(d.keys())
        self.assertEqual(keys, ['foo', 'bar'])
    def test_equality_with_dict(self):
        d = {'a': 1, 'b': 2}
        od = OrderedDict([('a', 1), ('b', 2)])
        self.assertEqual(dict(od), d)
    def test_ordering_differs_from_dict(self):
        od = OrderedDict()
        od['z'] = 26
        od['a'] = 1
        od['m'] = 13
        od_keys = list(od.keys())
        self.assertEqual(od_keys, ['z', 'a', 'm'])
    def test_pop_preserves_order(self):
        self.d['a'] = 1
        self.d['b'] = 2
        self.d['c'] = 3
        self.d.pop('b')
        keys = list(self.d.keys())
        self.assertEqual(keys, ['a', 'c'])
    def test_multiple_operations(self):
        self.d['first'] = 1
        self.d['second'] = 2
        self.d['third'] = 3
        self.d['second'] = 20
        self.d['fourth'] = 4
        keys = list(self.d.keys())
        values = list(self.d.values())
        self.assertEqual(keys, ['first', 'second', 'third', 'fourth'])
        self.assertEqual(values, [1, 20, 3, 4])
    def test_clear_and_reinitialize(self):
        self.d['a'] = 1
        self.d['b'] = 2
        self.d.clear()
        self.d['x'] = 10
        self.assertEqual(list(self.d.items()), [('x', 10)])
    def test_move_to_end(self):
        self.d['a'] = 1
        self.d['b'] = 2
        self.d['c'] = 3
        self.d.move_to_end('a')
        keys = list(self.d.keys())
        self.assertEqual(keys, ['b', 'c', 'a'])

if __name__ == '__main__':
    unittest.main()