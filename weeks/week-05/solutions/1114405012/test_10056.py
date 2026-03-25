import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA10056(unittest.TestCase):
    """UVA 10056（玩家獲勝機率）測試。"""

    CANDIDATE_FILES = [
        "10056.py",
        "10056-easy.py",
        "10056-hand.py",
        "solution_10056.py",
        "main_10056.py",
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
            self.fail("找不到 10056 解答檔。")

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
    def expected(n, p, i):
        if p == 0:
            return 0.0
        q = 1.0 - p
        return (q ** (i - 1) * p) / (1.0 - q ** n)

    def test_basic_cases(self):
        cases = [
            (3, 0.5, 1),
            (3, 0.5, 2),
            (3, 0.5, 3),
            (5, 0.0, 4),
        ]

        lines = [str(len(cases))]
        lines.extend(f"{n} {p} {i}" for n, p, i in cases)
        input_data = "\n".join(lines) + "\n"

        output = self.run_solution(input_data)
        expected = [f"{self.expected(n, p, i):.4f}" for n, p, i in cases]
        self.assertEqual(output, expected)

    def test_known_value(self):
        # n=2, p=0.25, i=2
        # 公式結果：((0.75^1)*0.25)/(1-0.75^2)=0.428571...
        input_data = "1\n2 0.25 2\n"
        output = self.run_solution(input_data)
        self.assertEqual(output, ["0.4286"])

    def test_generated_cases(self):
        cases = []
        for n in range(2, 9):
            p = (n % 5 + 1) / 10.0
            i = (n % n) + 1
            cases.append((n, p, i))

        lines = [str(len(cases))]
        lines.extend(f"{n} {p} {i}" for n, p, i in cases)
        input_data = "\n".join(lines) + "\n"

        output = self.run_solution(input_data)
        expected = [f"{self.expected(n, p, i):.4f}" for n, p, i in cases]
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
