"""10268 的單元測試。

這份測試同時檢查正式版與 easy 版，確保兩份程式輸出一致。
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent


def load_module(filename: str, module_name: str):
    """用檔案路徑載入模組，方便測試帶有 -easy 的檔名。"""

    path = BASE_DIR / filename
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


MAIN = load_module("10268.py", "solution_10268")
EASY = load_module("10268-easy.py", "solution_10268_easy")


class Test10268(unittest.TestCase):
    def assert_solve(self, text: str, expected: str) -> None:
        self.assertEqual(MAIN.solve(text), expected)
        self.assertEqual(EASY.solve(text), expected)

    def test_sample_cases(self) -> None:
        # 官方範例中包含正常答案與超過 63 次的情況。
        self.assert_solve(
            "2 100\n10 786599\n4 786599\n60 1844674407370955161\n63 9223372036854775807\n0 0\n",
            "14\n21\nMore than 63 trials needed.\n61\n63",
        )

    def test_small_cases(self) -> None:
        # 1 顆球時只能線性往上試；2 顆球時可以利用三角數加速。
        self.assert_solve(
            "1 1\n1 2\n2 3\n0 0\n",
            "1\n2\n2",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)