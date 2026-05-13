"""
UVA 10908 — Largest Square 簡易版測試

測試目標：
1. 確認簡易版的核心函式可以正確回傳答案。
2. 確認主程式輸出和題目範例完全一致。

這份測試也刻意維持簡單，方便一起記。
"""

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("10908-easy.py")


def load_module():
    """依照檔案位置載入主程式，避免檔名含連字號時不能直接 import。"""
    spec = importlib.util.spec_from_file_location("u10908_easy", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestLargestSquareEasy(unittest.TestCase):
    """簡易版核心函式測試。"""

    @classmethod
    def setUpClass(cls):
        cls.module = load_module()

    def setUp(self):
        # 題目範例網格。
        self.grid = [
            list("abbbaaaaaa"),
            list("abbbaaaaaa"),
            list("abbbaaaaaa"),
            list("aaaaaaaaaa"),
            list("aaaaaaaaaa"),
            list("aaccaaaaaa"),
            list("aaccaaaaaa"),
        ]

    def test_example_1(self):
        """範例查詢點 1。"""
        self.assertEqual(self.module.largest_square(self.grid, 1, 2), 3)

    def test_example_2(self):
        """範例查詢點 2。"""
        self.assertEqual(self.module.largest_square(self.grid, 2, 4), 1)

    def test_example_3(self):
        """範例查詢點 3。"""
        self.assertEqual(self.module.largest_square(self.grid, 4, 6), 5)

    def test_example_4(self):
        """範例查詢點 4。"""
        self.assertEqual(self.module.largest_square(self.grid, 5, 2), 1)

    def test_single_cell(self):
        """只有一格時，答案一定是 1。"""
        grid = [list("x")]
        self.assertEqual(self.module.largest_square(grid, 0, 0), 1)

    def test_all_same_3x3(self):
        """整個 3x3 都相同時，答案是 3。"""
        grid = [
            list("aaa"),
            list("aaa"),
            list("aaa"),
        ]
        self.assertEqual(self.module.largest_square(grid, 1, 1), 3)

    def test_stop_at_boundary(self):
        """靠邊時不能超出範圍。"""
        grid = [
            list("aaaa"),
            list("aaaa"),
            list("aaaa"),
            list("aaaa"),
        ]
        self.assertEqual(self.module.largest_square(grid, 0, 0), 1)

    def test_stop_at_different_char(self):
        """遇到不同字元就停止。"""
        grid = [
            list("aaaaa"),
            list("aaaaa"),
            list("aabaa"),
            list("aaaaa"),
            list("aaaaa"),
        ]
        self.assertEqual(self.module.largest_square(grid, 2, 2), 1)


class TestMainProgramEasy(unittest.TestCase):
    """簡易版主程式輸出測試。"""

    def test_sample_output(self):
        """題目範例輸出要完全一致。"""
        input_data = """1
7 10 4
abbbaaaaaa
abbbaaaaaa
abbbaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaccaaaaaa
aaccaaaaaa
1 2
2 4
4 6
5 2
"""

        expected_output = """7 10 4
3
1
5
1
"""

        result = subprocess.run(
            [sys.executable, str(SCRIPT_PATH)],
            input=input_data,
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), expected_output.strip())


if __name__ == "__main__":
    unittest.main(verbosity=2)