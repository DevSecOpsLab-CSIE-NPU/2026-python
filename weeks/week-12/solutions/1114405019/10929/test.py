import unittest
import io
import sys
from main import solve

class TestMultipleOf11(unittest.TestCase):
    def test_sample(self):
        sample_input = "112233\n30800\n2937\n3234556\n121\n0\n"
        expected_output = (
            "112233 is a multiple of 11.\n"
            "30800 is a multiple of 11.\n"
            "2937 is a multiple of 11.\n"
            "3234556 is a multiple of 11.\n"
            "121 is a multiple of 11.\n"
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
