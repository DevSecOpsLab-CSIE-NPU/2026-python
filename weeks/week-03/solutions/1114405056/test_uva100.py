import os
import random
import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA100(unittest.TestCase):
    """UVA 100（3n+1）題目的單元測試。"""

    @classmethod
    def setUpClass(cls):
        cls.test_dir = Path(__file__).resolve().parent
        # 預設測試同目錄下的 uva100-easy.py，也可用環境變數覆蓋。
        cls.solution_path = Path(
            os.environ.get("UVA100_SOLUTION", cls.test_dir / "uva100-easy.py")
        )

    def _cycle_length(self, n: int, memo: dict[int, int]) -> int:
        """使用記憶化計算單一數字的 cycle length。"""
        original_n = n
        seq = []

        while n not in memo:
            seq.append(n)
            if n % 2 == 1:
                n = 3 * n + 1
            else:
                n //= 2

        length = memo[n]
        for value in reversed(seq):
            length += 1
            memo[value] = length

        return memo[original_n]

    def _max_cycle(self, i: int, j: int) -> int:
        """計算區間 [min(i, j), max(i, j)] 的最大 cycle length。"""
        start, end = (i, j) if i <= j else (j, i)
        memo = {1: 1}
        return max(self._cycle_length(n, memo) for n in range(start, end + 1))

    def _expected_output(self, input_text: str) -> str:
        """根據題意生成期望輸出（每列輸出 i j max_cycle）。"""
        lines = []
        for line in input_text.strip().splitlines():
            i_str, j_str = line.split()
            i, j = int(i_str), int(j_str)
            lines.append(f"{i} {j} {self._max_cycle(i, j)}")
        return "\n".join(lines)

    def _run_solution(self, input_text: str) -> str:
        """以子行程執行受測程式，回傳標準輸出字串。"""
        if not self.solution_path.exists():
            self.skipTest(
                f"找不到受測程式：{self.solution_path}，"
                "請先建立解答檔，或設定 UVA100_SOLUTION。"
            )

        result = subprocess.run(
            [sys.executable, str(self.solution_path)],
            input=input_text,
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(
            result.returncode,
            0,
            msg=(
                "受測程式執行失敗。\n"
                f"return code: {result.returncode}\n"
                f"stderr:\n{result.stderr}"
            ),
        )

        # UVA 題目常忽略行尾空白，這裡用 strip() 避免格式細節造成誤判。
        return result.stdout.strip()

    def test_sample_cases(self):
        """驗證題目範例。"""
        input_text = "\n".join([
            "1 10",
            "100 200",
            "201 210",
            "900 1000",
        ])
        expected = "\n".join([
            "1 10 20",
            "100 200 125",
            "201 210 89",
            "900 1000 174",
        ])
        actual = self._run_solution(input_text)
        self.assertEqual(actual, expected)

    def test_reversed_interval(self):
        """驗證 i > j 時仍需正確計算，且輸出保留原始 i j。"""
        input_text = "10 1\n210 201"
        expected = self._expected_output(input_text)
        actual = self._run_solution(input_text)
        self.assertEqual(actual, expected)

    def test_random_small_ranges(self):
        """小範圍隨機測資，降低僅通過範例的風險。"""
        random.seed(100)
        pairs = [(random.randint(1, 300), random.randint(1, 300)) for _ in range(10)]
        input_text = "\n".join(f"{i} {j}" for i, j in pairs)
        expected = self._expected_output(input_text)
        actual = self._run_solution(input_text)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
