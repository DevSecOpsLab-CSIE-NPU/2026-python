"""10242 的單元測試。

這份測試同時驗證正式版與 easy 版，確保兩份程式的輸出一致。
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent


def load_module(filename: str, module_name: str):
    """依檔名載入模組，方便測試帶有 -easy 的程式。"""

    path = BASE_DIR / filename
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


MAIN = load_module("10242.py", "solution_10242")
EASY = load_module("10242-easy.py", "solution_10242_easy")


class Test10242(unittest.TestCase):
    def assert_solve(self, text: str, expected: str) -> None:
        self.assertEqual(MAIN.solve(text.encode()), expected)
        self.assertEqual(EASY.solve(text.encode()), expected)

    def test_sample_case(self) -> None:
        # 官方範例：最佳答案是 47。
        self.assert_solve(
            "6 7\n"
            "1 2\n"
            "2 3\n"
            "3 5\n"
            "2 4\n"
            "4 1\n"
            "2 6\n"
            "6 5\n"
            "10\n"
            "12\n"
            "8\n"
            "16\n"
            "1\n"
            "5\n"
            "1 4\n"
            "4 3 5 6\n",
            "47",
        )

    def test_scc_must_collect_entire_component(self) -> None:
        # 1 -> 2 -> 3，而 2 <-> 3 形成 SCC。
        # 起點只能先走到 SCC，再拿完 SCC 內的 ATM，最後去酒吧 4。
        self.assert_solve(
            "4 4\n"
            "1 2\n"
            "2 3\n"
            "3 2\n"
            "3 4\n"
            "5\n"
            "7\n"
            "11\n"
            "13\n"
            "1 1\n"
            "4\n",
            "36",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)