import io
import os
import unittest
import importlib.util


def _load_module_from_path(module_name: str, file_path: str):
    """從指定檔案路徑動態載入模組（支援 *_easy）"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"無法載入模組：{file_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestUVA10908(unittest.TestCase):
    """UVA 10908: Largest Square 的單元測試。"""

    @classmethod
    def setUpClass(cls):
        here = os.path.dirname(__file__)
        cls.solution = _load_module_from_path(
            "solution_10908",
            os.path.join(here, "solution_10908.py"),
        )
        cls.solution_easy = _load_module_from_path(
            "solution_10908_easy",
            os.path.join(here, "solution_10908_easy.py"),
        )

    def _run_solve(self, mod, input_text: str) -> str:
        """用 StringIO 模擬 stdin/stdout，取得程式標準輸出文字。"""
        stdin = io.StringIO(input_text)
        stdout = io.StringIO()
        mod.solve(stdin, stdout)
        return stdout.getvalue()

    def test_sample_case(self):
        # 題目給定之範例測資
        input_text = (
            "1\n7 10 4\n"
            "abbbaaaaaa\nabbbaaaaaa\nabbbaaaaaa\naaaaaaaaaa\naaaaaaaaaa\naaccaaaaaa\naaccaaaaaa\n"
            "1 2\n2 4\n4 6\n5 2\n"
        )
        expected = (
            "7 10 4\n"
            "3\n"
            "1\n"
            "5\n"
            "1\n"
        )
        self.assertEqual(self._run_solve(self.solution, input_text), expected)
        self.assertEqual(self._run_solve(self.solution_easy, input_text), expected)

    def test_odd_center_and_singlecell(self):
        # 邊界：中心點本身、小矩陣、多字元
        input_text = (
            "1\n3 3 2\naba\nbcb\naba\n"
            "1 1\n0 0\n"
        )
        expected = (
            "3 3 2\n1\n1\n"
        )
        self.assertEqual(self._run_solve(self.solution, input_text), expected)
        self.assertEqual(self._run_solve(self.solution_easy, input_text), expected)

    def test_full_same_char(self):
        # 特例：全部都是同一字元，中心最大可撐多大
        input_text = (
            "1\n5 5 1\nxxxxx\nxxxxx\nxxxxx\nxxxxx\nxxxxx\n2 2\n"
        )
        expected = "5 5 1\n5\n"
        self.assertEqual(self._run_solve(self.solution, input_text), expected)
        self.assertEqual(self._run_solve(self.solution_easy, input_text), expected)

    def test_out_of_bound(self):
        # 極小矩陣/角落直接只有 1
        input_text = (
            "1\n2 3 1\nabc\ndef\n1 2\n"
        )
        expected = "2 3 1\n1\n"
        self.assertEqual(self._run_solve(self.solution, input_text), expected)
        self.assertEqual(self._run_solve(self.solution_easy, input_text), expected)

if __name__ == "__main__":
    unittest.main()
