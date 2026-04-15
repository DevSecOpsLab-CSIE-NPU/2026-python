"""
UVA 10071 - easy 版測試程式

用途：
1. 測試 solution_10071-easy.py 的正確性
2. 產生測試紀錄檔 test_10071-easy.log
"""

from __future__ import annotations

from pathlib import Path
import importlib.util
import unittest


def _load_easy_solver():
    """動態載入 solution_10071-easy.py，避免檔名含 '-' 造成 import 問題。"""
    file_path = Path(__file__).resolve().parent / "solution_10071-easy.py"
    spec = importlib.util.spec_from_file_location("solution_10071_easy_module", file_path)
    if spec is None or spec.loader is None:
        raise ImportError("無法載入 solution_10071-easy.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.count_six_tuples_easy


count_six_tuples_easy = _load_easy_solver()


def count_six_tuples_naive(values):
    """朴素法 O(N^6)，只用在小測試驗證。"""
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


class TestEasy(unittest.TestCase):
    def test_single_zero(self):
        self.assertEqual(count_six_tuples_easy([0]), 1)

    def test_small_set_1(self):
        arr = [0, 1]
        self.assertEqual(count_six_tuples_easy(arr), count_six_tuples_naive(arr))

    def test_small_set_2(self):
        arr = [-1, 0, 1]
        self.assertEqual(count_six_tuples_easy(arr), count_six_tuples_naive(arr))

    def test_small_set_3(self):
        arr = [1, 2, 3]
        self.assertEqual(count_six_tuples_easy(arr), count_six_tuples_naive(arr))


def run_tests() -> bool:
    log_path = Path(__file__).resolve().parent / "test_10071-easy.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestEasy)
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
