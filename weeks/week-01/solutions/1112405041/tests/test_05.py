import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ?®å?æ¸¬è©¦ï¼šä¸»é¡?05ï¼ˆç´¢å¼•è??‡ç?ï¼?

import unittest
import importlib

# ?•æ?å°Žå…¥ 05_formal æ¨¡ç?
formal_05 = importlib.import_module('05_hand')
string_indexing = formal_05.string_indexing
list_slicing = formal_05.list_slicing

class TestIndexingSlicing(unittest.TestCase):
    
    def test_string_indexing(self):
        """æ¸¬è©¦å­—ä¸²ç´¢å?"""
        result = string_indexing()
        self.assertEqual(result['first'], 'a')
        self.assertEqual(result['last'], 'g')
        self.assertEqual(result['mid'], 'cde')
    
    def test_list_slicing(self):
        """æ¸¬è©¦ list ?‡ç?"""
        result = list_slicing()
        self.assertEqual(result['last_two'], [40, 50])
        self.assertEqual(result['first_three'], [10, 20, 30])
        self.assertEqual(result['every_other'], [10, 30, 50])
    
    def test_negative_index(self):
        """æ¸¬è©¦è² ç´¢å¼?""
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(lst[-1], 5)
        self.assertEqual(lst[-2], 4)

if __name__ == '__main__':
    unittest.main()
