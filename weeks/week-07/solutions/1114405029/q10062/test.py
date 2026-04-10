import unittest
import io
from contextlib import redirect_stdout

class TestSolution(unittest.TestCase):
    def test_logic(self):
        test_input = "5\n1\n2\n1\n0"
        expected_output = "2\n4\n5\n3\n1\n"
        
        # 測試各個版本
        from main_easy import solve as solve_easy
        from main_handwritten import solve as solve_hand
        
        for func in [solve_easy, solve_hand]:
            sys_stdin = io.StringIO(test_input)
            sys_stdout = io.StringIO()
            import sys
            old_stdin = sys.stdin
            sys.stdin = sys_stdin
            
            with redirect_stdout(sys_stdout):
                func()
            
            sys.stdin = old_stdin
            self.assertEqual(sys_stdout.getvalue().strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()