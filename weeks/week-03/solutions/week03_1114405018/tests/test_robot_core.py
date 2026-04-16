"""Week 03 Robot Lost - 核心邏輯單元測試

本測試採用 TDD 的 Red 階段思維，先把規格固定下來，
再驅動後續的 robot_core.py 實作。

預期 robot_core.py 至少提供以下函式：
- turn_left(direction: str) -> str
- turn_right(direction: str) -> str
- step_forward(x: int, y: int, direction: str) -> tuple[int, int]
- simulate(max_x, max_y, start_x, start_y, start_dir, instructions, scents=None)
    -> tuple[int, int, str, bool, set[tuple[int, int, str]]]
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


class RobotCoreLoaderMixin:
    """負責載入受測模組，避免硬編碼 import 路徑造成測試不可攜。"""

    @classmethod
    def setUpClass(cls) -> None:
        """在測試開始前載入 robot_core.py，若缺檔案就直接報錯。"""
        cls.tests_dir = Path(__file__).resolve().parent
        cls.base_dir = cls.tests_dir.parent
        cls.core_path = cls.base_dir / "robot_core.py"

        if not cls.core_path.exists():
            raise FileNotFoundError(
                "找不到 robot_core.py，請先在 week03_1114405018 下建立該檔案。"
            )

        spec = importlib.util.spec_from_file_location("robot_core", cls.core_path)
        if spec is None or spec.loader is None:
            raise RuntimeError("無法載入 robot_core.py，請檢查檔案內容。")

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        cls.core = module


class TestRobotCoreDirection(RobotCoreLoaderMixin, unittest.TestCase):
    """測試旋轉與位移等最基礎、最容易擴散 bug 的核心功能。"""

    def test_turn_left_from_north(self) -> None:
        """必測清單 #1：N + L = W。"""
        self.assertEqual(self.core.turn_left("N"), "W")

    def test_turn_right_from_north(self) -> None:
        """必測清單 #2：N + R = E。"""
        self.assertEqual(self.core.turn_right("N"), "E")

    def test_turn_right_four_times_back_to_origin(self) -> None:
        """必測清單 #3：連續 4 次右轉應回到原方向。"""
        direction = "N"
        for _ in range(4):
            direction = self.core.turn_right(direction)
        self.assertEqual(direction, "N")

    def test_step_forward_on_north(self) -> None:
        """位移表驗證：朝北前進只增加 y。"""
        self.assertEqual(self.core.step_forward(2, 3, "N"), (2, 4))

    def test_step_forward_on_west(self) -> None:
        """位移表驗證：朝西前進只減少 x。"""
        self.assertEqual(self.core.step_forward(2, 3, "W"), (1, 3))


class TestRobotCoreSimulation(RobotCoreLoaderMixin, unittest.TestCase):
    """測試 simulate 的狀態機規則：越界、LOST、非法指令處理。"""

    def test_inside_boundary_move_not_lost(self) -> None:
        """必測清單 #5：邊界內移動不應 LOST。"""
        x, y, d, lost, scents = self.core.simulate(
            max_x=5,
            max_y=3,
            start_x=1,
            start_y=1,
            start_dir="N",
            instructions="FFRFF",
            scents=set(),
        )
        self.assertEqual((x, y, d, lost), (3, 3, "E", False))
        self.assertEqual(scents, set())

    def test_out_of_boundary_causes_lost(self) -> None:
        """必測清單 #4：在邊界往外前進會 LOST。"""
        x, y, d, lost, scents = self.core.simulate(
            max_x=5,
            max_y=3,
            start_x=0,
            start_y=3,
            start_dir="N",
            instructions="F",
            scents=set(),
        )
        self.assertEqual((x, y, d, lost), (0, 3, "N", True))
        self.assertIn((0, 3, "N"), scents)

    def test_lost_robot_stops_following_commands(self) -> None:
        """必測清單 #9：一旦 LOST，後續指令必須停止執行。"""
        x, y, d, lost, _ = self.core.simulate(
            max_x=2,
            max_y=2,
            start_x=0,
            start_y=2,
            start_dir="N",
            instructions="FRFRF",
            scents=set(),
        )
        self.assertEqual((x, y, d, lost), (0, 2, "N", True))

    def test_invalid_instruction_should_raise_value_error(self) -> None:
        """必測清單 #10：非法指令需有明確策略，這裡要求丟出 ValueError。"""
        with self.assertRaises(ValueError):
            self.core.simulate(
                max_x=5,
                max_y=5,
                start_x=1,
                start_y=1,
                start_dir="E",
                instructions="FXF",
                scents=set(),
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
