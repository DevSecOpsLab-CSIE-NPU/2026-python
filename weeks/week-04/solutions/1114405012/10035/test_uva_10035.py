from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


def _load_module(path: Path, module_name: str):
    """用檔案路徑載入模組，便於測試一般檔與 -easy 檔。"""
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"無法載入模組：{path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE_DIR = Path(__file__).resolve().parent
normal = _load_module(BASE_DIR / "uva_10035.py", "uva_10035_normal")
easy = _load_module(BASE_DIR / "uva_10035-easy.py", "uva_10035_easy")
hand = _load_module(BASE_DIR / "uva_10035-hand.py", "uva_10035_hand")


class TestUVA10035(unittest.TestCase):
    """測試進位次數與輸出字串格式是否正確。"""

    def assert_both_versions(self, input_data: str, expected: str) -> None:
        self.assertEqual(normal.solve(input_data), expected)
        self.assertEqual(easy.solve(input_data), expected)
        self.assertEqual(hand.solve(input_data), expected)

    def test_sample_style(self) -> None:
        input_data = """123 456
555 555
123 594
0 0
"""
        expected = """No carry operation.
3 carry operations.
1 carry operation."""
        self.assert_both_versions(input_data, expected)

    def test_multiple_carries(self) -> None:
        input_data = """1 99999
9999 1
0 0
"""
        expected = """5 carry operations.
4 carry operations."""
        self.assert_both_versions(input_data, expected)


if __name__ == "__main__":
    unittest.main()
