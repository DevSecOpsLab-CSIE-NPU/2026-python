import unittest
from io import StringIO
from unittest.mock import patch
import sys
import importlib.util
import os

# 動態匯入 948.py
current_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(current_dir, "948.py")
spec = importlib.util.spec_from_file_location("fibo_module", module_path)
fibo_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fibo_module)

class TestFibonaccimalBase(unittest.TestCase):
    def test_sample_output(self):
        input_data = "1\n100\n"
        expected_output = "100 = 1000010100 (fib)"

        with patch('sys.stdin', StringIO(input_data)), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            if hasattr(fibo_module, 'solve'):
                fibo_module.solve()
            elif hasattr(fibo_module, 'main'):
                fibo_module.main()

            actual = mock_stdout.getvalue().replace('\r', '').strip()
            self.assertEqual(actual, expected_output)

if __name__ == '__main__':
    unittest.main()
