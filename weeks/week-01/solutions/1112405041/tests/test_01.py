import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ?®å?æ¸¬è©¦ï¼šä¸»é¡?01ï¼ˆè??¸è??‡å?ï¼?

import unittest
import importlib

# ?•æ?å°Žå…¥ 01_formal æ¨¡ç?
formal_01 = importlib.import_module('01_hand')
get_point = formal_01.get_point
demonstrate_assignment = formal_01.demonstrate_assignment

class TestAssignment(unittest.TestCase):
    
    def test_get_point(self):
        """æ¸¬è©¦ get_point ?½å?"""
        result = get_point()
        self.assertEqual(result, (4, 9))
    
    def test_demonstrate_assignment(self):
        """æ¸¬è©¦ demonstrate_assignment ?½å?"""
        result = demonstrate_assignment()
        self.assertEqual(result['x'], 3)
        self.assertEqual(result['name'], 'ACME')
        self.assertEqual(result['y'], 5)
        self.assertEqual(result['px'], 4)
        self.assertEqual(result['py'], 9)
    
    def test_tuple_unpacking(self):
        """æ¸¬è©¦ tuple è§??"""
        a, b = 1, 2
        self.assertEqual(a, 1)
        self.assertEqual(b, 2)

if __name__ == '__main__':
    unittest.main()
