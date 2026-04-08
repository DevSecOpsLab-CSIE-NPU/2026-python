"""10071 單元測試（黑箱）。

測試重點：
1. 以 subprocess 呼叫目標程式，檢查命令列 I/O。
2. 小資料用暴力枚舉 6 重迴圈當作真值。
3. 對照程式輸出與暴力結果是否一致。
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import subprocess
import sys
import unittest


class Test10071(unittest.TestCase):
    def setUp(self) -> None:
        # 目標程式固定放在 tests 上一層目錄。
        self.root = Path(__file__).resolve().parents[1]
        self.script = self.root / "10071.py"
        if not self.script.exists():
            self.fail("找不到 10071.py")

    def run_case(self, values: list[int]) -> int:
        # 輸入格式：N + N 行元素。
        inp = str(len(values)) + "\n" + "\n".join(map(str, values)) + "\n"
        p = subprocess.run(
            [sys.executable, str(self.script)],
            input=inp,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(p.returncode, 0, msg=p.stderr)
        return int(p.stdout.strip())

    def brute(self, values: list[int]) -> int:
        # 直接暴力枚舉所有有序六元組，作為正確答案基準。
        ans = 0
        for a, b, c, d, e, f in product(values, repeat=6):
            if a + b + c + d + e == f:
                ans += 1
        return ans

    def test_small_set_01(self):
        values = [0]
        self.assertEqual(self.run_case(values), self.brute(values))

    def test_small_set_02(self):
        values = [0, 1]
        self.assertEqual(self.run_case(values), self.brute(values))

    def test_small_set_03(self):
        values = [-1, 0, 1]
        self.assertEqual(self.run_case(values), self.brute(values))

    def test_small_set_04(self):
        values = [2, 3, 5]
        self.assertEqual(self.run_case(values), self.brute(values))


if __name__ == "__main__":
    unittest.main()
