import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ?®å?æ¸¬è©¦ï¼šä¸»é¡?03ï¼ˆåŸº?¬å®¹?¨å??¥ï?

import unittest
import importlib

# ?•æ?å°å…¥ 03_formal æ¨¡ç?
formal_03 = importlib.import_module('03_hand')
manage_containers = formal_03.manage_containers

class TestContainers(unittest.TestCase):
    
    def test_manage_containers(self):
        """æ¸¬è©¦å®¹å™¨?ä?"""
        result = manage_containers()
        self.assertIn(4, result['list'])
        self.assertEqual(result['tuple'], (4, 5))
        self.assertIn(4, result['set'])
        self.assertIn('GOOGL', result['dict'])
    
    def test_list_append(self):
        """æ¸¬è©¦ list ?°å?"""
        lst = [1, 2, 3]
        lst.append(4)
        self.assertEqual(len(lst), 4)
    
    def test_dict_access(self):
        """æ¸¬è©¦ dict å­˜å?"""
        d = {'a': 1, 'b': 2}
        self.assertEqual(d['a'], 1)

if __name__ == '__main__':
    unittest.main()
