from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


def _load_module(path: Path, module_name: str):
    """從指定檔案路徑載入模組，方便測試含 -easy 檔名的程式。"""
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"無法載入模組：{path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE_DIR = Path(__file__).resolve().parent
normal = _load_module(BASE_DIR / "uva_10008.py", "uva_10008_normal")
easy = _load_module(BASE_DIR / "uva_10008-easy.py", "uva_10008_easy")
hand = _load_module(BASE_DIR / "uva_10008-hand.py", "uva_10008_hand")


class TestUVA10008(unittest.TestCase):
    """測試 UVA 10008：字母次數統計與排序規則。"""

    def assert_both_versions(self, input_data: str, expected: str) -> None:
        # 兩個版本都要得到同樣結果
        self.assertEqual(normal.solve(input_data), expected)
        self.assertEqual(easy.solve(input_data), expected)
        self.assertEqual(hand.solve(input_data), expected)

    def test_basic_count_and_sort(self) -> None:
        input_data = """2
ABCabc
bB!!
"""
        expected = """B 4
A 2
C 2"""
        self.assert_both_versions(input_data, expected)

    def test_tie_break_by_letter(self) -> None:
        input_data = """3
a z
B y
c X
"""
        expected = """A 1
B 1
C 1
X 1
Y 1
Z 1"""
        self.assert_both_versions(input_data, expected)

    def test_no_letters(self) -> None:
        input_data = """1
1234 !@#
"""
        expected = ""
        self.assert_both_versions(input_data, expected)


if __name__ == "__main__":
    unittest.main()
