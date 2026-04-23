import unittest
from io import StringIO
from unittest.mock import patch
import sys
import importlib.util
import os

# 動態匯入 490.py (Rotating Sentences)
current_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(current_dir, "490.py")
spec = importlib.util.spec_from_file_location("rotate_module", module_path)
rotate_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rotate_module)

class TestRotatingSentences(unittest.TestCase):
    def test_sample_rotation(self):
        # 模擬 UVA 490 範例輸入
        input_data = "HELLO\nWORLD\n"
        # 旋轉後: 最後一行變第一列，補齊空格
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

            # 因為 print 可能會多換行或空格，我們進行逐行比較或 strip
            actual = mock_stdout.getvalue().replace('\r', '')
            self.assertEqual(actual.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
