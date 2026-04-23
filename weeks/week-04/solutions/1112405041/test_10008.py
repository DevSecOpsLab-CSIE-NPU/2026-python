import unittest
from io import StringIO
from unittest.mock import patch
import sys
import importlib.util
import os

# 動態匯入 10008.py
current_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(current_dir, "10008.py")
spec = importlib.util.spec_from_file_location("crypto_module", module_path)
crypto_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(crypto_module)

class TestCryptanalysis(unittest.TestCase):
    def test_sample_output(self):
        input_data = "1\nThis is a test."
        # T: 3, S: 3, I: 2, A: 1, E: 1, H: 1
        expected_output = "S 3\nT 3\nI 2\nA 1\nE 1\nH 1\n"

        with patch('sys.stdin', StringIO(input_data)), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            if hasattr(crypto_module, 'solve'):
                crypto_module.solve()
            elif hasattr(crypto_module, 'main'):
                crypto_module.main()

            actual = mock_stdout.getvalue().replace('\r', '')
            self.assertEqual(actual.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
