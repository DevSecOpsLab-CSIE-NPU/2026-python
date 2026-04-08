"""10093 單元測試（黑箱）。

測試策略：
1. 用 subprocess 驗證命令列輸入輸出。
2. 小尺寸地圖用 DFS + 記憶化做暴力真值。
3. 比對程式答案與真值是否一致。
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
import random
import subprocess
import sys
import unittest


class Test10093(unittest.TestCase):
    def setUp(self) -> None:
        # 目標程式路徑。
        self.root = Path(__file__).resolve().parents[1]
        self.script = self.root / "10093.py"
        if not self.script.exists():
            self.fail("找不到 10093.py")

    def run_case(self, grid: list[str]) -> int:
        # 輸入格式：N M + N 行地圖。
        n = len(grid)
        m = len(grid[0]) if n else 0
        inp = f"{n} {m}\n" + "\n".join(grid) + "\n"
        p = subprocess.run(
            [sys.executable, str(self.script)],
            input=inp,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(p.returncode, 0, msg=p.stderr)
        return int(p.stdout.strip())

    def brute(self, grid: list[str]) -> int:
        # 這個 brute 只用在小地圖測試，不追求大資料效率。
        n = len(grid)
        m = len(grid[0])

        row_ok = []
        for row in grid:
            mask = 0
            for c, ch in enumerate(row):
                if ch == "P":
                    mask |= 1 << c
            row_ok.append(mask)

        row_states = []
        for r in range(n):
            states = []
            for s in range(1 << m):
                if (s & row_ok[r]) != s:
                    continue
                if s & (s << 1):
                    continue
                if s & (s << 2):
                    continue
                states.append(s)
            row_states.append(states)

        @lru_cache(maxsize=None)
        def dfs(r: int, prev: int, prev2: int) -> int:
            # 逐列選狀態，並檢查與前一列、前二列是否衝突。
            if r == n:
                return 0
            best = 0
            for cur in row_states[r]:
                if cur & prev:
                    continue
                if cur & prev2:
                    continue
                best = max(best, bin(cur).count("1") + dfs(r + 1, cur, prev))
            return best

        return dfs(0, 0, 0)

    def test_fixed_cases(self):
        # 手動設計案例，覆蓋最小值、全平原、混合地形。
        cases = [
            ["P"],
            ["PPP"],
            ["PPP", "PPP"],
            ["PPP", "PPP", "PPP"],
            ["PHP", "HPH", "PHP"],
        ]
        for grid in cases:
            with self.subTest(grid=grid):
                self.assertEqual(self.run_case(grid), self.brute(grid))

    def test_random_small_cases(self):
        # 隨機小案例，避免只對固定樣本過擬合。
        rnd = random.Random(20260408)
        for _ in range(6):
            n = rnd.randint(2, 5)
            m = rnd.randint(2, 5)
            grid = []
            for _r in range(n):
                row = "".join(rnd.choice(["P", "H"]) for _c in range(m))
                grid.append(row)
            with self.subTest(grid=grid):
                self.assertEqual(self.run_case(grid), self.brute(grid))


if __name__ == "__main__":
    unittest.main()
