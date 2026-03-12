"""
測試 R07: OrderedDict
驗證 OrderedDict 的有序性和 JSON 序列化
"""

import unittest
from collections import OrderedDict
import json


class TestOrderedDict(unittest.TestCase):
    """OrderedDict 功能測試"""
    
    def setUp(self):
        """設定測試用的字典"""
        self.d = OrderedDict()
    
    def test_insertion_order_preserved(self):
        """測試插入順序保留"""
        self.d['foo'] = 1
        self.d['bar'] = 2
        self.d['baz'] = 3
        
        keys = list(self.d.keys())
        self.assertEqual(keys, ['foo', 'bar', 'baz'])
    
    def test_access_order_unchanged(self):
        """測試訪問不改變順序"""
        self.d['first'] = 1
        self.d['second'] = 2
        
        # 訪問 first
        _ = self.d['first']
        
        keys = list(self.d.keys())
        self.assertEqual(keys, ['first', 'second'])
    
    def test_json_serialization(self):
        """測試 JSON 序列化"""
        self.d['foo'] = 1
        self.d['bar'] = 2
        
        json_str = json.dumps(self.d)
        # JSON 應該按順序序列化
        self.assertEqual(json_str, '{"foo": 1, "bar": 2}')
    
    def test_json_deserialization(self):
        """測試 JSON 反序列化"""
        json_str = '{"foo": 1, "bar": 2}'
        d = json.loads(json_str, object_pairs_hook=OrderedDict)
        
        keys = list(d.keys())
        self.assertEqual(keys, ['foo', 'bar'])
    
    def test_equality_with_dict(self):
        """測試 OrderedDict 與 dict 的相等性"""
        d = {'a': 1, 'b': 2}
        od = OrderedDict([('a', 1), ('b', 2)])
        
        # 內容相同
        self.assertEqual(dict(od), d)
    
    def test_ordering_differs_from_dict(self):
        """測試 OrderedDict 保留順序，普通 dict 不一定"""
        od = OrderedDict()
        od['z'] = 26
        od['a'] = 1
        od['m'] = 13
        
        od_keys = list(od.keys())
        self.assertEqual(od_keys, ['z', 'a', 'm'])
    
    def test_pop_preserves_order(self):
        """測試 pop 後保留原始順序"""
        self.d['a'] = 1
        self.d['b'] = 2
        self.d['c'] = 3
        
        self.d.pop('b')
        
        keys = list(self.d.keys())
        self.assertEqual(keys, ['a', 'c'])
    
    def test_multiple_operations(self):
        """測試多個操作"""
        self.d['first'] = 1
        self.d['second'] = 2
        self.d['third'] = 3
        
        self.d['second'] = 20  # 修改值，順序不變
        self.d['fourth'] = 4   # 新增
        
        keys = list(self.d.keys())
        values = list(self.d.values())
        
        self.assertEqual(keys, ['first', 'second', 'third', 'fourth'])
        self.assertEqual(values, [1, 20, 3, 4])
    
    def test_clear_and_reinitialize(self):
        """測試清空和重新初始化"""
        self.d['a'] = 1
        self.d['b'] = 2
        
        self.d.clear()
        self.d['x'] = 10
        
        self.assertEqual(list(self.d.items()), [('x', 10)])
    
    def test_move_to_end(self):
        """測試 move_to_end 方法"""
        self.d['a'] = 1
        self.d['b'] = 2
        self.d['c'] = 3
        
        self.d.move_to_end('a')
        
        keys = list(self.d.keys())
        self.assertEqual(keys, ['b', 'c', 'a'])


if __name__ == '__main__':
    unittest.main()
