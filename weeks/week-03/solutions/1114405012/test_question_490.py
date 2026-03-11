import importlib.util
import unittest
from pathlib import Path


# 受測檔名包含連字號，因此使用 importlib 依路徑載入。
def load_solution_module():
    solution_path = Path(__file__).with_name("QUESTION-490.py")
    spec = importlib.util.spec_from_file_location("question_490_solution", solution_path)

    if spec is None or spec.loader is None:
        raise ImportError("無法載入 QUESTION-490.py")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestQuestion490(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 整個測試類別只載入一次受測模組。
        cls.solution = load_solution_module()

    def test_sample_input_output(self):
        # 驗證題目說明中的 HELLO / WORLD 範例。
        self.assertEqual(
            self.solution.solve(self.solution.SAMPLE_INPUT),
            self.solution.SAMPLE_OUTPUT,
        )

    def test_rotate_uneven_lines(self):
        # 不同行長度時，必須以空白補齊後再旋轉。
        lines = ["ABC", "DE", "F"]
        expected = ["FDA", " EB", "  C"]
        self.assertEqual(self.solution.rotate_sentences(lines), expected)

    def test_single_line_input(self):
        # 單一橫向字串旋轉後會變成直向輸出。
        text = "ABC"
        expected = "A\nB\nC"
        self.assertEqual(self.solution.solve(text), expected)

    def test_preserve_leading_spaces_after_rotation(self):
        # 旋轉後若某列左側需要空白，應該保留下來。
        text = "AB\nC"
        expected = "CA\n B"
        self.assertEqual(self.solution.solve(text), expected)

    def test_empty_input(self):
        # 空輸入應回傳空字串。
        self.assertEqual(self.solution.solve(""), "")


if __name__ == "__main__":
    # 直接執行此檔案時，啟動 Python 內建單元測試。
    unittest.main()
