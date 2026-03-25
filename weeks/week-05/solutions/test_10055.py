import unittest
from io import StringIO
import sys
import importlib.util

# 動態載入 10055.py 模組
spec = importlib.util.spec_from_file_location("solution", "10055.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

SegmentTree = solution.SegmentTree

class Test10055(unittest.TestCase):
    """
    測試類別：針對 10055 問題的測試
    """

    def test_segment_tree_basic(self):
        st = SegmentTree(5)
        funcs = [0, 0, 0, 0, 0, 0]
        st.build(funcs, 1, 1, 5)
        self.assertEqual(st.query_range(1, 1, 5, 1, 5), 0)
        st.update_range(1, 1, 5, 3, 3)
        self.assertEqual(st.query_range(1, 1, 5, 3, 3), 1)
        self.assertEqual(st.query_range(1, 1, 5, 1, 5), 1)
        st.update_range(1, 1, 5, 2, 4)
        self.assertEqual(st.query_range(1, 1, 5, 2, 4), 2)

    def test_main_simple(self):
        input_data = "3 4\n1 2\n2 1 3\n1 2\n2 1 3\n"
        expected_output = "1\n0\n"

        old_stdin = sys.stdin
        old_stdout = sys.stdout
        sys.stdin = StringIO(input_data)
        sys.stdout = StringIO()

        try:
            solution.main()
            output = sys.stdout.getvalue()
            self.assertEqual(output, expected_output)
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout

if __name__ == '__main__':
    unittest.main(verbosity=2)