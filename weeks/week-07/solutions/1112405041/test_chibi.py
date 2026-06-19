import unittest
from chibi_battle import ChibiBattle

class TestDataLoading(unittest.TestCase):
    """Stage 1: 資料讀取測試"""

    def test_load_generals_from_file(self):
        game = ChibiBattle()
        game.load_generals('generals.txt')
        self.assertEqual(len(game.generals), 9)
        self.assertIn('劉備', game.generals)
        self.assertIn('曹操', game.generals)

    def test_parse_general_attributes(self):
        game = ChibiBattle()
        game.load_generals('generals.txt')
        general = game.generals['關羽']
        self.assertEqual(general.name, '關羽')
        self.assertEqual(general.atk, 28)
        self.assertEqual(general.def_, 14)
        self.assertEqual(general.spd, 85)
        self.assertEqual(general.faction, '蜀')

    def test_faction_distribution(self):
        game = ChibiBattle()
        game.load_generals('generals.txt')
        from collections import Counter
        factions = Counter(g.faction for g in game.generals.values())
        self.assertEqual(factions['蜀'], 3)
        self.assertEqual(factions['吳'], 3)
        self.assertEqual(factions['魏'], 3)

    def test_eof_parsing(self):
        game = ChibiBattle()
        game.load_generals('generals.txt')
        self.assertEqual(len(game.generals), 9)


class TestBattleLogic(unittest.TestCase):
    """Stage 2: 戰鬥模擬與統計測試"""

    def setUp(self):
        self.game = ChibiBattle()
        self.game.load_generals('generals.txt')

    def test_battle_order_by_speed(self):
        order = self.game.get_battle_order()
        self.assertEqual(order[0].spd, 85)
        self.assertEqual(order[-1].spd, 60)

    def test_calculate_damage(self):
        damage = self.game.calculate_damage('關羽', '夏侯惇')
        self.assertEqual(damage, 28 - 14)

    def test_damage_counter_accumulation(self):
        self.game.calculate_damage('關羽', '夏侯惇')
        self.game.calculate_damage('關羽', '曹操')
        self.assertEqual(self.game.stats['damage']['關羽'], 26)

    def test_simulate_one_wave(self):
        self.game.simulate_wave(1)
        total_damage = sum(self.game.stats['damage'].values())
        self.assertGreater(total_damage, 0)

    def test_simulate_three_waves(self):
        self.game.simulate_battle()
        shu_wu_damage = sum(
            dmg for name, dmg in self.game.stats['damage'].items()
            if self.game.generals[name].faction in ['蜀', '吳']
        )
        wei_damage = sum(
            dmg for name, dmg in self.game.stats['damage'].items()
            if self.game.generals[name].faction == '魏'
        )
        self.assertGreater(shu_wu_damage, wei_damage)

    def test_troop_loss_tracking(self):
        self.game.simulate_battle()
        self.assertGreater(self.game.stats['losses']['夏侯惇'], 0)

    def test_damage_ranking_most_common(self):
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        damages = [dmg for _, dmg in ranking]
        self.assertEqual(damages, sorted(damages, reverse=True))

    def test_faction_damage_stats(self):
        self.game.simulate_battle()
        faction_stats = self.game.get_faction_stats()
        self.assertGreater(faction_stats['蜀'], 0)
        self.assertGreater(faction_stats['吳'], 0)
        self.assertGreater(faction_stats['魏'], 0)

    def test_defeated_generals(self):
        self.game.simulate_battle()
        defeated = self.game.get_defeated_generals()
        self.assertGreater(len(defeated), 0)


class TestRefactoring(unittest.TestCase):
    """Stage 3: 重構測試（確保視覺化不影響邏輯）"""

    def setUp(self):
        self.game = ChibiBattle()
        self.game.load_generals('generals.txt')

    def test_stats_unchanged_after_refactor(self):
        self.game.simulate_battle()
        damage_before = dict(self.game.stats['damage'])
        losses_before = dict(self.game.stats['losses'])
        self.assertEqual(dict(self.game.stats['damage']), damage_before)
        self.assertEqual(dict(self.game.stats['losses']), losses_before)

    def test_all_stage1_tests_still_pass(self):
        self.game.load_generals('generals.txt')
        self.assertEqual(len(self.game.generals), 9)

    def test_all_stage2_tests_still_pass(self):
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        self.assertEqual(len(ranking), 5)


class TestSecurity(unittest.TestCase):
    """安全掃毒測試"""

    def setUp(self):
        self.game = ChibiBattle()
        self.game.load_generals('generals.txt')

    def test_empty_filename_raises(self):
        with self.assertRaises(ValueError):
            self.game.load_generals('')

    def test_none_filename_raises(self):
        with self.assertRaises(ValueError):
            self.game.load_generals(None)

    def test_invalid_attacker_raises(self):
        with self.assertRaises(ValueError):
            self.game.calculate_damage('無此人', '曹操')

    def test_invalid_defender_raises(self):
        with self.assertRaises(ValueError):
            self.game.calculate_damage('關羽', '無此人')

    def test_wave_num_zero_raises(self):
        with self.assertRaises(ValueError):
            self.game.simulate_wave(0)

    def test_wave_num_negative_raises(self):
        with self.assertRaises(ValueError):
            self.game.simulate_wave(-1)

    def test_wave_num_float_raises(self):
        with self.assertRaises(ValueError):
            self.game.simulate_wave(1.5)

    def test_bad_format_line_raises(self):
        """少一欄的資料行會拋 ValueError"""
        game2 = ChibiBattle()
        with self.assertRaises(ValueError):
            game2.load_generals('battles.txt')

if __name__ == '__main__':
    unittest.main()
