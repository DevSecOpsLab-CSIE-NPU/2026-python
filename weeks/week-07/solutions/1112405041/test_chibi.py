import unittest
import os
from chibi_battle import ChibiBattle

class TestChibiBattle(unittest.TestCase):
    def setUp(self):
        # 確保測試環境有 generals.txt
        # 這是為了解決路徑地雷，手動指定絕對路徑
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.test_file = os.path.join(current_dir, "..", "..", "generals.txt")

        self.game = ChibiBattle()
        self.game.load_generals(self.test_file)

    def test_load_count(self):
        """測試 1: 是否讀取 9 位武將"""
        self.assertEqual(len(self.game.generals), 9)

    def test_specific_general(self):
        """測試 2: 驗證關羽屬性"""
        if '關羽' in self.game.generals:
            guanyu = self.game.generals['關羽']
            self.assertEqual(guanyu.faction, '蜀')
            self.assertEqual(guanyu.atk, 28)
        else:
            self.fail("關羽不在武將名單中")

    def test_battle_order(self):
        """測試 3: 驗證速度排序"""
        order = self.game.get_battle_order()
        if order:
            self.assertGreaterEqual(order[0].spd, order[-1].spd)
        else:
            self.fail("排序結果為空")

    def test_damage_calc(self):
        """測試 4: 傷害計算邏輯"""
        # 曹操(28) vs 劉備(16) => 12 傷害
        if '曹操' in self.game.generals and '劉備' in self.game.generals:
            dmg = self.game.calculate_damage('曹操', '劉備')
            self.assertEqual(dmg, 12)

    def test_counter_stat(self):
        """測試 5: Counter 傷害累加"""
        if '關羽' in self.game.generals and '曹操' in self.game.generals:
            self.game.calculate_damage('關羽', '曹操')
            self.game.calculate_damage('關羽', '曹操')
            # 關羽(28) - 曹操(16) = 12; 12 * 2 = 24
            self.assertEqual(self.game.stats['damage']['關羽'], 24)

    def test_faction_stats(self):
        """測試 6: 勢力統計"""
        self.game.simulate_battle()
        stats = self.game.get_faction_stats()
        self.assertTrue('蜀' in stats or '吳' in stats or '魏' in stats)

    def test_ranking_length(self):
        """測試 7: 排名長度"""
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        self.assertLessEqual(len(ranking), 5)

    def test_eof_handling(self):
        """測試 8: EOF 處理"""
        self.assertEqual(len(self.game.generals), 9)

if __name__ == "__main__":
    unittest.main()
