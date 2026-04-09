import sys
import unittest
from collections import Counter
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from chibi_battle import ChibiBattle


class TestStage1DataLoading(unittest.TestCase):
    def setUp(self):
        self.game = ChibiBattle()

    def test_load_generals_from_file(self):
        self.game.load_generals("generals.txt")
        self.assertEqual(len(self.game.generals), 9)
        self.assertIn("劉備", self.game.generals)
        self.assertIn("曹操", self.game.generals)

    def test_parse_general_attributes(self):
        self.game.load_generals("generals.txt")
        general = self.game.generals["關羽"]

        self.assertEqual(general.name, "關羽")
        self.assertEqual(general.atk, 28)
        self.assertEqual(general.def_, 14)
        self.assertEqual(general.spd, 85)
        self.assertEqual(general.faction, "蜀")

    def test_faction_distribution(self):
        self.game.load_generals("generals.txt")
        factions = Counter(g.faction for g in self.game.generals.values())

        self.assertEqual(factions["蜀"], 3)
        self.assertEqual(factions["吳"], 3)
        self.assertEqual(factions["魏"], 3)

    def test_eof_parsing(self):
        self.game.load_generals("generals.txt")
        self.assertEqual(len(self.game.generals), 9)


class TestStage2BattleLogic(unittest.TestCase):
    def setUp(self):
        self.game = ChibiBattle()
        self.game.load_generals("generals.txt")

    def test_battle_order_by_speed(self):
        order = self.game.get_battle_order()
        self.assertEqual(order[0].spd, 85)
        self.assertEqual(order[-1].spd, 60)

    def test_calculate_damage(self):
        damage = self.game.calculate_damage("關羽", "夏侯惇")
        self.assertEqual(damage, 14)

    def test_damage_counter_accumulation(self):
        self.game.calculate_damage("關羽", "夏侯惇")
        self.game.calculate_damage("關羽", "曹操")
        self.assertEqual(self.game.stats["damage"]["關羽"], 26)

    def test_simulate_one_wave(self):
        self.game.simulate_wave(1)
        self.assertGreater(sum(self.game.stats["damage"].values()), 0)

    def test_simulate_three_waves(self):
        self.game.simulate_battle()
        shu_wu_damage = sum(
            dmg
            for name, dmg in self.game.stats["damage"].items()
            if self.game.generals[name].faction in ["蜀", "吳"]
        )
        wei_damage = sum(
            dmg
            for name, dmg in self.game.stats["damage"].items()
            if self.game.generals[name].faction == "魏"
        )
        self.assertGreater(shu_wu_damage, wei_damage)

    def test_troop_loss_tracking(self):
        self.game.simulate_battle()
        self.assertGreater(self.game.stats["losses"]["夏侯惇"], 0)

    def test_damage_ranking_most_common(self):
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        values = [item[1] for item in ranking]
        self.assertEqual(values, sorted(values, reverse=True))

    def test_faction_damage_stats(self):
        self.game.simulate_battle()
        stats = self.game.get_faction_stats()
        self.assertGreater(stats.get("蜀", 0), 0)
        self.assertGreater(stats.get("吳", 0), 0)
        self.assertGreater(stats.get("魏", 0), 0)

    def test_defeated_generals(self):
        self.game.simulate_battle()
        defeated = self.game.get_defeated_generals()
        self.assertGreater(len(defeated), 0)


class TestStage3Refactor(unittest.TestCase):
    def setUp(self):
        self.game = ChibiBattle()
        self.game.load_generals("generals.txt")

    def test_stats_unchanged_after_reporting(self):
        self.game.simulate_battle()
        damage_before = dict(self.game.stats["damage"])
        losses_before = dict(self.game.stats["losses"])

        self.game.print_damage_report()

        self.assertEqual(dict(self.game.stats["damage"]), damage_before)
        self.assertEqual(dict(self.game.stats["losses"]), losses_before)

    def test_stage1_and_stage2_apis_still_work(self):
        self.assertEqual(len(self.game.generals), 9)
        self.game.simulate_battle()
        self.assertEqual(len(self.game.get_damage_ranking()), 5)


if __name__ == "__main__":
    unittest.main()
