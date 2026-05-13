import unittest
import io
import sys
from main_optimized import solve

class TestNineDegree(unittest.TestCase):
    def test_sample(self):
        # 根據 UVA 10922 標準範例
        sample_input = "999999999999999999999\n9\n0\n"
        expected_output = (
            "9-degree of 999999999999999999999 is 3.\n"
            "9-degree of 9 is 1.\n"
        )
        
        # Mock stdin
        sys.stdin = io.StringIO(sample_input)
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        solve()
        
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
