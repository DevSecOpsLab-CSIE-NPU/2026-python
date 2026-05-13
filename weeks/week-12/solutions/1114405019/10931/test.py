import unittest
import io
import sys
from main import solve

class TestParity(unittest.TestCase):
    def test_sample(self):
        sample_input = "1\n2\n10\n21\n0\n"
        expected_output = (
            "The parity of 1 is 1 (mod 2).\n"
            "The parity of 10 is 1 (mod 2).\n"
            "The parity of 1010 is 2 (mod 2).\n"
            "The parity of 10101 is 3 (mod 2).\n"
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
