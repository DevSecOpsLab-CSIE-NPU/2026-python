import importlib.util
import unittest
from pathlib import Path


# 由於原始解答檔名包含連字號，不能直接用一般 import 載入，
# 因此這裡改用 importlib 依照檔案路徑動態載入模組。
def load_solution_module():
    solution_path = Path(__file__).with_name("QUESTION-100.py")
    spec = importlib.util.spec_from_file_location("question_100_solution", solution_path)

    if spec is None or spec.loader is None:
        raise ImportError("無法載入 QUESTION-100.py")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestQuestion100(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 只在整個測試類別開始時載入一次受測模組。
        cls.solution = load_solution_module()

    def setUp(self):
        # 每個測試案例開始前重置快取，避免不同測試互相影響。
        self.solution.memo.clear()
        self.solution.memo.update({1: 1})

    def test_cycle_length_of_1(self):
        # 最小基本案例：1 的 cycle length 應該是 1。
        self.assertEqual(self.solution.cycle_length(1), 1)

    def test_cycle_length_of_22(self):
        # 題目敘述明確給出 22 的 cycle length 為 16。
        self.assertEqual(self.solution.cycle_length(22), 16)

    def test_max_cycle_length_with_normal_order(self):
        # 驗證一般順序輸入時，區間 [1, 10] 的最大值是否正確。
        self.assertEqual(self.solution.max_cycle_length(1, 10), 20)

    def test_max_cycle_length_with_reverse_order(self):
        # 題目允許 i 與 j 任意順序，因此反向輸入也應得到相同答案。
        self.assertEqual(self.solution.max_cycle_length(10, 1), 20)

    def test_solve_sample_input(self):
        # 直接驗證題目範例輸入與範例輸出是否完全一致。
        self.assertEqual(
            self.solution.solve(self.solution.SAMPLE_INPUT),
            self.solution.SAMPLE_OUTPUT,
        )

    def test_solve_ignores_blank_lines(self):
        # 若輸入中夾帶空白行，程式也應能安全略過並正常輸出。
        text = """
1 10

201 210
"""
        expected = "1 10 20\n201 210 89"
        self.assertEqual(self.solution.solve(text), expected)


if __name__ == "__main__":
    # 直接執行此檔案時，啟動 Python 內建的單元測試。
    unittest.main()
