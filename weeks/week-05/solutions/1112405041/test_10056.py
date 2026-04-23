import unittest
from io import StringIO
import sys
import importlib

problem_10056 = importlib.import_module("10056")

class TestWhatIsTheProbability(unittest.TestCase):
    def test_sample_input(self):
        # 測試輸入：
        # 1 組測資, 2 個玩家, 成功機率 0.1666, 找第 1 個玩家
        # 計算: 0.1666 / (1 - (1-0.1666)^2) = 0.1666 / (1 - 0.8334^2)
        # = 0.1666 / (1 - 0.69455556) = 0.1666 / 0.30544444 = 0.545434...
        # 所以預期輸出應為 0.5454 (如果題目要求 4 位小數)
        # 檢查原 test_10056.py 裡的 expected_output 是 0.5455，這可能是隨意寫的
        input_str = "1\n2 0.1666 1\n"
        expected_output = "0.5454\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin

        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10056.solve()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output.strip())
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == '__main__':
    unittest.main()
