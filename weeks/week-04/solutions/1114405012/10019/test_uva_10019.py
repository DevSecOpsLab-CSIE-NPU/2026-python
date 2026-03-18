from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


def _load_module(path: Path, module_name: str):
    """用檔案路徑載入模組，讓 -easy 檔名也可被測試。"""
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"無法載入模組：{path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE_DIR = Path(__file__).resolve().parent
normal = _load_module(BASE_DIR / "uva_10019.py", "uva_10019_normal")
easy = _load_module(BASE_DIR / "uva_10019-easy.py", "uva_10019_easy")
hand = _load_module(BASE_DIR / "uva_10019-hand.py", "uva_10019_hand")


class TestUVA10019(unittest.TestCase):
    """測試兩整數差距（絕對值）輸出。"""

    def assert_both_versions(self, input_data: str, expected: str) -> None:
        self.assertEqual(normal.solve(input_data), expected)
        self.assertEqual(easy.solve(input_data), expected)
        self.assertEqual(hand.solve(input_data), expected)

    def test_basic_cases(self) -> None:
        input_data = """10 12
10 14
100 200
"""
        expected = """2
4
100"""
        self.assert_both_versions(input_data, expected)

    def test_big_integers(self) -> None:
        input_data = """100000000000000000000 1
1 100000000000000000000
"""
        expected = """99999999999999999999
99999999999999999999"""
        self.assert_both_versions(input_data, expected)


if __name__ == "__main__":
    unittest.main()
