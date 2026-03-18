import importlib.util
import pathlib
import unittest


BASE_DIR = pathlib.Path(__file__).resolve().parent


def load_module(file_name: str, module_name: str):
    # 使用檔案路徑載入模組，這樣就算檔名含有 - 也能正常測試。
    module_path = BASE_DIR / file_name
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


solution = load_module("solution_948.py", "solution_948")
solution_easy = load_module("solution_948-easy.py", "solution_948_easy")
solution_hand = load_module("q948_hand.py", "q948_hand")


SAMPLE_INPUT = """2

5 3
2 1 2 3 4
<
1 1 4
=
1 2 5
=

4 2
1 1 2
<
1 3 4
=
"""

SAMPLE_OUTPUT = """3

0"""


class FakeCoinTests(unittest.TestCase):
    def test_sample_case(self):
        # 驗證題目範例輸入輸出是否正確。
        self.assertEqual(solution.solve(SAMPLE_INPUT), SAMPLE_OUTPUT)
        self.assertEqual(solution_easy.solve(SAMPLE_INPUT), SAMPLE_OUTPUT)
        self.assertEqual(solution_hand.solve(SAMPLE_INPUT), SAMPLE_OUTPUT)

    def test_single_unique_lighter_coin(self):
        # 只有 1 號硬幣可能是較輕的假幣。
        data = """1

3 2
1 1 2
<
1 2 3
=
"""
        self.assertEqual(solution.solve(data), "1")
        self.assertEqual(solution_easy.solve(data), "1")
        self.assertEqual(solution_hand.solve(data), "1")

    def test_single_unique_heavier_coin(self):
        # 透過多次秤重排除其他可能，最後只剩 1 號較重成立。
        data = """1

4 3
2 1 2 3 4
>
1 2 4
=
1 1 2
>
"""
        self.assertEqual(solution.solve(data), "1")
        self.assertEqual(solution_easy.solve(data), "1")
        self.assertEqual(solution_hand.solve(data), "1")

    def test_ambiguous_answer_returns_zero(self):
        # 若仍有多顆硬幣都可能是假幣，題目要求輸出 0。
        data = """1

5 1
2 1 2 3 4
<
"""
        self.assertEqual(solution.solve(data), "0")
        self.assertEqual(solution_easy.solve(data), "0")
        self.assertEqual(solution_hand.solve(data), "0")


if __name__ == "__main__":
    unittest.main()