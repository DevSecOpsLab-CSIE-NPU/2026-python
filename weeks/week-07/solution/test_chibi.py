import io
import unittest
from contextlib import redirect_stdout

from chibi_battle import ChibiBattle


class TestChibiBattle(unittest.TestCase):
    def setUp(self):
        self.game = ChibiBattle()
        self.game.load_generals("generals.txt")

    # Stage 1
    def test_load_generals_count(self):
        self.assertEqual(len(self.game.generals), 9)
        self.assertIn("劉備", self.game.generals)
        self.assertIn("曹操", self.game.generals)

    def test_parse_general_attributes(self):
        guan_yu = self.game.generals["關羽"]
        self.assertEqual(guan_yu.name, "關羽")
        self.assertEqual(guan_yu.atk, 28)
        self.assertEqual(guan_yu.def_, 14)
        self.assertEqual(guan_yu.spd, 85)
        self.assertEqual(guan_yu.faction, "蜀")

    def test_faction_distribution(self):
        factions = [g.faction for g in self.game.generals.values()]
        self.assertEqual(factions.count("蜀"), 3)
        self.assertEqual(factions.count("吳"), 3)
        self.assertEqual(factions.count("魏"), 3)

    def test_eof_parsing(self):
        self.assertEqual(len(self.game.generals), 9)

    # Stage 2
    def test_battle_order_by_speed(self):
        battle_order = self.game.get_battle_order()
        self.assertEqual(battle_order[0].spd, 85)
        self.assertEqual(battle_order[-1].spd, 60)

    def test_calculate_damage(self):
        damage = self.game.calculate_damage("關羽", "夏侯惇")
        self.assertEqual(damage, 28 - 14)

    def test_damage_counter_accumulation(self):
        self.game.calculate_damage("關羽", "夏侯惇")
        self.game.calculate_damage("關羽", "曹操")
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

    # Stage 3
    def test_stats_unchanged_after_report(self):
        self.game.simulate_battle()
        damage_before = dict(self.game.stats["damage"])
        losses_before = dict(self.game.stats["losses"])

        output = io.StringIO()
        with redirect_stdout(output):
            self.game.print_damage_report()

        self.assertEqual(dict(self.game.stats["damage"]), damage_before)
        self.assertEqual(dict(self.game.stats["losses"]), losses_before)

    def test_run_full_battle_output(self):
        game = ChibiBattle()
        game.load_generals("generals.txt")

        output = io.StringIO()
        with redirect_stdout(output):
            game.run_full_battle()

        text = output.getvalue()
        self.assertIn("赤壁戰役", text)
        self.assertIn("傷害統計報告", text)


if __name__ == "__main__":
    unittest.main()
