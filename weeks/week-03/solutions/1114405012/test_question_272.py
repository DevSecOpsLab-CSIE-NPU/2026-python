import importlib.util
import unittest
from pathlib import Path


# 受測檔名包含連字號，因此改用 importlib 依路徑載入模組。
def load_solution_module():
    solution_path = Path(__file__).with_name("QUESTION-272.py")
    spec = importlib.util.spec_from_file_location("question_272_solution", solution_path)

    if spec is None or spec.loader is None:
        raise ImportError("無法載入 QUESTION-272.py")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestQuestion272(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 整個測試類別只需要載入一次受測模組。
        cls.solution = load_solution_module()

    def test_sample_sentence(self):
        # 題目敘述中的經典句子必須被正確轉換。
        self.assertEqual(
            self.solution.solve(self.solution.SAMPLE_INPUT),
            self.solution.SAMPLE_OUTPUT,
        )

    def test_plain_text_without_quotes(self):
        # 沒有雙引號的文字不應被更動。
        text = "Hello\nWorld\n"
        self.assertEqual(self.solution.solve(text), text)

    def test_quotes_across_multiple_lines(self):
        # 多行文字中的雙引號要依照全域順序交替替換。
        text = '"Hello"\n"World"\n'
        expected = "``Hello''\n``World''\n"
        self.assertEqual(self.solution.solve(text), expected)

    def test_quote_pair_spanning_two_lines(self):
        # 即使開引號與閉引號分別落在不同列，也應正常處理。
        text = '"Hello\nWorld"\n'
        expected = "``Hello\nWorld''\n"
        self.assertEqual(self.solution.transform_quotes(text), expected)

    def test_empty_input(self):
        # 空字串應回傳空字串。
        self.assertEqual(self.solution.solve(""), "")


if __name__ == "__main__":
    # 直接執行此檔案時，啟動 Python 內建單元測試。
    unittest.main()
