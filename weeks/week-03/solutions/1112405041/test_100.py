import unittest
from io import StringIO
from unittest.mock import patch
import sys
import importlib.util
import os

# 動態匯入模組，確保路徑正確
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
            # 這裡呼叫 100.py 的 solve 或是 main
            # 由於 100.py 之前內容可能被改過，我們確保呼叫正確入口
            if hasattr(formal_module, 'solve'):
                formal_module.solve()
            elif hasattr(formal_module, 'main'):
                formal_module.main()

            self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
