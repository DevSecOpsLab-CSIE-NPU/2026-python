import unittest
from io import StringIO
import sys
import importlib

# 使用 importlib 讀取開頭為數字的模組
problem_10041 = importlib.import_module("10041")

class TestVitosFamily(unittest.TestCase):
    def test_sample_input(self):
        # 模擬輸入：2 組資料
        # 第一組：2 個親戚，門牌 2 4 -> 距離 |2-3| + |4-3| = 2 (中位數是 2 或 4 都可以，這裡選 4)
        # 修正: 2 2 4 表示 2 組測資，第一組 2 個親戚是 2 4
        # 第二組: 3 個親戚，門牌 2 4 6 -> 距離 |2-4| + |4-4| + |6-4| = 2 + 0 + 2 = 4
        input_str = "2\n2 2 4\n3 2 4 6\n"
        expected_output = "2\n4\n"

        # 攔截 stdout
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        # 攔截 stdin
        saved_stdin = sys.stdin
        sys.stdin = StringIO(input_str)

        try:
            problem_10041.solve()
            # 去除結尾空白再比較
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output.strip())
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == '__main__':
    unittest.main()
