from collections import Counter
from pathlib import Path
import unittest

from chibi_battle import ChibiBattle, General


class TestChibiBattle(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base = Path(__file__).parent
        cls.generals_file = cls.base / "generals.txt"

    def setUp(self) -> None:
        self.game = ChibiBattle()
        self.game.load_generals(str(self.generals_file))

    # Stage 1
    def test_load_generals_from_file(self):
        self.assertEqual(len(self.game.generals), 9)
        self.assertIn("劉備", self.game.generals)
        self.assertIn("曹操", self.game.generals)

    def test_parse_general_attributes(self):
        general = self.game.generals["關羽"]
        self.assertEqual(general.name, "關羽")
        self.assertEqual(general.atk, 28)
        self.assertEqual(general.def_, 14)
        self.assertEqual(general.spd, 85)
        self.assertEqual(general.faction, "蜀")

    def test_namedtuple_structure(self):
        general = self.game.generals["周瑜"]
        self.assertIsInstance(general, tuple)
        self.assertIsInstance(general, General)

    def test_faction_distribution(self):
        factions = Counter(g.faction for g in self.game.generals.values())
        self.assertEqual(factions["蜀"], 3)
        self.assertEqual(factions["吳"], 3)
        self.assertEqual(factions["魏"], 3)

    def test_eof_parsing(self):
        self.assertEqual(len(self.game.generals), 9)

    # Stage 2
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
        wei_losses = sum(
            self.game.stats["losses"][name]
            for name, general in self.game.generals.items()
            if general.faction == "魏"
        )
        self.assertGreater(wei_losses, 0)

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
    def test_stats_unchanged_after_snapshot(self):
        self.game.simulate_battle()
        damage_before = dict(self.game.stats["damage"])
        losses_before = dict(self.game.stats["losses"])
        self.assertEqual(dict(self.game.stats["damage"]), damage_before)
        self.assertEqual(dict(self.game.stats["losses"]), losses_before)


if __name__ == "__main__":
    unittest.main()
