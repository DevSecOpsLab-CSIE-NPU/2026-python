import unittest
from io import StringIO
from unittest.mock import patch
import sys
import importlib.util
import os

# 動態匯入 118.py (Martian Robots)
current_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(current_dir, "118.py")
spec = importlib.util.spec_from_file_location("robot_module", module_path)
robot_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(robot_module)

class TestMartianRobots(unittest.TestCase):
    def test_sample_output(self):
        # 模擬 UVA 118 範例輸入
        input_data = "5 3\n1 1 E\nRFRFRFRF\n3 2 N\nFRRFLLFFRRFLL\n0 3 W\nLLFFFLFLFL\n"
        expected_output = "1 1 E\n3 3 N LOST\n2 3 S\n"
        
        with patch('sys.stdin', StringIO(input_data)), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            if hasattr(robot_module, 'solve'):
                robot_module.solve()
            elif hasattr(robot_module, 'main'):
                robot_module.main()

            self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
