"""10226 的單元測試。

這份測試會同時檢查正式版與 easy 版，確保兩份程式的輸出一致。
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent


def load_module(filename: str, module_name: str):
    """用檔案路徑載入模組，這樣檔名有 -easy 也不會受限。"""

    path = BASE_DIR / filename
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


MAIN = load_module("10226.py", "solution_10226")
EASY = load_module("10226-easy.py", "solution_10226_easy")


class Test10226(unittest.TestCase):
    def assert_solve(self, text: str, expected: str) -> None:
        self.assertEqual(MAIN.solve(text), expected)
        self.assertEqual(EASY.solve(text), expected)

    def test_sample_case_without_constraints(self) -> None:
        # 第一組範例：三個人都沒有禁排位置。
        self.assert_solve(
            "3\n0\n0\n0\n",
            "ABC\nCB\nBAC\nCA\nCAB\nBA",
        )

    def test_multiple_cases_and_forbidden_positions(self) -> None:
        # 這個測資同時檢查：
        # 1. 多筆測資輸出中間要有空白行
        # 2. 禁排規則真的有被套用
        self.assert_solve(
            "2\n0\n0\n2\n2 0\n0\n",
            "AB\nBA\n\nAB",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)