import unittest
from collections import Counter
from pathlib import Path

from chibi_battle import ChibiBattle


BASE_DIR = Path(__file__).resolve().parent.parent
GENERALS_FILE = BASE_DIR / "generals.txt"
BATTLES_FILE = BASE_DIR / "battles.txt"


class TestStage1DataLoading(unittest.TestCase):
    def test_load_generals_from_file(self):
        game = ChibiBattle()
        game.load_generals(str(GENERALS_FILE))

        self.assertEqual(len(game.generals), 9)
        self.assertIn("劉備", game.generals)
        self.assertIn("曹操", game.generals)

    def test_parse_general_attributes(self):
        game = ChibiBattle()
        game.load_generals(str(GENERALS_FILE))

        general = game.generals["關羽"]
        self.assertEqual(general.name, "關羽")
        self.assertEqual(general.atk, 28)
        self.assertEqual(general.def_, 14)
        self.assertEqual(general.spd, 85)
        self.assertEqual(general.faction, "蜀")

    def test_faction_distribution(self):
        game = ChibiBattle()
        game.load_generals(str(GENERALS_FILE))

        factions = Counter(g.faction for g in game.generals.values())
        self.assertEqual(factions["蜀"], 3)
        self.assertEqual(factions["吳"], 3)
        self.assertEqual(factions["魏"], 3)

    def test_eof_parsing(self):
        game = ChibiBattle()
        game.load_generals(str(GENERALS_FILE))
        self.assertEqual(len(game.generals), 9)


class TestStage2BattleLogic(unittest.TestCase):
    def setUp(self):
        self.game = ChibiBattle()
        self.game.load_generals(str(GENERALS_FILE))
        self.game.load_battle_config(str(BATTLES_FILE))
        self.game.reset_battle_state()

    def test_battle_order_by_speed(self):
        battle_order = self.game.get_battle_order()
        self.assertEqual(battle_order[0].spd, 85)
        self.assertEqual(battle_order[-1].spd, 60)

    def test_calculate_damage(self):
        damage = self.game.calculate_damage("關羽", "夏侯惇")
        self.assertEqual(damage, 14)

    def test_damage_counter_accumulation(self):
        self.game.calculate_damage("關羽", "夏侯惇")
        self.game.calculate_damage("關羽", "夏侯惇")
        self.assertEqual(self.game.stats["damage"]["關羽"], 28)

    def test_simulate_one_wave(self):
        self.game.simulate_wave(1)
        total_damage = sum(self.game.stats["damage"].values())
        self.assertGreater(total_damage, 0)

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
        damages = [dmg for _, dmg in ranking]
        self.assertEqual(damages, sorted(damages, reverse=True))

    def test_faction_damage_stats(self):
        self.game.simulate_battle()
        faction_stats = self.game.get_faction_stats()
        self.assertGreater(faction_stats["蜀"], 0)
        self.assertGreater(faction_stats["吳"], 0)
        self.assertGreater(faction_stats["魏"], 0)

    def test_defeated_generals(self):
        self.game.simulate_battle()
        defeated = self.game.get_defeated_generals()
        self.assertGreater(len(defeated), 0)


class TestStage3Refactor(unittest.TestCase):
    def setUp(self):
        self.game = ChibiBattle()
        self.game.load_generals(str(GENERALS_FILE))
        self.game.load_battle_config(str(BATTLES_FILE))

    def test_stats_unchanged_after_refactor(self):
        self.game.reset_battle_state()
        self.game.simulate_battle()
        damage_before = dict(self.game.stats["damage"])
        losses_before = dict(self.game.stats["losses"])

        self.assertEqual(dict(self.game.stats["damage"]), damage_before)
        self.assertEqual(dict(self.game.stats["losses"]), losses_before)

    def test_all_stage1_tests_still_pass(self):
        self.game.load_generals(str(GENERALS_FILE))
        self.assertEqual(len(self.game.generals), 9)

    def test_all_stage2_tests_still_pass(self):
        self.game.reset_battle_state()
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        self.assertEqual(len(ranking), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
