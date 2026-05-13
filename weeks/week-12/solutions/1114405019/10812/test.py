import unittest
import io
import sys
from main import solve

class TestBeatTheSpread(unittest.TestCase):
    def test_sample(self):
        sample_input = "2\n40 20\n20 40\n"
        expected_output = "30 10\nimpossible\n"
        
        # Mock stdin
        sys.stdin = io.StringIO(sample_input)
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        solve()
        
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
