import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from io import StringIO
from unittest.mock import patch
import sys
import importlib.util
import os

# ?•æ??¯å…¥æ¨¡ç?ï¼Œç¢ºä¿è·¯å¾‘æ­£ç¢?
current_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(current_dir, "100.py")
spec = importlib.util.spec_from_file_location("formal_module", module_path)
formal_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(formal_module)

class TestCollatzCalculator(unittest.TestCase):
    def test_max_cycle(self):
        input_data = "1 10\n100 200\n"
        expected_output = "1 10 20\n100 200 125\n"
        
        with patch('sys.stdin', StringIO(input_data)), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # ?™è£¡?¼å« 100.py ??solve ?–æ˜¯ main
            # ?±æ–¼ 100.py ä¹‹å??§å®¹?¯èƒ½è¢«æ”¹?ï??‘å€‘ç¢ºä¿å‘¼?«æ­£ç¢ºå…¥??
            if hasattr(formal_module, 'solve'):
                formal_module.solve()
            elif hasattr(formal_module, 'main'):
                formal_module.main()

            self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()

