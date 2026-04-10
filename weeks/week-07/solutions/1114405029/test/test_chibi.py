import unittest
import sys
import os
from collections import Counter

# 確保路徑指向父目錄以匯入 chibi_battle.py
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from chibi_battle import ChibiBattle

class TestChibiBattleMaster(unittest.TestCase):
    
    def setUp(self):
        """測試前的環境初始化"""
        self.game = ChibiBattle()
        self.gen_file = os.path.join(parent_dir, 'generals.txt')
        self.bat_file = os.path.join(parent_dir, 'battles.txt')
        
        # 預先載入資料，這是後續所有測試的基礎
        self.game.load_generals(self.gen_file)
        self.game.load_battles(self.bat_file)

    # === Stage 1: 進階資料載入測試 ===
    
    def test_load_generals_count(self):
        """驗證是否成功載入 9 位武將"""
        self.assertEqual(len(self.game.generals), 9)

    def test_load_battle_config(self):
        """驗證 battles.txt 是否正確解析為字典"""
        self.assertIsNotNone(self.game.battle_config)
        self.assertEqual(self.game.battle_config['name'], '赤壁')
        self.assertIn('蜀', self.game.battle_config['attackers'])

    # === Stage 2: 核心戰鬥邏輯與加成測試 ===

    def test_leader_aura_bonus(self):
        """驗證領袖活著時是否有攻擊加成 (1.1倍)"""
        # 假設關羽(28)攻擊夏侯惇(14)，若劉備(領袖)在場
        # 傷害應為: int(28 * 1.1) - 14 = 30 - 14 = 16
        dmg = self.game.calculate_damage('關羽', '夏侯惇')
        self.assertEqual(dmg, 16)

    def test_permadeath_exclusion(self):
        """驗證陣亡武將是否會被移出攻擊順序"""
        # 手動將張遼設定為戰敗
        self.game.stats['losses']['張遼'] = 999 
        order = self.game.get_battle_order()
        names = [g.name for g in order]
        self.assertNotIn('張遼', names)

    def test_calculate_damage_minimum(self):
        """驗證即使防禦極高，傷害保底仍為 1"""
        # 人為修改曹操防禦力
        self.game.generals['曹操'] = self.game.generals['曹操']._replace(def_=999)
        dmg = self.game.calculate_damage('劉備', '曹操')
        self.assertEqual(dmg, 1)

    # === Stage 3: 完整模擬與報表數據測試 ===

    def test_simulate_full_campaign(self):
        """執行完整三波模擬並檢查傷害統計"""
        self.game.simulate_battle()
        total_dmg = sum(self.game.stats['damage'].values())
        self.assertGreater(total_dmg, 0)
        
        # 檢查是否有武將產生敗退紀錄
        defeated = self.game.get_defeated_generals()
        self.assertIsInstance(defeated, list)

    def test_faction_stat_integrity(self):
        """驗證陣營傷害總和是否等於各武將傷害總和"""
        self.game.simulate_battle()
        f_stats = self.game.get_faction_stats()
        sum_f_stats = sum(f_stats.values())
        sum_indiv_stats = sum(self.game.stats['damage'].values())
        self.assertEqual(sum_f_stats, sum_indiv_stats)

if __name__ == '__main__':
    unittest.main()