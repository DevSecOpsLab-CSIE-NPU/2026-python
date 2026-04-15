"""
測試程式：solution_10170-easy.py

easy 版測試（較少案例），並保留 log。
"""

from __future__ import annotations

from pathlib import Path
import unittest
import importlib.util


def load_easy_module():
    """動態載入檔名含 '-' 的 easy 解答檔。"""
    path = Path(__file__).resolve().parent / "solution_10170-easy.py"
    spec = importlib.util.spec_from_file_location("solution_10170_easy", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


easy = load_easy_module()


def brute_solve(s: int, d: int) -> int:
    people = s
    days = 0
    while True:
        days += people
        if days >= d:
            return people
        people += 1


class TestHotel10170Easy(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(easy.solve(4, 10), 6)

    def test_case_2(self):
        self.assertEqual(easy.solve(1, 1), 1)

    def test_case_3(self):
        self.assertEqual(easy.solve(7, 8), 8)

    def test_case_4(self):
        for s, d in [(2, 3), (3, 20), (10, 100), (12, 300)]:
            self.assertEqual(easy.solve(s, d), brute_solve(s, d))


def run_tests() -> bool:
    """執行所有測試並輸出 LOG。"""
    log_path = Path(__file__).resolve().parent / "test_10170-easy.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestHotel10170Easy)
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
