from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


def _load_module(path: Path, module_name: str):
    """從路徑載入模組，方便測試含連字號檔名。"""
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"無法載入模組：{path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE_DIR = Path(__file__).resolve().parent
normal = _load_module(BASE_DIR / "uva_948.py", "uva_948_normal")
easy = _load_module(BASE_DIR / "uva_948-easy.py", "uva_948_easy")
hand = _load_module(BASE_DIR / "uva_948-hand.py", "uva_948_hand")


class TestUVA948(unittest.TestCase):
    """測試假幣推論：唯一解、無法唯一、與空白行格式。"""

    def assert_both_versions(self, input_data: str, expected: str) -> None:
        self.assertEqual(normal.solve(input_data), expected)
        self.assertEqual(easy.solve(input_data), expected)
        self.assertEqual(hand.solve(input_data), expected)

    def test_unique_solution(self) -> None:
        input_data = """1

3 2
1 1 2
=
1 1 2
=
"""
        expected = "3"
        self.assert_both_versions(input_data, expected)

    def test_multiple_testcases_with_blank_line_output(self) -> None:
        input_data = """2

3 2
1 1 2
=
1 1 2
=

3 1
1 1 2
<
"""
        expected = """3

0"""
        self.assert_both_versions(input_data, expected)

    def test_unique_by_mixed_results(self) -> None:
        input_data = """1

4 2
1 1 2
<
1 2 3
=
"""
        expected = "1"
        self.assert_both_versions(input_data, expected)


if __name__ == "__main__":
    unittest.main()
