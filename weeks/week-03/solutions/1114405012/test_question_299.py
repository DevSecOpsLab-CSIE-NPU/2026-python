import importlib.util
import unittest
from pathlib import Path


# 受測檔名包含連字號，因此使用 importlib 動態載入。
def load_solution_module():
    solution_path = Path(__file__).with_name("QUESTION-299.py")
    spec = importlib.util.spec_from_file_location("question_299_solution", solution_path)

    if spec is None or spec.loader is None:
        raise ImportError("無法載入 QUESTION-299.py")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestQuestion299(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 整個測試類別只需載入一次解答模組。
        cls.solution = load_solution_module()

    def test_count_swaps_sorted_train(self):
        # 已排序完成的火車不需要任何交換。
        self.assertEqual(self.solution.count_swaps([1, 2, 3, 4]), 0)

    def test_count_swaps_reversed_train(self):
        # 完全反序的 4 節車廂共有 6 個反序對。
        self.assertEqual(self.solution.count_swaps([4, 3, 2, 1]), 6)

    def test_sample_input_output(self):
        # 驗證常見範例輸入是否能得到正確輸出。
        self.assertEqual(
            self.solution.solve(self.solution.SAMPLE_INPUT),
            self.solution.SAMPLE_OUTPUT,
        )

    def test_zero_length_train(self):
        # 題目允許 L = 0，此時交換次數應為 0。
        text = "1\n0\n"
        expected = "Optimal train swapping takes 0 swaps."
        self.assertEqual(self.solution.solve(text), expected)

    def test_multiple_cases_with_blank_lines(self):
        # 即使輸入中夾帶空白行，也應能正確解析。
        text = """
2
3
1 3 2

5
1 2 3 5 4
"""
        expected = (
            "Optimal train swapping takes 1 swaps.\n"
            "Optimal train swapping takes 1 swaps."
        )
        self.assertEqual(self.solution.solve(text), expected)


if __name__ == "__main__":
    # 直接執行此檔案時，啟動 Python 內建單元測試。
    unittest.main()
