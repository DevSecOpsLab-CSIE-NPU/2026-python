from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


def _load_module(path: Path, module_name: str):
    """從檔案路徑載入模組，用於同時測試正式版與 easy 版。"""
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"無法載入模組：{path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE_DIR = Path(__file__).resolve().parent
normal = _load_module(BASE_DIR / "uva_10038.py", "uva_10038_normal")
easy = _load_module(BASE_DIR / "uva_10038-easy.py", "uva_10038_easy")
hand = _load_module(BASE_DIR / "uva_10038-hand.py", "uva_10038_hand")


class TestUVA10038(unittest.TestCase):
    """測試 Jolly Jumper 判斷。"""

    def assert_both_versions(self, input_data: str, expected: str) -> None:
        self.assertEqual(normal.solve(input_data), expected)
        self.assertEqual(easy.solve(input_data), expected)
        self.assertEqual(hand.solve(input_data), expected)

    def test_mixed_cases(self) -> None:
        input_data = """4 1 4 2 3
5 1 4 2 -1 6
1 10
"""
        expected = """Jolly
Not jolly
Jolly"""
        self.assert_both_versions(input_data, expected)

    def test_wrapped_tokens(self) -> None:
        input_data = """4
1 4 2 3
"""
        expected = "Jolly"
        self.assert_both_versions(input_data, expected)


if __name__ == "__main__":
    unittest.main()
