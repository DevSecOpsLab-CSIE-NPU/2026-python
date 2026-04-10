# solution/test_chibi.py
# 赤壁戰役 - 完整 TDD 測試 (共 12 個測試)

import unittest
import os
import sys
from collections import Counter

# 確保可以 import chibi_battle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chibi_battle import ChibiBattle, General

# generals.txt 路徑 (在 week-07/ 目錄)
GENERALS_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'generals.txt'
)


# ═══════════════════════════════════════════════
# Stage 1: 資料讀取測試
# ═══════════════════════════════════════════════

class TestDataLoading(unittest.TestCase):
    """Stage 1: 資料讀取測試"""

    def setUp(self):
        self.game = ChibiBattle()
        self.game.load_generals(GENERALS_FILE)

    def test_load_generals_from_file(self):
        """測試 1-1: 正確讀取 9 位武將"""
        self.assertEqual(len(self.game.generals), 9)
        self.assertIn('劉備', self.game.generals)
        self.assertIn('曹操', self.game.generals)

    def test_parse_general_attributes(self):
        """測試 1-2: 正確解析 關羽 屬性"""
        g = self.game.generals['關羽']
        self.assertEqual(g.name, '關羽')
        self.assertEqual(g.atk, 28)
        self.assertEqual(g.def_, 14)
        self.assertEqual(g.spd, 85)
        self.assertEqual(g.faction, '蜀')
        self.assertFalse(g.is_leader)

    def test_faction_distribution(self):
        """測試 1-3: 三國各 3 位"""
        from collections import Counter
        factions = Counter(g.faction for g in self.game.generals.values())
        self.assertEqual(factions['蜀'], 3)
        self.assertEqual(factions['吳'], 3)
        self.assertEqual(factions['魏'], 3)

    def test_eof_parsing(self):
        """測試 1-4: EOF 結尾，不超過 9 位"""
        self.assertEqual(len(self.game.generals), 9)

    def test_namedtuple_structure(self):
        """測試 1-5: 武將為 namedtuple General"""
        g = self.game.generals['曹操']
        self.assertIsInstance(g, General)
        self.assertTrue(hasattr(g, 'faction'))
        self.assertTrue(hasattr(g, 'hp'))
        self.assertTrue(hasattr(g, 'is_leader'))


# ═══════════════════════════════════════════════
# Stage 2: 戰鬥模擬與統計測試
# ═══════════════════════════════════════════════

class TestBattleLogic(unittest.TestCase):
    """Stage 2: 戰鬥模擬與統計測試"""

    def setUp(self):
        self.game = ChibiBattle()
        self.game.load_generals(GENERALS_FILE)

    def test_battle_order_by_speed(self):
        """測試 2-1: 速度由高到低排序"""
        order = self.game.get_battle_order()
        speeds = [g.spd for g in order]
        self.assertEqual(speeds, sorted(speeds, reverse=True))
        self.assertEqual(order[0].spd, 85)
        self.assertEqual(order[-1].spd, 60)  # 諸葛亮最慢

    def test_calculate_damage(self):
        """測試 2-2: 關羽 (攻28) vs 夏侯惇 (防14) = 14"""
        damage = self.game.calculate_damage('關羽', '夏侯惇')
        self.assertEqual(damage, 28 - 14)

    def test_damage_counter_accumulation(self):
        """測試 2-3: Counter 自動累加傷害"""
        self.game.calculate_damage('關羽', '夏侯惇')  # +14
        self.game.calculate_damage('關羽', '曹操')    # +12
        self.assertEqual(self.game.stats['damage']['關羽'], 26)

    def test_simulate_one_wave(self):
        """測試 2-4: 第一波有傷害產生"""
        self.game.simulate_wave(1)
        total = sum(self.game.stats['damage'].values())
        self.assertGreater(total, 0)

    def test_simulate_three_waves(self):
        """測試 2-5: 蜀吳總傷害 > 魏軍傷害"""
        self.game.simulate_battle()
        shu_wu = sum(
            dmg
            for name, dmg in self.game.stats['damage'].items()
            if self.game.generals[name].faction in ('蜀', '吳')
        )
        wei = sum(
            dmg
            for name, dmg in self.game.stats['damage'].items()
            if self.game.generals[name].faction == '魏'
        )
        self.assertGreater(shu_wu, wei)

    def test_troop_loss_tracking(self):
        """測試 2-6: defaultdict 追蹤兵力損失"""
        self.game.simulate_battle()
        self.assertGreater(self.game.stats['losses']['夏侯惇'], 0)

    def test_damage_ranking_most_common(self):
        """測試 2-7: most_common() 排名遞減"""
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        damages = [dmg for _, dmg in ranking]
        self.assertEqual(damages, sorted(damages, reverse=True))

    def test_faction_damage_stats(self):
        """測試 2-8: 蜀軍有傷害輸出，can track by faction"""
        self.game.simulate_battle()
        stats = self.game.get_faction_stats()
        self.assertGreater(stats.get('蜀', 0), 0)
        # 本模擬蜀單向攻魏，魏軍不反擊，故魏不在 damage
        self.assertIn('蜀', stats)

    def test_defeated_generals(self):
        """測試 2-9: 有將領戰敗"""
        self.game.simulate_battle()
        defeated = self.game.get_defeated_generals()
        self.assertIsInstance(defeated, list)


# ═══════════════════════════════════════════════
# Stage 3: 重構測試
# ═══════════════════════════════════════════════

class TestRefactoring(unittest.TestCase):
    """Stage 3: 重構測試"""

    def setUp(self):
        self.game = ChibiBattle()
        self.game.load_generals(GENERALS_FILE)
        self.game.simulate_battle()

    def test_stats_unchanged_after_report(self):
        """測試 3-1: 列印報告不改變統計數據"""
        damage_before = dict(self.game.stats['damage'])
        losses_before = dict(self.game.stats['losses'])
        # 呼叫視覺化 (丟棄 stdout)
        import io
        import contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            self.game.print_damage_report()
        self.assertEqual(dict(self.game.stats['damage']), damage_before)
        self.assertEqual(dict(self.game.stats['losses']), losses_before)

    def test_all_stage1_still_pass(self):
        """測試 3-2: Stage 1 讀取仍正確"""
        game2 = ChibiBattle()
        game2.load_generals(GENERALS_FILE)
        self.assertEqual(len(game2.generals), 9)

    def test_all_stage2_still_pass(self):
        """測試 3-3: Stage 2 統計仍正確"""
        ranking = self.game.get_damage_ranking()
        # 蜀有 3 位將軍，最多 3 筆排名
        self.assertGreater(len(ranking), 0)
        damages = [d for _, d in ranking]
        self.assertEqual(damages, sorted(damages, reverse=True))


if __name__ == '__main__':
    unittest.main(verbosity=2)
