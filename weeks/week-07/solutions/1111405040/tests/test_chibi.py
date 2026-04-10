"""
赤壁戰役引擎測試。
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys
import tempfile
import unittest

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from chibi_battle import ChibiBattle, General


class BaseChibiBattleTest(unittest.TestCase):
    """提供共用測試資料與初始化。"""

    def setUp(self) -> None:
        self.solution_dir = ROOT_DIR
        self.generals_file = self.solution_dir / "generals.txt"
        self.battles_file = self.solution_dir / "battles.txt"
        self.game = ChibiBattle()
        self.game.load_generals(self.generals_file)
        self.game.load_battle_config(self.battles_file)


class TestStage1DataLoading(BaseChibiBattleTest):
    """Stage 1: 資料讀取測試。"""

    def test_load_generals_from_file(self) -> None:
        self.assertEqual(len(self.game.generals), 9)
        self.assertIn("劉備", self.game.generals)
        self.assertIn("曹操", self.game.generals)

    def test_parse_general_attributes(self) -> None:
        general = self.game.generals["關羽"]
        self.assertIsInstance(general, General)
        self.assertEqual(general.name, "關羽")
        self.assertEqual(general.atk, 28)
        self.assertEqual(general.def_, 14)
        self.assertEqual(general.spd, 85)
        self.assertEqual(general.faction, "蜀")

    def test_faction_distribution(self) -> None:
        factions = Counter(general.faction for general in self.game.generals.values())
        self.assertEqual(factions["蜀"], 3)
        self.assertEqual(factions["吳"], 3)
        self.assertEqual(factions["魏"], 3)

    def test_eof_parsing_stops_at_marker(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "generals_extra.txt"
            file_path.write_text(
                "\n".join(
                    [
                        "蜀 劉備 100 18 16 75 False",
                        "蜀 關羽 100 28 14 85 False",
                        "EOF",
                        "魏 曹操 120 28 16 80 False",
                    ]
                ),
                encoding="utf-8",
            )

            game = ChibiBattle()
            game.load_generals(file_path)
            self.assertEqual(len(game.generals), 2)
            self.assertNotIn("曹操", game.generals)

    def test_battle_config_is_loaded_correctly(self) -> None:
        config = self.game.battle_config
        self.assertEqual(config.name, "赤壁")
        self.assertEqual(config.waves, 3)
        self.assertEqual(config.allies, ("蜀", "吳"))
        self.assertEqual(config.enemies, ("魏",))


class TestStage2BattleLogic(BaseChibiBattleTest):
    """Stage 2: 戰鬥模擬與統計。"""

    def test_battle_order_by_speed(self) -> None:
        order = self.game.get_battle_order()
        speeds = [general.spd for general in order]
        self.assertEqual(speeds, sorted(speeds, reverse=True))
        self.assertEqual(order[0].spd, 85)
        self.assertEqual(order[-1].spd, 60)

    def test_calculate_damage(self) -> None:
        damage = self.game.calculate_damage("關羽", "夏侯惇")
        self.assertEqual(damage, 14)

    def test_damage_counter_accumulation(self) -> None:
        self.game.calculate_damage("關羽", "夏侯惇")
        self.game.calculate_damage("關羽", "曹操")
        self.assertEqual(self.game.stats["damage"]["關羽"], 26)

    def test_simulate_one_wave(self) -> None:
        self.game.simulate_wave(1)
        total_damage = sum(self.game.stats["damage"].values())
        self.assertGreater(total_damage, 0)
        self.assertGreater(self.game.stats["losses"]["郭嘉"], 0)

    def test_simulate_three_waves_allied_damage_is_higher(self) -> None:
        self.game.simulate_battle()
        faction_stats = self.game.get_faction_stats()
        allied_damage = faction_stats.get("蜀", 0) + faction_stats.get("吳", 0)
        self.assertGreater(allied_damage, faction_stats.get("魏", 0))

    def test_troop_loss_tracking(self) -> None:
        self.game.simulate_battle()
        self.assertGreater(self.game.stats["losses"]["郭嘉"], 0)
        self.assertGreater(self.game.stats["losses"]["諸葛亮"], 0)

    def test_damage_ranking_most_common(self) -> None:
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        damages = [damage for _, damage in ranking]
        self.assertEqual(damages, sorted(damages, reverse=True))
        self.assertEqual(len(ranking), 5)

    def test_faction_damage_stats(self) -> None:
        self.game.simulate_battle()
        faction_stats = self.game.get_faction_stats()
        self.assertGreater(faction_stats["蜀"], 0)
        self.assertGreater(faction_stats["吳"], 0)
        self.assertGreater(faction_stats["魏"], 0)

    def test_defeated_generals(self) -> None:
        self.game.simulate_battle()
        defeated = self.game.get_defeated_generals()
        self.assertGreater(len(defeated), 0)
        self.assertIn("郭嘉", defeated)


class TestStage3Refactor(BaseChibiBattleTest):
    """Stage 3: 報告與重構測試。"""

    def test_stats_unchanged_after_report_generation(self) -> None:
        self.game.simulate_battle()
        damage_before = dict(self.game.stats["damage"])
        losses_before = dict(self.game.stats["losses"])

        _ = self.game.generate_damage_report()

        self.assertEqual(dict(self.game.stats["damage"]), damage_before)
        self.assertEqual(dict(self.game.stats["losses"]), losses_before)

    def test_battle_start_report_contains_factions_and_name(self) -> None:
        report = self.game.generate_battle_start()
        self.assertIn("赤壁戰役", report)
        self.assertIn("【蜀軍】", report)
        self.assertIn("【吳軍】", report)
        self.assertIn("【魏軍】", report)

    def test_full_battle_report_contains_rankings(self) -> None:
        report = self.game.run_full_battle(print_output=False)
        self.assertIn("【傷害輸出排名】", report)
        self.assertIn("【勢力傷害統計】", report)
        self.assertIn("【兵力損失統計】", report)


if __name__ == "__main__":
    unittest.main()
