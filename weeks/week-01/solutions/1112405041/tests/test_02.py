import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ?®å?æ¸¬è©¦ï¼šä¸»é¡?02ï¼ˆåŸº?¬è??™å??¥ï?

import unittest
import importlib

# ?•æ?å°Žå…¥ 02_formal æ¨¡ç?
formal_02 = importlib.import_module('02_hand')
get_basic_types = formal_02.get_basic_types
convert_types = formal_02.convert_types

class TestBasicTypes(unittest.TestCase):
    
    def test_get_basic_types(self):
        """æ¸¬è©¦?ºæœ¬?‹åˆ¥"""
        result = get_basic_types()
        self.assertIsInstance(result['int'], int)
        self.assertIsInstance(result['float'], float)
        self.assertIsInstance(result['str'], str)
        self.assertIsInstance(result['bool'], bool)
    
    def test_convert_types(self):
        """æ¸¬è©¦?‹åˆ¥è½‰æ?"""
        result = convert_types()
        self.assertEqual(result['to_int'], 12)
        self.assertEqual(result['to_float'], 19.99)
        self.assertEqual(result['to_str'], '42')
    
    def test_int_conversion(self):
        """æ¸¬è©¦å­—ä¸²è½‰æ•´??""
        self.assertEqual(int('42'), 42)
        self.assertEqual(int('0'), 0)

if __name__ == '__main__':
    unittest.main()
