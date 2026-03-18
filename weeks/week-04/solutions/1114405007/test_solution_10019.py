import importlib.util
import pathlib
import unittest


BASE_DIR = pathlib.Path(__file__).resolve().parent


def load_module(file_name: str, module_name: str):
    # 透過路徑載入模組，避免 -easy 檔名造成匯入問題。
    module_path = BASE_DIR / file_name
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


solution = load_module("solution_10019.py", "solution_10019")
solution_easy = load_module("solution_10019-easy.py", "solution_10019_easy")
solution_hand = load_module("q10019_hand.py", "q10019_hand")


class FunnyEncryptionTests(unittest.TestCase):
    def test_known_values(self):
        # 驗證十進位與十六進位解讀兩種計算結果。
        data = """3
265
111
10
"""
        expected = """3 5
6 3
2 1"""
        self.assertEqual(solution.solve(data), expected)
        self.assertEqual(solution_easy.solve(data), expected)
        self.assertEqual(solution_hand.solve(data), expected)

    def test_zero_value(self):
        # 0 轉成任何進位後都沒有 1。
        data = """1
0
"""
        self.assertEqual(solution.solve(data), "0 0")
        self.assertEqual(solution_easy.solve(data), "0 0")
        self.assertEqual(solution_hand.solve(data), "0 0")


if __name__ == "__main__":
    unittest.main()