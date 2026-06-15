import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ?ÆÂ?Ê∏¨Ë©¶Ôºö‰∏ªÈ°?11ÔºàHello WorldÔº?

import unittest
import importlib

# ?ïÊ?Â∞éÂÖ• 11_formal Ê®°Á?
formal_11 = importlib.import_module('11_hand')
hello_world = formal_11.hello_world
hello_with_name = formal_11.hello_with_name

class TestHelloWorld(unittest.TestCase):
    
    def test_hello_world(self):
        """Ê∏¨Ë©¶ Hello World"""
        result = hello_world()
        self.assertEqual(result, 'Hello, World!')
    
    def test_hello_with_name(self):
        """Ê∏¨Ë©¶Â∏∂Â?Â≠óÁ??èÂÄ?""
        result = hello_with_name('Alice')
        self.assertEqual(result, 'Hello, Alice!')

if __name__ == '__main__':
    unittest.main()
