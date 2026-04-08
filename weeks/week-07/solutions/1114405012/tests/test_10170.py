"""10170 單元測試（黑箱）。

測試策略：
1. 程式輸出與模擬法答案比對。
2. 同時驗證多筆輸入（EOF）格式。
3. 覆蓋一般案例與大數案例。
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import unittest


class Test10170(unittest.TestCase):
    def setUp(self) -> None:
        # 目標程式位置。
        self.root = Path(__file__).resolve().parents[1]
        self.script = self.root / "10170.py"
        if not self.script.exists():
            self.fail("找不到 10170.py")

    def run_case(self, pairs: list[tuple[int, int]]) -> list[int]:
        # 多筆輸入一次餵入，模擬題目 EOF 格式。
        inp = "\n".join(f"{s} {d}" for s, d in pairs) + "\n"
        p = subprocess.run(
            [sys.executable, str(self.script)],
            input=inp,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(p.returncode, 0, msg=p.stderr)
        return list(map(int, p.stdout.strip().splitlines())) if p.stdout.strip() else []

    def simulate(self, s: int, d: int) -> int:
        # 線性模擬（作為測試真值），只用於測試資料量。
        day = 0
        group = s
        while True:
            day += group
            if day >= d:
                return group
            group += 1

    def test_known_cases(self):
        pairs = [(1, 1), (1, 3), (3, 10), (4, 4), (4, 5)]
        expected = [self.simulate(s, d) for s, d in pairs]
        self.assertEqual(self.run_case(pairs), expected)

    def test_large_case(self):
        pairs = [(10000, 10**12)]
        expected = [self.simulate(10000, 10**12)]
        self.assertEqual(self.run_case(pairs), expected)


if __name__ == "__main__":
    unittest.main()
