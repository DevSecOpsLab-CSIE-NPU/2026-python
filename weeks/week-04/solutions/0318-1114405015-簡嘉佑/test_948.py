"""
UVA 948 - 假幣偵測 單元測試（測試 solution_948.py）

題目重點：
  - 有 N 枚硬幣，其中一枚是假的（重量不同，可能偏輕或偏重）。
  - 共進行 K 次天平秤重，每次記錄「左邊硬幣編號、右邊硬幣編號、結果（< > =）」。
  - 目標：找出假幣的「編號」。
  - 若無法唯一確定，輸出 0。

解題思路：
  1. 對每枚硬幣，假設「它是假幣且偏輕」或「它是假幣且偏重」，共 2N 種情境。
  2. 逐一驗證該情境是否與所有秤重結果一致。
  3. 只有唯一一種「硬幣 + 偏輕/偏重」同時通過所有驗證，才回傳該硬幣編號；
     否則回傳 0。

測試策略：
  - 用小型手算案例確認輸出。
  - 測試「左邊輕（<）」、「左邊重（>）」、「兩邊等重（=）」三種狀況。
  - 測試無法唯一確定的情形。
  - 測試邊界：N=1、K=1、大量秤重結果互相矛盾。
"""

from __future__ import annotations

import unittest
from pathlib import Path

# 從正式版解答匯入受測函式
from solution_948 import find_fake_coin


# ===========================================================
# 測試案例
# ===========================================================

class TestFakeCoin948(unittest.TestCase):
    """UVA 948 假幣偵測測試。"""

    def test_fake_is_light_left_side(self):
        """
        左邊放假幣（偏輕），結果 < → 找出假幣在左邊。
        N=3，硬幣 1 2 3，秤重：左=[1]，右=[2]，結果=<
        假幣是 1（偏輕）。
        """
        weighings = [([1], [2], "<")]
        # 1 在左側且偏輕 → 一致
        # 2 在右側且偏重 → 也一致
        # 不確定，但若加一組秤重就可以排除
        weighings2 = [([1], [2], "<"), ([1], [3], "<")]
        # 只有硬幣 1 偏輕同時滿足兩組 → 答案 1
        result = find_fake_coin(3, weighings2)
        self.assertEqual(result, 1)

    def test_fake_is_heavy_right_side(self):
        """
        右邊放假幣（偏重），結果 < → 左輕右重。
        N=3，秤重組合讓硬幣 3 唯一可能。
        """
        weighings = [([1], [3], "<"), ([2], [3], "<")]
        # 只有硬幣 3 偏重同時滿足 → 答案 3
        result = find_fake_coin(3, weighings)
        self.assertEqual(result, 3)

    def test_equal_result_eliminates_coins(self):
        """
        兩次等重 + 一次不等，縮小候選。
        N=4，前兩次 1vs2=, 3vs4<，只有硬幣 3（偏輕）或 4（偏重）。
        再加 3vs1< 確認 3 偏輕。
        """
        weighings = [
            ([1], [2], "="),  # 1,2 都是真幣
            ([3], [4], "<"),  # 3 或 4 是假幣
            ([3], [1], "<"),  # 3 比真幣輕 → 3 偏輕
        ]
        result = find_fake_coin(4, weighings)
        self.assertEqual(result, 3)

    def test_ambiguous_returns_zero(self):
        """
        秤重資訊不足，無法唯一確定 → 應回傳 0。
        只一次秤重且左輕，可能是左邊任意一枚偏輕，或右邊任意一枚偏重。
        """
        weighings = [([1, 2], [3, 4], "<")]
        result = find_fake_coin(4, weighings)
        self.assertEqual(result, 0)

    def test_single_coin(self):
        """
        N=1：只有一枚硬幣，必定是假幣。
        但題目保證 Pi <= N/2，N=1 時無法秤重，K=0 → 唯一候選即 1。
        """
        result = find_fake_coin(1, [])
        # 無任何秤重，所有硬幣都是候選（只有 1 枚）→ 答案 1
        self.assertEqual(result, 1)

    def test_heavy_fake_coin(self):
        """
        假幣偏重，右邊結果 > 表示左重右輕的情境。
        N=3, 秤重: [2] vs [1] = >, [2] vs [3] = >
        → 硬幣 2 偏重是唯一一致解。
        """
        weighings = [([2], [1], ">"), ([2], [3], ">")]
        result = find_fake_coin(3, weighings)
        self.assertEqual(result, 2)

    def test_all_equal_weighings(self):
        """
        所有秤重結果都是 = → 假幣不在任何一次秤重的硬幣中。
        N=5，秤重只涉及 1,2,3,4 → 假幣是 5。
        """
        weighings = [
            ([1], [2], "="),
            ([3], [4], "="),
            ([1, 3], [2, 4], "="),
        ]
        result = find_fake_coin(5, weighings)
        self.assertEqual(result, 5)

    def test_multiple_weighings_unique_answer(self):
        """
        多次秤重後可唯一確定假幣（N=6，答案=4 偏輕）。
        """
        weighings = [
            ([1, 2], [3, 4], "<"),  # 4 偏重 or 1,2 偏輕 or 3 偏重
            ([1, 3], [2, 4], "<"),  # 縮小候選
            ([4], [5], ">"),        # 4 比真幣重 → 4 偏重
        ]
        # 驗證 4 偏重是否一致
        result = find_fake_coin(6, weighings)
        self.assertEqual(result, 4)


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並將結果寫入 test_948.log。"""
    log_path = Path(__file__).resolve().parent / "test_948.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestFakeCoin948)
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
