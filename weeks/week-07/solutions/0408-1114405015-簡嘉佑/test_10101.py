"""
測試程式：solution_10101.py

以「暴力驗證」搭配「輸出合法性檢查」測試正式版解法。
"""

from __future__ import annotations

from pathlib import Path
import unittest

from solution_10101 import solve_equation, STICKS


def is_true_equation(expr: str) -> bool:
    """檢查等式是否成立。"""
    try:
        left, right = expr.split("=", 1)
        return eval(left) == eval(right)
    except Exception:
        return False


def is_valid_move(original: str, candidate: str) -> bool:
    """檢查 candidate 是否可由 original 移動一根木棒得到。"""
    if len(original) != len(candidate):
        return False

    # 運算符位置不可改動
    for a, b in zip(original, candidate):
        if not a.isdigit() and a != b:
            return False

    diff_pos: list[int] = []
    for i, (a, b) in enumerate(zip(original, candidate)):
        if a != b:
            if not (a.isdigit() and b.isdigit()):
                return False
            diff_pos.append(i)

    # 必須剛好改兩個數字：一個 -1，一個 +1
    if len(diff_pos) != 2:
        return False

    d1 = STICKS[int(candidate[diff_pos[0]])] - STICKS[int(original[diff_pos[0]])]
    d2 = STICKS[int(candidate[diff_pos[1]])] - STICKS[int(original[diff_pos[1]])]
    return sorted([d1, d2]) == [-1, 1]


def brute_exists_solution(eq: str) -> bool:
    """暴力檢查是否至少存在一組解。"""
    pos = [i for i, ch in enumerate(eq) if ch.isdigit()]
    arr = list(eq)

    for i in pos:
        a = int(arr[i])
        for na in range(10):
            da = STICKS[na] - STICKS[a]
            if na == a or da != -1:
                continue

            arr1 = arr[:]
            arr1[i] = str(na)

            for j in pos:
                if j == i:
                    continue
                b = int(arr[j])
                for nb in range(10):
                    db = STICKS[nb] - STICKS[b]
                    if nb == b or db != 1:
                        continue

                    arr2 = arr1[:]
                    arr2[j] = str(nb)
                    cand = "".join(arr2)
                    if is_true_equation(cand):
                        return True

    return False


class TestSticks10101(unittest.TestCase):
    """正式版測試。"""

    def assert_solution_behavior(self, eq: str) -> None:
        """統一檢查：有解時回傳合法解；無解時回傳 None。"""
        expected_exists = brute_exists_solution(eq)
        got = solve_equation(eq)

        if not expected_exists:
            self.assertIsNone(got)
            return

        self.assertIsNotNone(got)
        self.assertTrue(is_valid_move(eq, got))
        self.assertTrue(is_true_equation(got))

    def test_case_1(self):
        self.assert_solution_behavior("2-1=0")

    def test_case_2(self):
        self.assert_solution_behavior("1+1=3")

    def test_case_3(self):
        self.assert_solution_behavior("7+1=0")

    def test_case_4(self):
        self.assert_solution_behavior("3+5=9")

    def test_case_5(self):
        self.assert_solution_behavior("9-4=6")

    def test_case_6(self):
        self.assert_solution_behavior("4+4=1")

    def test_case_7(self):
        self.assert_solution_behavior("0+0=1")

    def test_case_8(self):
        self.assert_solution_behavior("5+5=1")


def run_tests() -> bool:
    """執行所有測試並輸出 LOG。"""
    log_path = Path(__file__).resolve().parent / "test_10101.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestSticks10101)
    with log_path.open("w", encoding="utf-8") as log_file:
        runner = unittest.TextTestRunner(stream=log_file, verbosity=2)
        result = runner.run(suite)

        log_file.write("\n")
        log_file.write("=" * 60 + "\n")
        log_file.write(f"tests_run={result.testsRun}\n")
        log_file.write(f"failures={len(result.failures)}\n")
        log_file.write(f"errors={len(result.errors)}\n")
        log_file.write(f"success={result.wasSuccessful()}\n")

    print("Tests finished.")
    print(f"Log saved to: {log_path.name}")
    return result.wasSuccessful()


if __name__ == "__main__":
    ok = run_tests()
    raise SystemExit(0 if ok else 1)
