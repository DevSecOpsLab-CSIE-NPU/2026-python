from __future__ import annotations

import random
import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SCRIPT_MAIN = BASE_DIR / "QUESTION-10170.py"
SCRIPT_EASY = BASE_DIR / "QUESTION-10170-easy.py"


def run_script(script_path: Path, input_data: str) -> str:
    cp = subprocess.run(
        [sys.executable, str(script_path)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return cp.stdout.strip()


def brute_answer(s: int, d: int) -> int:
    cur = s
    total = 0
    while True:
        total += cur
        if total >= d:
            return cur
        cur += 1


class TestQuestion10170(unittest.TestCase):
    def assert_both_scripts(self, pairs: list[tuple[int, int]]) -> None:
        input_data = "\n".join(f"{s} {d}" for s, d in pairs) + "\n"
        expected = "\n".join(str(brute_answer(s, d)) for s, d in pairs)
        out_main = run_script(SCRIPT_MAIN, input_data)
        out_easy = run_script(SCRIPT_EASY, input_data)
        self.assertEqual(out_main, expected)
        self.assertEqual(out_easy, expected)

    def test_manual_cases(self) -> None:
        pairs = [(1, 1), (1, 3), (3, 10), (4, 7)]
        self.assert_both_scripts(pairs)

    def test_random_small(self) -> None:
        rng = random.Random(10170)
        pairs = []
        for _ in range(30):
            s = rng.randint(1, 20)
            d = rng.randint(1, 200)
            pairs.append((s, d))
        self.assert_both_scripts(pairs)


if __name__ == "__main__":
    unittest.main(verbosity=2)
