import unittest
import io
import sys
from main import solve

class TestLargestSquare(unittest.TestCase):
    def test_sample(self):
        sample_input = (
            "1\n"
            "7 10 4\n"
            "abbbaaaaaa\n"
            "abbbaaaaaa\n"
            "abbbaaaaaa\n"
            "aaaaaaaaaa\n"
            "aaaaaaaaaa\n"
            "aaccaaaaaa\n"
            "aaccaaaaaa\n"
            "1 2\n"
            "2 4\n"
            "4 6\n"
            "5 2\n"
        )
        expected_output = (
            "7 10 4\n"
            "3\n"
            "1\n"
            "5\n"
            "1\n"
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
