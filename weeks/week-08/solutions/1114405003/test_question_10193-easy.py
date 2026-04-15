import math
import os
import subprocess
import sys
import unittest
from pathlib import Path


# ============================================================
# 10193 好記版核心口訣：
# 1) 先算 n = a^2 + 1
# 2) 找 n 的因數配對 d, e（d * e = n）
# 3) b + c = 2a + d + e，取最小值
# ============================================================


def find_target_script() -> Path:
    """找 10193 解答檔，找不到就跳過測試。"""
    custom_path = os.environ.get("TARGET_10193")
    if custom_path:
        p = Path(custom_path)
        if p.exists():
            return p

    folder = Path(__file__).resolve().parent
    names = [
        "QUESTION-10193-手打.py",
        "QUESTION-10193.py",
        "question_10193.py",
        "uva10193.py",
        "10193.py",
        "solution_10193.py",
    ]
    for name in names:
        p = folder / name
        if p.exists():
            return p

    raise unittest.SkipTest("找不到 10193 解答檔，請放同資料夾或設定 TARGET_10193")


def run_program(a: int) -> int:
    """把 a 餵給解答程式，回傳程式輸出的 b+c。"""
    script = find_target_script()
    result = subprocess.run(
        [sys.executable, str(script)],
        input=f"{a}\n",
        text=True,
        capture_output=True,
        check=True,
    )
    return int(result.stdout.strip())


def expected_min_sum(a: int) -> int:
    """用數學推導後的簡單枚舉法算正確答案。"""
    n = a * a + 1
    best = None

    # 只要檢查到 sqrt(n) 即可，另一半會由配對因數補齊。
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0:
            e = n // d
            value = 2 * a + d + e
            if best is None or value < best:
                best = value

    assert best is not None
    return best


class Test10193Easy(unittest.TestCase):
    """UVA 10193（arctan）好記版測試。"""

    def test_small_numbers(self):
        # 先驗小數值，方便快速檢查基本邏輯。
        for a in [1, 2, 3, 4, 5, 10]:
            with self.subTest(a=a):
                self.assertEqual(run_program(a), expected_min_sum(a))

    def test_scattered_numbers(self):
        # 幾個分散值，避免只對連續小範圍有效。
        for a in [37, 99, 256, 1024, 12345]:
            with self.subTest(a=a):
                self.assertEqual(run_program(a), expected_min_sum(a))

    def test_upper_bound(self):
        # 題目上限 a=60000 也應該正確。
        a = 60000
        self.assertEqual(run_program(a), expected_min_sum(a))


if __name__ == "__main__":
    unittest.main()
