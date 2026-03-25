import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA10057(unittest.TestCase):
    """UVA 10057（A mid-summer night's dream）測試。"""

    CANDIDATE_FILES = [
        "10057.py",
        "10057-easy.py",
        "10057-hand.py",
        "solution_10057.py",
        "main_10057.py",
    ]

    @classmethod
    def setUpClass(cls):
        cls.base_dir = Path(__file__).resolve().parent
        cls.solution_file = None
        for name in cls.CANDIDATE_FILES:
            path = cls.base_dir / name
            if path.exists():
                cls.solution_file = path
                break

    def run_solution(self, input_data: str):
        if self.solution_file is None:
            self.fail("找不到 10057 解答檔。")

        completed = subprocess.run(
            [sys.executable, str(self.solution_file)],
            input=input_data,
            text=True,
            capture_output=True,
            cwd=str(self.base_dir),
            check=False,
        )

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"程式執行失敗\nstderr:\n{completed.stderr}",
        )

        return [line.strip() for line in completed.stdout.splitlines() if line.strip()]

    @staticmethod
    def brute_force_line(arr):
        arr = sorted(arr)
        best = None
        candidates = []

        # 直接枚舉 A 的可能範圍（足夠覆蓋最優解）
        for a in range(arr[0], arr[-1] + 1):
            total = sum(abs(x - a) for x in arr)
            if best is None or total < best:
                best = total
                candidates = [a]
            elif total == best:
                candidates.append(a)

        smallest_a = candidates[0]
        count = sum(1 for x in arr if x in set(candidates))
        ways = len(candidates)
        return f"{smallest_a} {count} {ways}"

    def test_odd_case(self):
        input_data = "5\n1 2 2 3 4\n"
        output = self.run_solution(input_data)
        self.assertEqual(output, ["2 2 1"])

    def test_even_case(self):
        input_data = "4\n1 2 3 4\n"
        output = self.run_solution(input_data)
        self.assertEqual(output, ["2 2 2"])

    def test_multiple_cases(self):
        cases = [
            [1, 1, 2, 2, 3],
            [10, 20, 20, 30],
            [5, 5, 5, 5],
        ]

        lines = []
        for arr in cases:
            lines.append(str(len(arr)))
            lines.append(" ".join(map(str, arr)))
        input_data = "\n".join(lines) + "\n"

        output = self.run_solution(input_data)
        expected = [self.brute_force_line(arr) for arr in cases]
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
