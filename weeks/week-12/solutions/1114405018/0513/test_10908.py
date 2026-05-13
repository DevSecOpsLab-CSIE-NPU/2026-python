"""
UVA 10908 — Largest Square 單元測試

這份測試的目標是驗證：
1. 中心點本身就能形成邊長 1 的正方形。
2. 正方形可以正確往外擴張。
3. 遇到不同字元或邊界時會正確停止。
4. 主程式輸出格式符合題目要求。
"""

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("10908.py")


def load_module():
    """用檔案路徑載入主程式，避免檔名無法直接 import 的問題。"""
    spec = importlib.util.spec_from_file_location("u10908", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestLargestSquare(unittest.TestCase):
    """Largest Square 的功能測試。"""

    @classmethod
    def setUpClass(cls):
        cls.module = load_module()

    def test_sample_center_1(self):
        """測試範例中第一個查詢點。"""
        grid = [
            list("abbbaaaaaa"),
            list("abbbaaaaaa"),
            list("abbbaaaaaa"),
            list("aaaaaaaaaa"),
            list("aaaaaaaaaa"),
            list("aaccaaaaaa"),
            list("aaccaaaaaa"),
        ]
        self.assertEqual(self.module.largest_square(grid, 1, 2), 3)

    def test_sample_center_2(self):
        """測試範例中第二個查詢點。"""
        grid = [
            list("abbbaaaaaa"),
            list("abbbaaaaaa"),
            list("abbbaaaaaa"),
            list("aaaaaaaaaa"),
            list("aaaaaaaaaa"),
            list("aaccaaaaaa"),
            list("aaccaaaaaa"),
        ]
        self.assertEqual(self.module.largest_square(grid, 2, 4), 1)

    def test_sample_center_3(self):
        """測試範例中第三個查詢點。"""
        grid = [
            list("abbbaaaaaa"),
            list("abbbaaaaaa"),
            list("abbbaaaaaa"),
            list("aaaaaaaaaa"),
            list("aaaaaaaaaa"),
            list("aaccaaaaaa"),
            list("aaccaaaaaa"),
        ]
        self.assertEqual(self.module.largest_square(grid, 4, 6), 5)

    def test_sample_center_4(self):
        """測試範例中第四個查詢點。"""
        grid = [
            list("abbbaaaaaa"),
            list("abbbaaaaaa"),
            list("abbbaaaaaa"),
            list("aaaaaaaaaa"),
            list("aaaaaaaaaa"),
            list("aaccaaaaaa"),
            list("aaccaaaaaa"),
        ]
        self.assertEqual(self.module.largest_square(grid, 5, 2), 1)

    def test_single_cell_grid(self):
        """最小網格只能得到邊長 1。"""
        grid = [list("x")]
        self.assertEqual(self.module.largest_square(grid, 0, 0), 1)

    def test_all_same_square(self):
        """整個區域字元都相同時，應能擴到整個可行範圍。"""
        grid = [
            list("aaa"),
            list("aaa"),
            list("aaa"),
        ]
        self.assertEqual(self.module.largest_square(grid, 1, 1), 3)

    def test_near_boundary(self):
        """中心點靠近邊界時，不能超出網格。"""
        grid = [
            list("aaaa"),
            list("aaaa"),
            list("aaaa"),
            list("aaaa"),
        ]
        self.assertEqual(self.module.largest_square(grid, 0, 0), 1)

    def test_blocked_by_different_char(self):
        """外框只要出現不同字元，就必須停止。"""
        grid = [
            list("aaaaa"),
            list("aaaaa"),
            list("aabaa"),
            list("aaaaa"),
            list("aaaaa"),
        ]
        self.assertEqual(self.module.largest_square(grid, 2, 2), 1)


def run_sample_program_test():
    """用題目的範例輸入，確認主程式輸出格式與結果都正確。"""
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

    return result.stdout.strip(), expected_output.strip(), result.returncode


class TestMainProgram(unittest.TestCase):
    """主程式輸出測試。"""

    def test_sample_program_output(self):
        """題目範例的整體輸出應完全一致。"""
        actual_output, expected_output, return_code = run_sample_program_test()
        self.assertEqual(return_code, 0)
        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main(verbosity=2)