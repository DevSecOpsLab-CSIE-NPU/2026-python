"""
UVA 118 - Mutant Flatworld Explorers 單元測試

題意摘要：
  - 世界是矩形，左下角固定為 (0,0)，右上角為 (max_x, max_y)。
  - 機器人有位置 (x,y) 與朝向（N/E/S/W）。
  - 指令：
      L -> 左轉 90 度
      R -> 右轉 90 度
      F -> 朝目前方向前進一格
  - 若前進後會離開邊界：
      1) 該機器人會 LOST
      2) 在掉落前最後位置留下 scent（標記）
      3) 之後若有機器人在同一格、同樣要往外走，會忽略該次 F（不掉落）

本測試檔用途：
  1. 驗證單一機器人指令執行是否正確。
  2. 驗證邊界掉落與 scent 規則。
  3. 驗證多機器人依序執行時 scent 會被後續機器人使用。
"""

from __future__ import annotations

import unittest
from pathlib import Path

# 從正式版解答匯入受測函式
from solution_118 import (
    format_robot_result,
    simulate_robot,
    turn_left,
    turn_right,
)


# ===========================================================
# 測試案例
# ===========================================================

class TestUVA118(unittest.TestCase):
    """UVA 118 核心規則測試。"""

    def test_turn_left_right_cycle(self):
        """旋轉規則應符合 N-E-S-W 循環。"""
        self.assertEqual(turn_left("N"), "W")
        self.assertEqual(turn_right("N"), "E")
        d = "N"
        for _ in range(4):
            d = turn_right(d)
        self.assertEqual(d, "N")

    def test_simple_move_inside(self):
        """在邊界內前進，不應 LOST。"""
        scents: set[tuple[int, int, str]] = set()
        x, y, d, lost = simulate_robot(5, 3, 1, 1, "E", "F", scents)
        self.assertEqual((x, y, d, lost), (2, 1, "E", False))

    def test_lost_at_boundary(self):
        """向外前進應 LOST，並停在掉落前位置。"""
        scents: set[tuple[int, int, str]] = set()
        x, y, d, lost = simulate_robot(5, 3, 5, 3, "N", "F", scents)
        self.assertEqual((x, y, d, lost), (5, 3, "N", True))
        self.assertIn((5, 3, "N"), scents)

    def test_scent_blocks_same_fall(self):
        """同一格同方向的掉落，後續機器人應忽略 F。"""
        scents: set[tuple[int, int, str]] = {(5, 3, "N")}
        x, y, d, lost = simulate_robot(5, 3, 5, 3, "N", "F", scents)
        self.assertEqual((x, y, d, lost), (5, 3, "N", False))

    def test_scent_is_direction_specific(self):
        """scent 與方向綁定，不同方向不應誤擋。"""
        scents: set[tuple[int, int, str]] = {(5, 3, "N")}
        x, y, d, lost = simulate_robot(5, 3, 5, 3, "E", "F", scents)
        self.assertEqual((x, y, d, lost), (5, 3, "E", True))
        self.assertIn((5, 3, "E"), scents)

    def test_sample_robot_1(self):
        """題目經典測資第 1 台：1 1 E / RFRFRFRF -> 1 1 E。"""
        scents: set[tuple[int, int, str]] = set()
        x, y, d, lost = simulate_robot(5, 3, 1, 1, "E", "RFRFRFRF", scents)
        self.assertEqual(format_robot_result(x, y, d, lost), "1 1 E")

    def test_sample_robot_2(self):
        """題目經典測資第 2 台：3 2 N / FRRFLLFFRRFLL -> 3 3 N LOST。"""
        scents: set[tuple[int, int, str]] = set()
        x, y, d, lost = simulate_robot(5, 3, 3, 2, "N", "FRRFLLFFRRFLL", scents)
        self.assertEqual(format_robot_result(x, y, d, lost), "3 3 N LOST")
        self.assertIn((3, 3, "N"), scents)

    def test_sample_robot_3_with_existing_scent(self):
        """題目經典測資第 3 台會受前台留下的 scent 保護。"""
        scents: set[tuple[int, int, str]] = {(3, 3, "N")}
        x, y, d, lost = simulate_robot(5, 3, 0, 3, "W", "LLFFFLFLFL", scents)
        self.assertEqual(format_robot_result(x, y, d, lost), "2 3 S")

    def test_multiple_robots_share_scents(self):
        """多機器人序列執行時，scent 應可共用。"""
        scents: set[tuple[int, int, str]] = set()

        # 第一台：先掉落，留下 (1,2,N)
        r1 = simulate_robot(2, 2, 1, 2, "N", "F", scents)
        self.assertEqual(r1, (1, 2, "N", True))
        self.assertIn((1, 2, "N"), scents)

        # 第二台：同點同向前進被忽略，不掉落
        r2 = simulate_robot(2, 2, 1, 2, "N", "F", scents)
        self.assertEqual(r2, (1, 2, "N", False))

    def test_output_format(self):
        """輸出格式：一般與 LOST 兩種。"""
        self.assertEqual(format_robot_result(1, 1, "E", False), "1 1 E")
        self.assertEqual(format_robot_result(3, 3, "N", True), "3 3 N LOST")


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並把結果寫入 test_118.log。"""
    log_path = Path(__file__).resolve().parent / "test_118.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestUVA118)
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
