"""
UVA 948 - 假幣偵測 easy 版單元測試

從 solution_948-easy.py 動態載入 solve 函式進行測試。
（因為檔名含有 '-' 符號，無法用 import 直接匯入，改用 importlib 動態載入）

涵蓋：
  - 假幣偏輕在左側
  - 假幣偏重在右側
  - 等重結果排除候選
  - 資訊不足 → 輸出 0
  - 邊界：N=1 無秤重
  - 全部等重 → 假幣是未秤到的硬幣
  - 多次秤重唯一確定
"""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


# ===========================================================
# 動態載入 solution_948-easy.py（因為檔名含 '-'）
# ===========================================================

def _load_easy_module():
    """動態載入與本測試檔同目錄的 solution_948-easy.py。"""
    module_path = Path(__file__).resolve().parent / "solution_948-easy.py"
    spec = importlib.util.spec_from_file_location("solution_948_easy", module_path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_easy = _load_easy_module()
# 取得 easy 版的核心解題函式
solve = _easy.solve


# ===========================================================
# 測試案例
# ===========================================================

class TestFakeCoin948Easy(unittest.TestCase):
    """UVA 948 假幣偵測測試（測試 solution_948-easy.solve）。"""

    def test_fake_is_light_left_side(self):
        """
        假幣偏輕在左側：兩組秤重均顯示左輕，只有 1 號硬幣偏輕同時滿足。
        """
        weighings = [([1], [2], "<"), ([1], [3], "<")]
        self.assertEqual(solve(3, weighings), 1)

    def test_fake_is_heavy_right_side(self):
        """
        假幣偏重在右側：兩組秤重均顯示左輕右重，只有 3 號硬幣偏重同時滿足。
        """
        weighings = [([1], [3], "<"), ([2], [3], "<")]
        self.assertEqual(solve(3, weighings), 3)

    def test_equal_result_eliminates_coins(self):
        """
        等重排除 1,2 為真幣，再利用不等重確認 3 偏輕。
        """
        weighings = [
            ([1], [2], "="),
            ([3], [4], "<"),
            ([3], [1], "<"),
        ]
        self.assertEqual(solve(4, weighings), 3)

    def test_ambiguous_returns_zero(self):
        """
        只有一次秤重，候選有多個 → 輸出 0。
        """
        weighings = [([1, 2], [3, 4], "<")]
        self.assertEqual(solve(4, weighings), 0)

    def test_single_coin(self):
        """
        N=1 無秤重：唯一一枚即為假幣 → 輸出 1。
        """
        self.assertEqual(solve(1, []), 1)

    def test_heavy_fake_coin(self):
        """
        假幣偏重（硬幣 2），兩組秤重均顯示左重 (>)。
        """
        weighings = [([2], [1], ">"), ([2], [3], ">")]
        self.assertEqual(solve(3, weighings), 2)

    def test_all_equal_weighings(self):
        """
        全部等重 → 假幣不在任何秤重的硬幣中，N=5 時假幣必定是 5。
        """
        weighings = [
            ([1], [2], "="),
            ([3], [4], "="),
            ([1, 3], [2, 4], "="),
        ]
        self.assertEqual(solve(5, weighings), 5)

    def test_multiple_weighings_unique_answer(self):
        """
        三次秤重後唯一確定假幣為 4 號（偏重）。
        """
        weighings = [
            ([1, 2], [3, 4], "<"),
            ([1, 3], [2, 4], "<"),
            ([4],    [5],    ">"),
        ]
        self.assertEqual(solve(6, weighings), 4)


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並將結果寫入 test_948-easy.log。"""
    log_path = Path(__file__).resolve().parent / "test_948-easy.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestFakeCoin948Easy)
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
