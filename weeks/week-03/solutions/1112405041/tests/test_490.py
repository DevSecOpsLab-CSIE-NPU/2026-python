import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from io import StringIO
from unittest.mock import patch
import sys
import importlib.util
import os

# ?•æ??¯å…¥ 490.py (Rotating Sentences)
current_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(current_dir, "490.py")
spec = importlib.util.spec_from_file_location("rotate_module", module_path)
rotate_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rotate_module)

class TestRotatingSentences(unittest.TestCase):
    def test_sample_rotation(self):
        # æ¨¡æ“¬ UVA 490 ç¯„ä?è¼¸å…¥
        input_data = "HELLO\nWORLD\n"
        # ?‹è?å¾? ?€å¾Œä?è¡Œè?ç¬¬ä??—ï?è£œé?ç©ºæ ¼
        # W H
        # O E
        # R L
        # L L
        # D O
        expected_output = "WH\nOE\nRL\nLL\nDO\n"

        with patch('sys.stdin', StringIO(input_data)), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            if hasattr(rotate_module, 'solve'):
                rotate_module.solve()
            elif hasattr(rotate_module, 'main'):
                rotate_module.main()

            # ? ç‚º print ?¯èƒ½?ƒå??›è??–ç©º?¼ï??‘å€‘é€²è??è?æ¯”è???strip
            actual = mock_stdout.getvalue().replace('\r', '')
            self.assertEqual(actual.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()

