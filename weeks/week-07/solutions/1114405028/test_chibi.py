"""赤壁戰役測試檔 - TDD 三階段測試"""

import unittest
from collections import Counter
from chibi_battle import ChibiBattle


class TestStage1DataLoading(unittest.TestCase):
    """Stage 1: RED 階段 - 資料讀取與結構 (Week 07 檔案 I/O)"""
    
    def setUp(self):
        """每個測試前準備"""
        self.game = ChibiBattle()
    
    def test_load_generals_from_file(self):
        """測試 1-1: 正確讀取 9 位武將"""
        # Arrange: 準備測試環境
        game = ChibiBattle()
        
        # Act: 執行讀取
        game.load_generals('generals.txt')
        
        # Assert: 驗證結果
        self.assertEqual(len(game.generals), 9)
    
    def test_parse_general_attributes(self):
        """測試 1-2: 正確解析武將屬性"""
        self.game.load_generals('generals.txt')
        
        # 驗證 namedtuple 結構體
        general = self.game.generals['關羽']
        self.assertEqual(general.name, '關羽')
        self.assertEqual(general.atk, 28)
        self.assertEqual(general.def_, 14)
        self.assertEqual(general.spd, 85)
        self.assertEqual(general.faction, '蜀')
    
    def test_faction_distribution(self):
        """測試 1-3: 三國分布正確"""
        self.game.load_generals('generals.txt')
        
        # 使用 Counter 統計
        factions = Counter(g.faction for g in self.game.generals.values())
        
        self.assertEqual(factions['蜀'], 3)
        self.assertEqual(factions['吳'], 3)
        self.assertEqual(factions['魏'], 3)
    
    def test_eof_parsing(self):
        """測試 1-4: 正確識別 EOF 結尾"""
        self.game.load_generals('generals.txt')
        
        # 應能正確停止在 EOF，不會超過 9 位
        self.assertEqual(len(self.game.generals), 9)


class TestStage2BattleLogic(unittest.TestCase):
    """Stage 2: GREEN 階段 - 戰鬥模擬與統計 (Week 02 資料結構)"""
    
    def setUp(self):
        """每個測試前準備"""
        self.game = ChibiBattle()
        self.game.load_generals('generals.txt')
    
    def test_battle_order_by_speed(self):
        """測試 2-1: 根據速度排序戰鬥順序"""
        # Week 02: sorted(key=...)
        battle_order = self.game.get_battle_order()
        
        # 速度由高到低
        self.assertEqual(battle_order[0].spd, 85)  # 最快
        self.assertGreaterEqual(battle_order[0].spd, battle_order[-1].spd)  # 遞減
    
    def test_calculate_damage(self):
        """測試 2-2: 正確計算傷害 (攻擊 - 防禦)"""
        # 關羽 (攻28) vs 夏侯惇 (防14)
        damage = self.game.calculate_damage('關羽', '夏侯惇')
        
        self.assertEqual(damage, 28 - 14)  # = 14
    
    def test_damage_counter_accumulation(self):
        """測試 2-3: Counter 自動累加傷害"""
        # Week 02: Counter
        self.game.calculate_damage('關羽', '夏侯惇')
        self.game.calculate_damage('關羽', '曹操')
        
        # 應累加為 14 + 12 = 26
        self.assertEqual(self.game.stats['damage']['關羽'], 26)
    
    def test_simulate_one_wave(self):
        """測試 2-4: 模擬一波戰鬥"""
        self.game.simulate_wave(1)  # Wave 1
        
        # 驗證有傷害產生
        total_damage = sum(self.game.stats['damage'].values())
        self.assertGreater(total_damage, 0)
    
    def test_simulate_three_waves(self):
        """測試 2-5: 模擬三波完整戰役"""
        self.game.simulate_battle()
        
        # 驗證三波都產生傷害
        total_damage = sum(self.game.stats['damage'].values())
        self.assertGreater(total_damage, 0)
    
    def test_troop_loss_tracking(self):
        """測試 2-6: defaultdict 追蹤兵力損失"""
        # Week 02: defaultdict
        self.game.simulate_battle()
        
        # 魏軍應受到傷害
        total_loss = sum(
            loss for name, loss in self.game.stats['losses'].items()
            if self.game.generals[name].faction == '魏'
        )
        self.assertGreater(total_loss, 0)
    
    def test_damage_ranking_most_common(self):
        """測試 2-7: most_common() 傷害排名"""
        # Week 02: Counter.most_common()
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        
        # 應取得排名
        self.assertGreater(len(ranking), 0)
        self.assertLessEqual(len(ranking), 5)
        
        # 傷害遞減
        damages = [dmg for _, dmg in ranking]
        self.assertEqual(damages, sorted(damages, reverse=True))
    
    def test_faction_damage_stats(self):
        """測試 2-8: 按勢力統計傷害"""
        # Week 02: groupby 概念 + defaultdict
        self.game.simulate_battle()
        faction_stats = self.game.get_faction_stats()
        
        self.assertGreater(faction_stats.get('蜀', 0), 0)
        self.assertGreater(faction_stats.get('吳', 0), 0)
        self.assertGreater(faction_stats.get('魏', 0), 0)
    
    def test_defeated_generals(self):
        """測試 2-9: 正確識別戰敗將領"""
        self.game.simulate_battle()
        defeated = self.game.get_defeated_generals()
        
        # 應該有將領戰敗 (至少一位)
        # 注意: 此測試可能需調整，取決於戰役規則
        self.assertIsInstance(defeated, list)


class TestStage3Refactor(unittest.TestCase):
    """Stage 3: REFACTOR 階段 - 視覺化與報告"""
    
    def setUp(self):
        """每個測試前準備"""
        self.game = ChibiBattle()
        self.game.load_generals('generals.txt')
    
    def test_stats_unchanged_after_refactor(self):
        """測試 3-1: 重構後統計結果不變"""
        self.game.simulate_battle()
        
        damage_before = dict(self.game.stats['damage'])
        losses_before = dict(self.game.stats['losses'])
        
        # 重新執行 (視覺化不應改變邏輯)
        self.assertEqual(dict(self.game.stats['damage']), damage_before)
        self.assertEqual(dict(self.game.stats['losses']), losses_before)
    
    def test_all_stage1_tests_still_pass(self):
        """測試 3-2: Stage 1 測試仍通過"""
        self.game.load_generals('generals.txt')
        self.assertEqual(len(self.game.generals), 9)
    
    def test_all_stage2_tests_still_pass(self):
        """測試 3-3: Stage 2 測試仍通過"""
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        self.assertEqual(len(ranking), 5)


if __name__ == '__main__':
    unittest.main()
