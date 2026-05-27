import io
import os
import unittest
import importlib.util


def _load_module_from_path(module_name: str, file_path: str):
    """從指定檔案路徑載入模組（支援檔名含 -easy）。"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"無法載入模組：{file_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestUVA10812(unittest.TestCase):
    """UVA 10812: Beat the Spread! 的單元測試。"""

    @classmethod
    def setUpClass(cls):
        here = os.path.dirname(__file__)
        cls.solution = _load_module_from_path(
            "solution_10812",
            os.path.join(here, "solution_10812.py"),
        )
        cls.solution_easy = _load_module_from_path(
            "solution_10812_easy",
            os.path.join(here, "solution_10812_easy.py"),
        )

    def _run_solve(self, mod, input_text: str) -> str:
        """用 StringIO 模擬 stdin/stdout，回傳輸出文字。"""
        stdin = io.StringIO(input_text)
        stdout = io.StringIO()
        mod.solve(stdin, stdout)
        return stdout.getvalue()

    def test_sample_case(self):
        # 題目給的範例
        input_text = "2\n40 20\n20 40\n"
        expected = "30 10\nimpossible\n"
        self.assertEqual(self._run_solve(self.solution, input_text), expected)
        self.assertEqual(self._run_solve(self.solution_easy, input_text), expected)

    def test_zero_zero(self):
        # S=0, D=0 -> 0 0
        input_text = "1\n0 0\n"
        expected = "0 0\n"
        self.assertEqual(self._run_solve(self.solution, input_text), expected)
        self.assertEqual(self._run_solve(self.solution_easy, input_text), expected)

    def test_diff_greater_than_sum_impossible(self):
        # D > S 一定無解（較小分會是負數）
        input_text = "3\n0 1\n20 40\n5 9\n"
        expected = "impossible\nimpossible\nimpossible\n"
        self.assertEqual(self._run_solve(self.solution, input_text), expected)
        self.assertEqual(self._run_solve(self.solution_easy, input_text), expected)

    def test_odd_sum_plus_diff_impossible(self):
        # (S + D) 必須為偶數，否則 (S+D)/2 不是整數
        input_text = "3\n1 0\n5 2\n9 4\n"  # 1, 7, 13 都是奇數
        expected = "impossible\nimpossible\nimpossible\n"
        self.assertEqual(self._run_solve(self.solution, input_text), expected)
        self.assertEqual(self._run_solve(self.solution_easy, input_text), expected)

    def test_valid_cases(self):
        # 一些有效案例：輸出較大的在前
        input_text = "4\n10 10\n10 0\n40 0\n100 20\n"
        expected = "10 0\n5 5\n20 20\n60 40\n"
        self.assertEqual(self._run_solve(self.solution, input_text), expected)
        self.assertEqual(self._run_solve(self.solution_easy, input_text), expected)


if __name__ == "__main__":
    unittest.main()
