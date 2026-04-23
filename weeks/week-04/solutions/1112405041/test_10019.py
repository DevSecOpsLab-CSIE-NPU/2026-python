import unittest
from io import StringIO
from unittest.mock import patch
import sys
import importlib.util
import os

# 動態匯入 10019.py
current_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(current_dir, "10019.py")
spec = importlib.util.spec_from_file_location("encrypt_module", module_path)
encrypt_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(encrypt_module)

class TestEncryptionAnalyzer(unittest.TestCase):
    def test_sample_output(self):
        input_data = "3\n265\n97\n3\n"
        # 265: dec(265)=100001001 (b=3), hex(265)=0010 0110 0101 (b=5)
        expected_output = "3 5\n3 5\n2 2\n"

        with patch('sys.stdin', StringIO(input_data)), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            if hasattr(encrypt_module, 'solve'):
                encrypt_module.solve()
            elif hasattr(encrypt_module, 'main'):
                encrypt_module.main()

            self.assertEqual(mock_stdout.getvalue().replace('\r', '').strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
