import importlib.util
import pathlib
import unittest


BASE_DIR = pathlib.Path(__file__).resolve().parent


def load_module(file_name: str, module_name: str):
    # 使用檔案路徑匯入，方便同時測試正式版與 easy 版。
    module_path = BASE_DIR / file_name
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


solution = load_module("solution_10038.py", "solution_10038")
solution_easy = load_module("solution_10038-easy.py", "solution_10038_easy")
solution_hand = load_module("q10038_hand.py", "q10038_hand")


class JollyJumpersTests(unittest.TestCase):
    def test_sample_case(self):
        # 經典範例：第一組是 Jolly，第二組不是。
        data = """4 1 4 2 3
5 1 4 2 -1 6
"""
        expected = """Jolly
Not jolly"""
        self.assertEqual(solution.solve(data), expected)
        self.assertEqual(solution_easy.solve(data), expected)
        self.assertEqual(solution_hand.solve(data), expected)

    def test_single_value_is_jolly(self):
        # 長度為 1 的序列沒有缺少任何差值，視為 Jolly。
        data = """1 100
"""
        self.assertEqual(solution.solve(data), "Jolly")
        self.assertEqual(solution_easy.solve(data), "Jolly")
        self.assertEqual(solution_hand.solve(data), "Jolly")


if __name__ == "__main__":
    unittest.main()