import subprocess
import sys
from pathlib import Path
import unittest


class TestQuestion10812(unittest.TestCase):
    """UVA 10812 的黑箱測試。

    這份測試不直接呼叫函式，而是模擬評測系統：
    透過標準輸入送資料，檢查標準輸出的結果是否正確。
    """

    def setUp(self):
        # 直接以同層的 solution.py 當作被測試程式，符合提交時的預設命名。
        self.solution_path = Path(__file__).with_name("solution.py")

    def _run_program(self, raw_input: str) -> str:
        # 使用 subprocess 模擬線上評測，避免測試與實作程式互相耦合。
        completed = subprocess.run(
            [sys.executable, str(self.solution_path)],
            input=raw_input,
            text=True,
            capture_output=True,
            cwd=self.solution_path.parent,
            check=False,
        )
        return completed.stdout.strip()

    def test_basic_valid_case(self):
        # 正常情況：和與差都合法，可以拆出兩隊分數。
        output = self._run_program("1\n40 20\n")
        self.assertEqual(output, "30 10")

    def test_equal_scores_case(self):
        # 差為 0 時，兩隊分數應該相同。
        output = self._run_program("1\n18 0\n")
        self.assertEqual(output, "9 9")

    def test_zero_scores_case(self):
        # 邊界值：總和與差都為 0，答案應該是 0 0。
        output = self._run_program("1\n0 0\n")
        self.assertEqual(output, "0 0")

    def test_impossible_due_to_odd_sum(self):
        # S + D 為奇數時，無法同時得到兩個整數解。
        output = self._run_program("1\n21 10\n")
        self.assertEqual(output, "impossible")

    def test_impossible_due_to_negative_score(self):
        # 若差值大於總和，較小分數會變成負數，必須輸出 impossible。
        output = self._run_program("1\n10 20\n")
        self.assertEqual(output, "impossible")

    def test_multiple_cases_in_one_input(self):
        # 模擬正式輸入格式：第一行是筆數，後面連續多筆資料。
        output = self._run_program("3\n40 20\n21 10\n10 20\n")
        self.assertEqual(output, "30 10\nimpossible\nimpossible")


if __name__ == "__main__":
    unittest.main()