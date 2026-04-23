import unittest
from io import StringIO
from unittest.mock import patch
import sys
import importlib.util
import os

# 動態匯入 10035.py
current_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(current_dir, "10035.py")
spec = importlib.util.spec_from_file_location("carry_module", module_path)
carry_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(carry_module)

class TestPrimaryArithmetic(unittest.TestCase):
    def test_sample_output(self):
        input_data = "123 456\n555 555\n123 594\n0 0\n"
        expected_output = "No carry operation.\n3 carry operations.\n1 carry operation.\n"

        with patch('sys.stdin', StringIO(input_data)), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            if hasattr(carry_module, 'solve'):
                carry_module.solve()
            elif hasattr(carry_module, 'main'):
                carry_module.main()

            self.assertEqual(mock_stdout.getvalue().replace('\r', '').strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
