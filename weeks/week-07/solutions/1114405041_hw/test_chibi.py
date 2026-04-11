from __future__ import annotations

import subprocess
import sys
import unittest
from collections import Counter
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from chibi_battle import ChibiBattle
from chibi_battle_easy import ChibiBattleEasy


class TestStage1DataLoading(unittest.TestCase):
    def setUp(self) -> None:
        self.game = ChibiBattle()
        self.game.setup()

    def test_load_generals_from_file(self) -> None:
        self.assertEqual(len(self.game.generals), 9)
        self.assertIn("劉備", self.game.generals)
        self.assertIn("曹操", self.game.generals)

    def test_parse_general_attributes(self) -> None:
        general = self.game.generals["關羽"]
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

    def test_eof_parsing(self) -> None:
        self.assertEqual(self.game.battle_config.waves, 3)
        self.assertEqual(self.game.battle_config.battlefield, "赤壁")


class TestStage2BattleLogic(unittest.TestCase):
    def setUp(self) -> None:
        self.game = ChibiBattle()
        self.game.setup()

    def test_battle_order_by_speed(self) -> None:
        battle_order = self.game.get_battle_order()
        self.assertEqual(battle_order[0].spd, 85)
        self.assertEqual(battle_order[-1].spd, 60)

    def test_calculate_damage(self) -> None:
        damage = self.game.calculate_damage("關羽", "夏侯惇")
        self.assertEqual(damage, 16)
        self.assertEqual(self.game.current_hp["夏侯惇"], 89)

    def test_damage_counter_accumulation(self) -> None:
        self.game.calculate_damage("關羽", "夏侯惇")
        self.game.calculate_damage("關羽", "曹操")
        self.assertEqual(self.game.stats["damage"]["關羽"], 30)

    def test_simulate_one_wave(self) -> None:
        events = self.game.simulate_wave(1)
        self.assertGreater(len(events), 0)
        self.assertGreater(sum(self.game.stats["damage"].values()), 0)

    def test_simulate_three_waves(self) -> None:
        self.game.simulate_battle()
        faction_stats = self.game.get_faction_stats()
        shu_wu_damage = faction_stats.get("蜀", 0) + faction_stats.get("吳", 0)
        wei_damage = faction_stats.get("魏", 0)
        self.assertGreater(shu_wu_damage, wei_damage)

    def test_troop_loss_tracking(self) -> None:
        self.game.simulate_battle()
        self.assertGreater(self.game.stats["losses"]["夏侯惇"], 0)

    def test_damage_ranking_most_common(self) -> None:
        self.game.simulate_battle()
        damages = [damage for _, damage in self.game.get_damage_ranking()]
        self.assertEqual(damages, sorted(damages, reverse=True))

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


class TestStage3InteractiveAndRefactor(unittest.TestCase):
    def setUp(self) -> None:
        self.game = ChibiBattle()
        self.game.setup()
        self.easy = ChibiBattleEasy()
        self.easy.load_generals()

    def test_stats_unchanged_after_report_generation(self) -> None:
        self.game.simulate_battle()
        damage_before = dict(self.game.stats["damage"])
        losses_before = dict(self.game.stats["losses"])
        _ = self.game.get_damage_report_lines()
        self.assertEqual(dict(self.game.stats["damage"]), damage_before)
        self.assertEqual(dict(self.game.stats["losses"]), losses_before)

    def test_auto_battle_output_contains_report(self) -> None:
        report = self.game.run_full_battle()
        self.assertIn("赤壁戰役 - 傷害統計報告", report)
        self.assertIn("勝方：蜀吳聯軍", report)

    def test_status_command(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(BASE_DIR / "chibi_battle.py"), "--status"],
            cwd=BASE_DIR,
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("【蜀軍】", completed.stdout)
        self.assertIn("劉備", completed.stdout)

    def test_easy_version_can_finish_battle(self) -> None:
        self.easy.simulate_battle()
        self.assertEqual(self.easy.get_winner(), "蜀吳聯軍")
        self.assertGreater(len(self.easy.get_defeated_generals()), 0)

    def test_easy_auto_output(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(BASE_DIR / "chibi_battle_easy.py"), "--auto"],
            cwd=BASE_DIR,
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("赤壁戰役簡單版", completed.stdout)
        self.assertIn("勝方：蜀吳聯軍", completed.stdout)


if __name__ == "__main__":
    unittest.main()