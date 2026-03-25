import subprocess
import sys
import unittest
from pathlib import Path


class Test10055(unittest.TestCase):
    """題號 10055（函數增減性區間查詢）測試。"""

    CANDIDATE_FILES = [
        "10055.py",
        "10055-easy.py",
        "10055-hand.py",
        "solution_10055.py",
        "main_10055.py",
    ]

    @classmethod
    def setUpClass(cls):
        cls.base_dir = Path(__file__).resolve().parent
        cls.solution_file = None
        for name in cls.CANDIDATE_FILES:
            p = cls.base_dir / name
            if p.exists():
                cls.solution_file = p
                break

    def run_solution(self, input_data: str):
        if self.solution_file is None:
            self.fail("找不到 10055 解答檔。")

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
    def brute_force(n, operations):
        """用直接模擬驗證答案：1=增，-1=減，乘積決定增減性。"""
        signs = [1] * (n + 1)
        result = []
        for op in operations:
            if op[0] == 1:
                signs[op[1]] *= -1
            else:
                l, r = op[1], op[2]
                product = 1
                for i in range(l, r + 1):
                    product *= signs[i]
                result.append("0" if product == 1 else "1")
        return result

    def test_basic_toggle_and_query(self):
        # 初始都為增（0）
        # flip 2 後，查 1..3 應為減（1）
        input_data = "\n".join([
            "3 4",
            "2 1 3",
            "1 2",
            "2 1 3",
            "2 2 2",
        ]) + "\n"

        output = self.run_solution(input_data)
        self.assertEqual(output, ["0", "1", "1"])

    def test_multiple_operations(self):
        n = 6
        operations = [
            (2, 1, 6),
            (1, 3),
            (2, 1, 6),
            (1, 4),
            (2, 2, 5),
            (1, 3),
            (2, 1, 4),
            (2, 4, 4),
        ]

        lines = [f"{n} {len(operations)}"]
        for op in operations:
            lines.append(" ".join(map(str, op)))
        input_data = "\n".join(lines) + "\n"

        expected = self.brute_force(n, operations)
        output = self.run_solution(input_data)
        self.assertEqual(output, expected)

    def test_generated_cases(self):
        n = 10
        operations = []

        # 建立規律操作：交錯翻轉與查詢
        for i in range(1, 8):
            operations.append((1, (i * 3) % n + 1))
            l = (i % n) + 1
            r = ((i * 2) % n) + 1
            if l > r:
                l, r = r, l
            operations.append((2, l, r))

        lines = [f"{n} {len(operations)}"]
        for op in operations:
            lines.append(" ".join(map(str, op)))
        input_data = "\n".join(lines) + "\n"

        expected = self.brute_force(n, operations)
        output = self.run_solution(input_data)
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
