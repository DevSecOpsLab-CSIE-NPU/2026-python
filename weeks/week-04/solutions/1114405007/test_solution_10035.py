import importlib.util
import pathlib
import unittest


BASE_DIR = pathlib.Path(__file__).resolve().parent


def load_module(file_name: str, module_name: str):
    # 直接從檔案載入，讓正式版與 easy 版共用相同測試。
    module_path = BASE_DIR / file_name
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


solution = load_module("solution_10035.py", "solution_10035")
solution_easy = load_module("solution_10035-easy.py", "solution_10035_easy")
solution_hand = load_module("q10035_hand.py", "q10035_hand")


class PrimaryArithmeticTests(unittest.TestCase):
    def test_sample_cases(self):
        # 驗證題目最常見的三種輸出句型。
        data = """123 456
555 555
123 594
0 0
"""
        expected = """No carry operation.
3 carry operations.
1 carry operation."""
        self.assertEqual(solution.solve(data), expected)
        self.assertEqual(solution_easy.solve(data), expected)
        self.assertEqual(solution_hand.solve(data), expected)

    def test_different_lengths(self):
        # 位數不同時也要能正確把缺少的位數視為 0。
        data = """1 20000
999 1
0 0
"""
        expected = """No carry operation.
3 carry operations."""
        self.assertEqual(solution.solve(data), expected)
        self.assertEqual(solution_easy.solve(data), expected)
        self.assertEqual(solution_hand.solve(data), expected)


if __name__ == "__main__":
    unittest.main()