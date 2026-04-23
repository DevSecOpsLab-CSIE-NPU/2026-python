import unittest
from io import StringIO
from unittest.mock import patch
import sys
import importlib.util
import os

# 動態匯入 299.py (Train Swapping)
current_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(current_dir, "299.py")
spec = importlib.util.spec_from_file_location("train_module", module_path)
train_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(train_module)

class TestTrainSwapping(unittest.TestCase):
    def test_bubble_sort_swaps(self):
        input_data = "3\n3\n1 3 2\n4\n4 3 2 1\n2\n2 1\n"
        expected_output = "Optimal train swapping takes 1 swaps.\nOptimal train swapping takes 6 swaps.\nOptimal train swapping takes 1 swaps.\n"

        with patch('sys.stdin', StringIO(input_data)), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            if hasattr(train_module, 'solve'):
                train_module.solve()
            elif hasattr(train_module, 'main'):
                train_module.main()

            self.assertEqual(mock_stdout.getvalue().replace('\r', ''), expected_output)

if __name__ == '__main__':
    unittest.main()
