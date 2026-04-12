from collections import Counter
import importlib.util
from pathlib import Path
import sys
import unittest

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))


def _load_engine_symbols():
    engine_path = CURRENT_DIR / "核心戰鬥引擎.py"
    spec = importlib.util.spec_from_file_location("core_battle_engine", engine_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"無法載入核心戰鬥引擎模組: {engine_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.ChibiBattle, module.General


ChibiBattle, General = _load_engine_symbols()


class TestChibiBattle(unittest.TestCase):
    def setUp(self) -> None:
        self.base_dir = Path(__file__).resolve().parent.parent
        self.game = ChibiBattle()
        self.game.load_generals(self.base_dir / "generals.txt")

    def test_load_generals_from_file(self) -> None:
        self.assertEqual(len(self.game.generals), 9)
        self.assertIn("劉備", self.game.generals)
        self.assertIn("曹操", self.game.generals)

    def test_parse_general_attributes(self) -> None:
        general = self.game.generals["關羽"]
        self.assertIsInstance(general, General)
        self.assertEqual(general.atk, 28)
        self.assertEqual(general.def_, 14)
        self.assertEqual(general.spd, 85)
        self.assertEqual(general.faction, "蜀")

    def test_faction_distribution(self) -> None:
        factions = Counter(g.faction for g in self.game.generals.values())
        self.assertEqual(factions["蜀"], 3)
        self.assertEqual(factions["吳"], 3)
        self.assertEqual(factions["魏"], 3)

    def test_eof_parsing(self) -> None:
        self.assertEqual(len(self.game.generals), 9)

    def test_battle_order_by_speed(self) -> None:
        order = self.game.get_battle_order()
        self.assertEqual(order[0].spd, 85)
        self.assertEqual(order[-1].spd, 60)

    def test_calculate_damage(self) -> None:
        damage = self.game.calculate_damage("關羽", "夏侯惇")
        attacker = self.game.generals["關羽"]
        defender = self.game.generals["夏侯惇"]
        expected = max(1, attacker.atk - defender.def_)
        if attacker.is_leader:
            expected += 2
        self.assertEqual(damage, expected)

    def test_damage_counter_accumulation(self) -> None:
        dmg_1 = self.game.calculate_damage("關羽", "夏侯惇")
        dmg_2 = self.game.calculate_damage("關羽", "曹操")
        self.assertEqual(self.game.stats["damage"]["關羽"], dmg_1 + dmg_2)

    def test_simulate_one_wave(self) -> None:
        self.game.simulate_wave(1)
        total_damage = sum(self.game.stats["damage"].values())
        self.assertGreater(total_damage, 0)

    def test_simulate_three_waves(self) -> None:
        self.game.simulate_battle()
        faction_stats = self.game.get_faction_stats()
        allied_damage = faction_stats.get("蜀", 0) + faction_stats.get("吳", 0)
        wei_damage = faction_stats.get("魏", 0)
        self.assertGreater(allied_damage, 0)
        self.assertGreater(wei_damage, 0)

    def test_troop_loss_tracking(self) -> None:
        self.game.simulate_battle()
        self.assertGreater(sum(self.game.stats["losses"].values()), 0)

    def test_damage_ranking_most_common(self) -> None:
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking(5)
        damages = [dmg for _, dmg in ranking]
        self.assertEqual(damages, sorted(damages, reverse=True))

    def test_faction_damage_stats(self) -> None:
        self.game.simulate_battle()
        faction_stats = self.game.get_faction_stats()
        self.assertGreater(faction_stats.get("蜀", 0), 0)
        self.assertGreater(faction_stats.get("吳", 0), 0)
        self.assertGreater(faction_stats.get("魏", 0), 0)

    def test_defeated_generals_type(self) -> None:
        self.game.simulate_battle(waves=6)
        defeated = self.game.get_defeated_generals()
        self.assertIsInstance(defeated, list)


if __name__ == "__main__":
    unittest.main()
