from __future__ import annotations

import itertools
import random
import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SCRIPT_MAIN = BASE_DIR / "QUESTION-10071.py"
SCRIPT_EASY = BASE_DIR / "QUESTION-10071-easy.py"


def build_input(values: list[int]) -> str:
    lines = [str(len(values))] + [str(x) for x in values]
    return "\n".join(lines) + "\n"


def brute_force_count(values: list[int]) -> int:
    total = 0
    for a, b, c, d, e, f in itertools.product(values, repeat=6):
        if a + b + c + d + e == f:
            total += 1
    return total


def run_script(script_path: Path, input_data: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(script_path)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return completed.stdout.strip()


class TestQuestion10071(unittest.TestCase):
    def assert_both_scripts(self, values: list[int]) -> None:
        input_data = build_input(values)
        expected = str(brute_force_count(values))
        out_main = run_script(SCRIPT_MAIN, input_data)
        out_easy = run_script(SCRIPT_EASY, input_data)
        self.assertEqual(out_main, expected)
        self.assertEqual(out_easy, expected)

    def test_single_zero(self) -> None:
        self.assert_both_scripts([0])

    def test_manual_positive(self) -> None:
        self.assert_both_scripts([1, 2])

    def test_manual_with_negative(self) -> None:
        self.assert_both_scripts([-1, 0, 1])

    def test_random_small_sets(self) -> None:
        rng = random.Random(10071)
        pool = list(range(-5, 6))
        for _ in range(20):
            n = rng.randint(1, 6)
            values = rng.sample(pool, n)
            self.assert_both_scripts(values)


if __name__ == "__main__":
    unittest.main(verbosity=2)
