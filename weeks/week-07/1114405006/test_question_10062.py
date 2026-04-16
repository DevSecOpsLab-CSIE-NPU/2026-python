from __future__ import annotations

import random
import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SCRIPT_MAIN = BASE_DIR / "QUESTION-10062.py"
SCRIPT_EASY = BASE_DIR / "QUESTION-10062-easy.py"


def encode_input_from_permutation(perm: list[int]) -> str:
    """把排列轉成題目輸入格式。"""
    n = len(perm)
    lines = [str(n)]
    for i in range(1, n):
        current = perm[i]
        count_smaller_before = sum(1 for x in perm[:i] if x < current)
        lines.append(str(count_smaller_before))
    return "\n".join(lines) + "\n"


def expected_output(perm: list[int]) -> str:
    return "\n".join(map(str, perm))


def run_script(script_path: Path, input_data: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(script_path)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return completed.stdout.strip()


class TestQuestion10062(unittest.TestCase):
    def assert_both_scripts(self, input_data: str, expected: str) -> None:
        out_main = run_script(SCRIPT_MAIN, input_data)
        out_easy = run_script(SCRIPT_EASY, input_data)
        self.assertEqual(out_main, expected)
        self.assertEqual(out_easy, expected)

    def test_n1(self) -> None:
        self.assert_both_scripts("1\n", "1")

    def test_manual_case_1(self) -> None:
        # permutation = [3, 1, 2]
        input_data = "3\n0\n1\n"
        expected = "3\n1\n2"
        self.assert_both_scripts(input_data, expected)

    def test_manual_case_2(self) -> None:
        # permutation = [2, 1, 3]
        input_data = "3\n0\n2\n"
        expected = "2\n1\n3"
        self.assert_both_scripts(input_data, expected)

    def test_random_permutations(self) -> None:
        rng = random.Random(10062)
        for n in range(2, 10):
            for _ in range(20):
                perm = list(range(1, n + 1))
                rng.shuffle(perm)
                input_data = encode_input_from_permutation(perm)
                expected = expected_output(perm)
                self.assert_both_scripts(input_data, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
