"""
UVA 118 - Mutant Flatworld Explorers easy 版單元測試

從 solution_118-easy.py 動態載入 lft / rgt / sim / fmt 進行測試。
（因檔名含 '-'，需使用 importlib 動態載入）
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


# ===========================================================
# 動態載入 solution_118-easy.py
# ===========================================================

def _load_easy_module():
    """載入與本測試檔同目錄的 solution_118-easy.py。"""
    module_path = Path(__file__).resolve().parent / "solution_118-easy.py"
    spec = importlib.util.spec_from_file_location("solution_118_easy", module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_easy = _load_easy_module()
lft = _easy.lft
rgt = _easy.rgt
sim = _easy.sim
fmt = _easy.fmt


# ===========================================================
# 測試案例
# ===========================================================

class TestUVA118Easy(unittest.TestCase):
    """UVA 118 easy 版規則測試。"""

    def test_turn_left_right_cycle(self):
        """旋轉規則應符合 N-E-S-W 循環。"""
        self.assertEqual(lft("N"), "W")
        self.assertEqual(rgt("N"), "E")
        d = "N"
        for _ in range(4):
            d = rgt(d)
        self.assertEqual(d, "N")

    def test_simple_move_inside(self):
        """在邊界內前進，不應 LOST。"""
        scents: set[tuple[int, int, str]] = set()
        x, y, d, lost = sim(5, 3, 1, 1, "E", "F", scents)
        self.assertEqual((x, y, d, lost), (2, 1, "E", False))

    def test_lost_at_boundary(self):
        """向外前進應 LOST，並停在掉落前位置。"""
        scents: set[tuple[int, int, str]] = set()
        x, y, d, lost = sim(5, 3, 5, 3, "N", "F", scents)
        self.assertEqual((x, y, d, lost), (5, 3, "N", True))
        self.assertIn((5, 3, "N"), scents)

    def test_scent_blocks_same_fall(self):
        """同一格同方向掉落後，後續機器人應忽略該次 F。"""
        scents: set[tuple[int, int, str]] = {(5, 3, "N")}
        x, y, d, lost = sim(5, 3, 5, 3, "N", "F", scents)
        self.assertEqual((x, y, d, lost), (5, 3, "N", False))

    def test_scent_is_direction_specific(self):
        """scent 與方向綁定，不同方向不應被同一標記擋住。"""
        scents: set[tuple[int, int, str]] = {(5, 3, "N")}
        x, y, d, lost = sim(5, 3, 5, 3, "E", "F", scents)
        self.assertEqual((x, y, d, lost), (5, 3, "E", True))
        self.assertIn((5, 3, "E"), scents)

    def test_sample_robot_1(self):
        """經典測資第 1 台：1 1 E / RFRFRFRF -> 1 1 E。"""
        scents: set[tuple[int, int, str]] = set()
        x, y, d, lost = sim(5, 3, 1, 1, "E", "RFRFRFRF", scents)
        self.assertEqual(fmt(x, y, d, lost), "1 1 E")

    def test_sample_robot_2(self):
        """經典測資第 2 台：3 2 N / FRRFLLFFRRFLL -> 3 3 N LOST。"""
        scents: set[tuple[int, int, str]] = set()
        x, y, d, lost = sim(5, 3, 3, 2, "N", "FRRFLLFFRRFLL", scents)
        self.assertEqual(fmt(x, y, d, lost), "3 3 N LOST")
        self.assertIn((3, 3, "N"), scents)

    def test_sample_robot_3_with_existing_scent(self):
        """經典測資第 3 台受前一台留下 scent 保護。"""
        scents: set[tuple[int, int, str]] = {(3, 3, "N")}
        x, y, d, lost = sim(5, 3, 0, 3, "W", "LLFFFLFLFL", scents)
        self.assertEqual(fmt(x, y, d, lost), "2 3 S")

    def test_multiple_robots_share_scents(self):
        """多機器人依序執行時 scent 要能共用。"""
        scents: set[tuple[int, int, str]] = set()

        r1 = sim(2, 2, 1, 2, "N", "F", scents)
        self.assertEqual(r1, (1, 2, "N", True))
        self.assertIn((1, 2, "N"), scents)

        r2 = sim(2, 2, 1, 2, "N", "F", scents)
        self.assertEqual(r2, (1, 2, "N", False))

    def test_output_format(self):
        """輸出格式：一般與 LOST 兩種。"""
        self.assertEqual(fmt(1, 1, "E", False), "1 1 E")
        self.assertEqual(fmt(3, 3, "N", True), "3 3 N LOST")


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並把結果寫入 test_118-easy.log。"""
    log_path = Path(__file__).resolve().parent / "test_118-easy.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestUVA118Easy)
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
