import importlib.util
import pathlib
import unittest


BASE_DIR = pathlib.Path(__file__).resolve().parent


def load_module(file_name: str, module_name: str):
    # 直接從檔案路徑載入，方便測試 -easy 檔名。
    module_path = BASE_DIR / file_name
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


solution = load_module("solution_10008.py", "solution_10008")
solution_easy = load_module("solution_10008-easy.py", "solution_10008_easy")
solution_hand = load_module("q10008_hand.py", "q10008_hand")


class CryptanalysisTests(unittest.TestCase):
    def test_count_and_sort_letters(self):
        # 驗證次數排序優先，其次才是字母順序。
        data = """4
AaBb
Zz
Hello
123!!
"""
        expected = """A 2
B 2
L 2
Z 2
E 1
H 1
O 1"""
        self.assertEqual(solution.solve(data), expected)
        self.assertEqual(solution_easy.solve(data), expected)
        self.assertEqual(solution_hand.solve(data), expected)

    def test_ignore_non_letters(self):
        # 若完全沒有英文字母，輸出應為空字串。
        data = """2
12345
?!@#$
"""
        self.assertEqual(solution.solve(data), "")
        self.assertEqual(solution_easy.solve(data), "")
        self.assertEqual(solution_hand.solve(data), "")


if __name__ == "__main__":
    unittest.main()