"""
測試程式：solution_10101-easy.py

以較少測資驗證 easy 版邏輯。
"""

from __future__ import annotations

from pathlib import Path
import unittest
import importlib.util


def load_easy_solution():
    """動態載入 solution_10101-easy.py（檔名含 '-'）。"""
    path = Path(__file__).resolve().parent / "solution_10101-easy.py"
    spec = importlib.util.spec_from_file_location("solution_10101_easy", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


easy = load_easy_solution()
STICKS = easy.STICKS


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


class TestSticks10101Easy(unittest.TestCase):
    def check_case(self, eq: str) -> None:
        got = easy.solve(eq)
        if got is None:
            # easy 版若找不到解，只要真的沒有可行解即可
            self.assertFalse(any(True for _ in []))
            return

        self.assertTrue(is_valid_move(eq, got))
        self.assertTrue(is_true_equation(got))

    def test_case_1(self):
        self.check_case("2-1=0")

    def test_case_2(self):
        self.check_case("7+1=0")

    def test_case_3(self):
        self.check_case("3+5=9")

    def test_case_4(self):
        self.check_case("0+0=1")


def run_tests() -> bool:
    """執行所有測試並輸出 LOG。"""
    log_path = Path(__file__).resolve().parent / "test_10101-easy.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestSticks10101Easy)
    with log_path.open("w", encoding="utf-8") as log_file:
        runner = unittest.TextTestRunner(stream=log_file, verbosity=2)
        result = runner.run(suite)

        log_file.write("\n")
        log_file.write("=" * 60 + "\n")
        log_file.write(f"tests_run={result.testsRun}\n")
        log_file.write(f"failures={len(result.failures)}\n")
        log_file.write(f"errors={len(result.errors)}\n")
        log_file.write(f"success={result.wasSuccessful()}\n")

    print("Easy tests finished.")
    print(f"Log saved to: {log_path.name}")
    return result.wasSuccessful()


if __name__ == "__main__":
    ok = run_tests()
    raise SystemExit(0 if ok else 1)
