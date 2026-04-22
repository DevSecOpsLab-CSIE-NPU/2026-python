"""10235 的單元測試。

這份測試同時檢查正式版與 easy 版，確保兩份程式輸出一致。
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent


def load_module(filename: str, module_name: str):
    """依檔案路徑載入模組，方便測試帶有 -easy 的檔名。"""

    path = BASE_DIR / filename
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


MAIN = load_module("10235.py", "solution_10235")
EASY = load_module("10235-easy.py", "solution_10235_easy")


class Test10235(unittest.TestCase):
    def assert_solve(self, text: str, expected: str) -> None:
        self.assertEqual(MAIN.solve(text), expected)
        self.assertEqual(EASY.solve(text), expected)

    def test_sample_like_cases(self) -> None:
        # 這組測資專門檢查：
        # 1. 單一格被插座佔住時答案是 1
        # 2. 單一格沒有插座時無法形成環，答案是 0
        # 3. 2x2 全空格時只有一種四邊環
        self.assert_solve(
            "3\n1 1\n0\n1 1\n1\n2 2\n1 1\n1 1\n",
            "Case 1: 1\nCase 2: 0\nCase 3: 1",
        )

    def test_blocked_cells_reduce_answers(self) -> None:
        # 這組測資檢查插座位置真的會把可行方案排除掉。
        self.assert_solve(
            "1\n2 2\n1 0\n1 1\n",
            "Case 1: 0",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)