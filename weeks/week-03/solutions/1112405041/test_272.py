import unittest
from io import StringIO
from unittest.mock import patch
import sys
import importlib.util
import os

# 動態匯入 272.py (TEX Quotes)
current_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(current_dir, "272.py")
spec = importlib.util.spec_from_file_location("tex_module", module_path)
tex_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tex_module)

class TestTexQuotes(unittest.TestCase):
    def test_quotes_replacement(self):
        input_data = '"To be or not to be," quoth the Bard, "that is the question."\n'
        expected_output = "``To be or not to be,'' quoth the Bard, ``that is the question.''\n"
        
        with patch('sys.stdin', StringIO(input_data)), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            if hasattr(tex_module, 'solve'):
                tex_module.solve()
            elif hasattr(tex_module, 'main'):
                tex_module.main()

            self.assertEqual(mock_stdout.getvalue().replace('\r', ''), expected_output)

if __name__ == '__main__':
    unittest.main()
