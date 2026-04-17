import os
import subprocess
import sys
import unittest
from pathlib import Path


def inversion_count(arr: list[int]) -> int:
    """用定義直接計算反序對數量。"""
    total = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                total += 1
    return total


class TestUVA299(unittest.TestCase):
    """UVA 299（Train Swapping）測試。"""

    @classmethod
    def setUpClass(cls):
        cls.test_dir = Path(__file__).resolve().parent
        cls.solution_path = Path(
            os.environ.get("UVA299_SOLUTION", cls.test_dir / "uva299-easy.py")
        )

    def _run_solution(self, input_text: str) -> str:
        if not self.solution_path.exists():
            self.skipTest(f"找不到受測程式：{self.solution_path}")

        result = subprocess.run(
            [sys.executable, str(self.solution_path)],
            input=input_text,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        return result.stdout.strip()

    def test_known_cases(self):
        input_text = "\n".join(["3", "3", "1 3 2", "4", "4 3 2 1", "2", "1 2"])
        expected = "\n".join(
            [
                "Optimal train swapping takes 1 swaps.",
                "Optimal train swapping takes 6 swaps.",
                "Optimal train swapping takes 0 swaps.",
            ]
        )
        self.assertEqual(self._run_solution(input_text), expected)

    def test_generated_case(self):
        train = [3, 1, 4, 2, 5]
        expected_swaps = inversion_count(train)
        input_text = "\n".join(["1", str(len(train)), " ".join(map(str, train))])
        expected = f"Optimal train swapping takes {expected_swaps} swaps."
        self.assertEqual(self._run_solution(input_text), expected)


if __name__ == "__main__":
    unittest.main()
