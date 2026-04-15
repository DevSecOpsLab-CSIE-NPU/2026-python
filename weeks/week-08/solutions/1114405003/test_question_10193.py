import math
import os
import subprocess
import sys
import unittest
from pathlib import Path


def _find_solution_script() -> Path:
    """尋找 10193 解答程式位置；可由環境變數覆寫。"""
    custom = os.environ.get("TARGET_10193")
    if custom:
        p = Path(custom)
        if p.exists():
            return p

    base = Path(__file__).resolve().parent
    candidates = [
        "QUESTION-10193-手打.py",
        "QUESTION-10193.py",
        "question_10193.py",
        "uva10193.py",
        "10193.py",
        "solution_10193.py",
    ]
    for name in candidates:
        p = base / name
        if p.exists():
            return p

    raise unittest.SkipTest("找不到 10193 解答程式，請先放入同資料夾或設定 TARGET_10193")


def _run_solution(a: int) -> int:
    script = _find_solution_script()
    proc = subprocess.run(
        [sys.executable, str(script)],
        input=f"{a}\n",
        text=True,
        capture_output=True,
        check=True,
    )
    out = proc.stdout.strip()
    return int(out)


def _reference_min_sum(a: int) -> int:
    # 由 arctan 恆等式可化為 (b-a)(c-a)=a^2+1，枚舉因數找最小 b+c。
    n = a * a + 1
    best = None
    root = int(math.isqrt(n))
    for d in range(1, root + 1):
        if n % d == 0:
            e = n // d
            val = 2 * a + d + e
            if best is None or val < best:
                best = val
    assert best is not None
    return best


class TestQuestion10193(unittest.TestCase):
    """UVA 10193 測試：驗證最小 b+c 是否正確。"""

    def test_small_known_values(self):
        for a in [1, 2, 3, 4, 5, 10]:
            with self.subTest(a=a):
                self.assertEqual(_run_solution(a), _reference_min_sum(a))

    def test_large_value(self):
        a = 60000
        self.assertEqual(_run_solution(a), _reference_min_sum(a))

    def test_random_style_values(self):
        # 固定幾個分散值，檢查演算法泛化能力。
        for a in [37, 99, 256, 1024, 12345]:
            with self.subTest(a=a):
                self.assertEqual(_run_solution(a), _reference_min_sum(a))


if __name__ == "__main__":
    unittest.main()
