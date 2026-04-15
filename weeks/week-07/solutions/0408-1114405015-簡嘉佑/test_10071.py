"""
UVA 10071 - 正式版測試程式

這個檔案負責：
1. 測試 solution_10071.py 的核心函式正確性
2. 產生測試紀錄檔 test_10071.log
"""

from __future__ import annotations

from pathlib import Path
import unittest

from solution_10071 import count_six_tuples


def count_six_tuples_naive(values):
    """
    朴素法（O(N^6)）：
    只用來做小資料的正確性比對，避免正式解法寫錯卻不自知。
    """
    total = 0
    for a in values:
        for b in values:
            for c in values:
                for d in values:
                    for e in values:
                        for f in values:
                            if a + b + c + d + e == f:
                                total += 1
    return total


class TestSolution10071(unittest.TestCase):
    """正式版測試集合。"""

    def test_single_zero(self):
        # 僅有 (0,0,0,0,0,0) 一組
        self.assertEqual(count_six_tuples([0]), 1)

    def test_small_case_zero_one(self):
        arr = [0, 1]
        self.assertEqual(count_six_tuples(arr), count_six_tuples_naive(arr))

    def test_small_case_negative(self):
        arr = [-1, 0, 1]
        self.assertEqual(count_six_tuples(arr), count_six_tuples_naive(arr))

    def test_small_case_positive(self):
        arr = [1, 2, 3]
        self.assertEqual(count_six_tuples(arr), count_six_tuples_naive(arr))

    def test_scale_property(self):
        # 結構相同的集合做等比例縮放，解的個數應保持一致
        arr1 = [1, 2, 3]
        arr2 = [2, 4, 6]
        self.assertEqual(count_six_tuples(arr1), count_six_tuples(arr2))

    def test_medium_case_runs(self):
        # 中型資料主要確認程式可以順利跑完
        arr = list(range(-5, 10))
        ans = count_six_tuples(arr)
        self.assertIsInstance(ans, int)
        self.assertGreaterEqual(ans, 0)


def run_tests() -> bool:
    """執行測試並寫入 test_10071.log。"""
    log_path = Path(__file__).resolve().parent / "test_10071.log"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution10071)

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
