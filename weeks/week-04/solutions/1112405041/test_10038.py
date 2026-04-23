import unittest
from io import StringIO
from unittest.mock import patch
import sys
import importlib.util
import os

# 動態匯入 10038.py
current_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(current_dir, "10038.py")
spec = importlib.util.spec_from_file_location("jolly_module", module_path)
jolly_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jolly_module)

class TestJollyJumpers(unittest.TestCase):
    def test_sample_output(self):
        input_data = "4 1 4 2 3\n5 1 4 2 -1 6\n"
        expected_output = "Jolly\nNot jolly\n"

        with patch('sys.stdin', StringIO(input_data)), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            if hasattr(jolly_module, 'solve'):
                jolly_module.solve()
            elif hasattr(jolly_module, 'main'):
                jolly_module.main()

            self.assertEqual(mock_stdout.getvalue().replace('\r', '').strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
