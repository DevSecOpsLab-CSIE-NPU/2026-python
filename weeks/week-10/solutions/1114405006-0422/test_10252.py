"""10252 的單元測試。

這份測試同時檢查正式版與 easy 版，確保兩份程式輸出一致。
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent


def load_module(filename: str, module_name: str):
    """用檔案路徑載入模組，這樣檔名帶有 -easy 也沒問題。"""

    path = BASE_DIR / filename
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


MAIN = load_module("10252.py", "solution_10252")
EASY = load_module("10252-easy.py", "solution_10252_easy")


class Test10252(unittest.TestCase):
    def assert_solve(self, text: str, expected: str) -> None:
        self.assertEqual(MAIN.solve(text), expected)
        self.assertEqual(EASY.solve(text), expected)

    def test_sample_like_case(self) -> None:
        # 兩個字串有多個共同字元，且需要排序輸出。
        self.assert_solve(
            "1\npretty\nwomen\n",
            "e",
        )

    def test_duplicates_are_kept_by_minimum_count(self) -> None:
        # 同一字元重複出現時，要保留共同出現次數的最小值。
        self.assert_solve(
            "2\naabbcc\nbbccdd\nabcabc\ncbacba\n",
            "bbcc\naabbcc",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)