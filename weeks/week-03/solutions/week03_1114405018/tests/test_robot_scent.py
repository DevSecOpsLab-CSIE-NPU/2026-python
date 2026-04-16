"""Week 03 Robot Lost - scent 規則單元測試

本檔聚焦 UVA 118 最關鍵的 scent 機制：
- 第一台機器人越界會留下 scent
- 第二台同位置同方向遇到危險前進要忽略
- 同位置不同方向不能共用 scent
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


class RobotCoreLoaderMixin:
    """集中管理模組載入，讓兩份測試可重複使用。"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.tests_dir = Path(__file__).resolve().parent
        cls.base_dir = cls.tests_dir.parent
        cls.core_path = cls.base_dir / "robot_core.py"

        if not cls.core_path.exists():
            raise FileNotFoundError(
                "找不到 robot_core.py，請先建立核心邏輯檔再執行測試。"
            )

        spec = importlib.util.spec_from_file_location("robot_core", cls.core_path)
        if spec is None or spec.loader is None:
            raise RuntimeError("無法載入 robot_core.py。")

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        cls.core = module


class TestRobotScentRules(RobotCoreLoaderMixin, unittest.TestCase):
    """針對 scent 生效與不生效邊界設計測試。"""

    def test_first_robot_lost_leaves_scent(self) -> None:
        """必測清單 #6：第一台越界後要留下 scent。"""
        scents: set[tuple[int, int, str]] = set()
        x, y, d, lost, scents = self.core.simulate(
            max_x=5,
            max_y=3,
            start_x=3,
            start_y=3,
            start_dir="N",
            instructions="F",
            scents=scents,
        )
        self.assertTrue(lost)
        self.assertEqual((x, y, d), (3, 3, "N"))
        self.assertIn((3, 3, "N"), scents)

    def test_second_robot_ignores_dangerous_forward(self) -> None:
        """必測清單 #7：同 (x,y,dir) 的危險 F 要被忽略，且不能 LOST。"""
        scents: set[tuple[int, int, str]] = {(3, 3, "N")}
        x, y, d, lost, scents_after = self.core.simulate(
            max_x=5,
            max_y=3,
            start_x=3,
            start_y=3,
            start_dir="N",
            instructions="F",
            scents=scents,
        )
        self.assertEqual((x, y, d, lost), (3, 3, "N", False))
        self.assertEqual(scents_after, scents)

    def test_same_cell_but_different_direction_not_shared(self) -> None:
        """必測清單 #8：同格但方向不同，scent 不可共用。"""
        scents: set[tuple[int, int, str]] = {(3, 3, "N")}
        x, y, d, lost, scents_after = self.core.simulate(
            max_x=3,
            max_y=3,
            start_x=3,
            start_y=3,
            start_dir="E",
            instructions="F",
            scents=scents,
        )
        self.assertTrue(lost)
        self.assertEqual((x, y, d), (3, 3, "E"))
        self.assertIn((3, 3, "E"), scents_after)

    def test_ignore_then_continue_next_instruction(self) -> None:
        """當危險 F 被 scent 忽略時，後續指令仍應繼續執行。"""
        scents: set[tuple[int, int, str]] = {(3, 3, "N")}
        x, y, d, lost, _ = self.core.simulate(
            max_x=5,
            max_y=3,
            start_x=3,
            start_y=3,
            start_dir="N",
            instructions="FRF",
            scents=scents,
        )
        # 第一步 F 被忽略，之後 R 轉向 E，再 F 到 (4,3)
        self.assertEqual((x, y, d, lost), (4, 3, "E", False))

    def test_scent_set_is_shared_between_robots(self) -> None:
        """同一個 scent 集合在多台機器人間共享，才能反映歷史危險點。"""
        scents: set[tuple[int, int, str]] = set()

        _, _, _, lost_1, scents = self.core.simulate(
            max_x=2,
            max_y=2,
            start_x=2,
            start_y=2,
            start_dir="N",
            instructions="F",
            scents=scents,
        )
        self.assertTrue(lost_1)
        self.assertIn((2, 2, "N"), scents)

        x2, y2, d2, lost_2, _ = self.core.simulate(
            max_x=2,
            max_y=2,
            start_x=2,
            start_y=2,
            start_dir="N",
            instructions="F",
            scents=scents,
        )
        self.assertEqual((x2, y2, d2, lost_2), (2, 2, "N", False))

    def test_empty_instruction_should_keep_state(self) -> None:
        """空指令是合法情況，狀態應維持不變且不 LOST。"""
        x, y, d, lost, scents = self.core.simulate(
            max_x=5,
            max_y=3,
            start_x=1,
            start_y=1,
            start_dir="W",
            instructions="",
            scents=set(),
        )
        self.assertEqual((x, y, d, lost), (1, 1, "W", False))
        self.assertEqual(scents, set())


if __name__ == "__main__":
    unittest.main(verbosity=2)
