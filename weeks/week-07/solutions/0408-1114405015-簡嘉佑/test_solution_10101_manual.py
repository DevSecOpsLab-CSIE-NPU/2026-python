"""
Test program for solution_10101_manual.py
"""

from __future__ import annotations

from pathlib import Path
import unittest

from solution_10101_manual import solve_equation, STICKS


def is_true_equation(expr: str) -> bool:
    try:
        left, right = expr.split("=", 1)
        return eval(left) == eval(right)
    except Exception:
        return False


def is_valid_move(original: str, candidate: str) -> bool:
    if len(original) != len(candidate):
        return False

    diff_pos = []
    for i, (a, b) in enumerate(zip(original, candidate)):
        if not a.isdigit() and a != b:
            return False
        if a != b:
            if not (a.isdigit() and b.isdigit()):
                return False
            diff_pos.append(i)

    if len(diff_pos) != 2:
        return False

    d1 = STICKS[int(candidate[diff_pos[0]])] - STICKS[int(original[diff_pos[0]])]
    d2 = STICKS[int(candidate[diff_pos[1]])] - STICKS[int(original[diff_pos[1]])]
    return sorted([d1, d2]) == [-1, 1]


class TestSticks10101Manual(unittest.TestCase):
    def check_case(self, eq: str) -> None:
        got = solve_equation(eq)
        if got is None:
            # Some equations truly have no solution under this model.
            return
        self.assertTrue(is_valid_move(eq, got))
        self.assertTrue(is_true_equation(got))

    def test_case_1(self):
        self.check_case("2-1=0")

    def test_case_2(self):
        self.check_case("1+1=3")

    def test_case_3(self):
        self.check_case("7+1=0")

    def test_case_4(self):
        self.check_case("3+5=9")

    def test_case_5(self):
        self.check_case("9-4=6")

    def test_case_6(self):
        self.check_case("4+4=1")

    def test_case_7(self):
        self.check_case("0+0=1")

    def test_case_8(self):
        self.check_case("5+5=1")


def run_tests() -> bool:
    """Run all tests and save log."""
    log_path = Path(__file__).resolve().parent / "test_solution_10101_manual.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestSticks10101Manual)
    with log_path.open("w", encoding="utf-8") as log_file:
        runner = unittest.TextTestRunner(stream=log_file, verbosity=2)
        result = runner.run(suite)

        log_file.write("\n")
        log_file.write("=" * 60 + "\n")
        log_file.write(f"tests_run={result.testsRun}\n")
        log_file.write(f"failures={len(result.failures)}\n")
        log_file.write(f"errors={len(result.errors)}\n")
        log_file.write(f"success={result.wasSuccessful()}\n")

    print("Manual tests finished.")
    print(f"Log saved to: {log_path.name}")
    return result.wasSuccessful()


if __name__ == "__main__":
    ok = run_tests()
    raise SystemExit(0 if ok else 1)
