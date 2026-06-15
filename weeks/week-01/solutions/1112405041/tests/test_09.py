import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ?®å?æ¸¬è©¦ï¼šä¸»é¡?09ï¼ˆæ?è¼ƒã€æ?åºè? key ?½å?ï¼?

import unittest
import sys
import importlib

# ?•æ?å°å…¥ 09_formal æ¨¡ç?
formal_09 = importlib.import_module('09_hand')
sort_by_uid = formal_09.sort_by_uid
find_min_max_by_key = formal_09.find_min_max_by_key
sort_tuples = formal_09.sort_tuples
sort_descending = formal_09.sort_descending
tuple_comparison = formal_09.tuple_comparison

class TestSortingComparison(unittest.TestCase):
    
    def test_sort_by_uid(self):
        """æ¸¬è©¦?¹æ? uid ?’å?"""
        rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
        result = sort_by_uid(rows)
        self.assertEqual(result[0]['uid'], 1)
        self.assertEqual(result[2]['uid'], 3)
    
    def test_find_min_max(self):
        """æ¸¬è©¦?¾æ?å°å??€å¤§å€?""
        rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
        result = find_min_max_by_key(rows, 'uid')
        self.assertEqual(result['min']['uid'], 1)
        self.assertEqual(result['max']['uid'], 3)
    
    def test_sort_descending(self):
        """æ¸¬è©¦?å??’å?"""
        result = sort_descending([3, 1, 4, 1, 5])
        self.assertEqual(result, [5, 4, 3, 1, 1])
    
    def test_tuple_comparison(self):
        """æ¸¬è©¦ tuple æ¯”è?"""
        result = tuple_comparison()
        self.assertTrue(result['a_less_than_b'])
        self.assertTrue(result['x_less_than_y'])

if __name__ == '__main__':
    unittest.main()
