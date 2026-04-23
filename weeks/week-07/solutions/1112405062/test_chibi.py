"""
赤壁戰役 - 單元測試
整合 Stage 1-3 測試案例

Week 02 技能：sorted, Counter, defaultdict, namedtuple
Week 07 技能：檔案 I/O, EOF 輸入處理
"""

import unittest
import os
from collections import Counter

from chibi_battle import ChibiBattle, General

TEST_DIR = os.path.dirname(os.path.abspath(__file__))


class TestStage1DataLoading(unittest.TestCase):
    """Stage 1: 資料讀取測試"""

    def setUp(self):
        """每個測試前準備測試環境"""
        self.game = ChibiBattle()
        self.game.load_generals(os.path.join(TEST_DIR, "generals.txt"))

    def test_load_generals_from_file(self):
        """測試 1-1: 正確讀取 9 位武將"""
        self.assertEqual(len(self.game.generals), 9)
        self.assertIn("劉備", self.game.generals)
        self.assertIn("曹操", self.game.generals)
        self.assertIn("孫權", self.game.generals)

    def test_parse_general_attributes(self):
        """測試 1-2: 正確解析武將屬性"""
        general = self.game.generals["關羽"]
        self.assertEqual(general.name, "關羽")
        self.assertEqual(general.atk, 28)
        self.assertEqual(general.def_, 14)
        self.assertEqual(general.spd, 85)
        self.assertEqual(general.faction, "蜀")

    def test_faction_distribution(self):
        """測試 1-3: 三國分布正確"""
        factions = Counter(g.faction for g in self.game.generals.values())
        self.assertEqual(factions["蜀"], 3)
        self.assertEqual(factions["吳"], 3)
        self.assertEqual(factions["魏"], 3)

    def test_eof_parsing(self):
        """測試 1-4: 正確識別 EOF 結尾"""
        self.assertEqual(len(self.game.generals), 9)

    def test_general_namedtuple_structure(self):
        """測試 1-5: namedtuple 結構正確"""
        general = self.game.generals["周瑜"]
        self.assertIsInstance(general, General)
        self.assertEqual(general.faction, "吳")
        self.assertEqual(general.hp, 85)
        self.assertEqual(general.is_leader, True)


class TestStage2BattleLogic(unittest.TestCase):
    """Stage 2: 戰鬥模擬與統計測試"""

    def setUp(self):
        """每個測試前準備"""
        self.game = ChibiBattle()
        self.game.load_generals(os.path.join(TEST_DIR, "generals.txt"))

    def test_battle_order_by_speed(self):
        """測試 2-1: 根據速度排序戰鬥順序"""
        battle_order = self.game.get_battle_order()
        speeds = [g.spd for g in battle_order]
        self.assertEqual(speeds, sorted(speeds, reverse=True))

    def test_calculate_damage(self):
        """測試 2-2: 正確計算傷害 (攻擊 - 防禦)"""
        damage = self.game.calculate_damage("關羽", "夏侯惇")
        self.assertEqual(damage, 28 - 14)

    def test_damage_counter_accumulation(self):
        """測試 2-3: Counter 自動累加傷害"""
        self.game.calculate_damage("關羽", "夏侯惇")
        self.game.calculate_damage("關羽", "曹操")
        self.assertEqual(self.game.stats["damage"]["關羽"], 14 + (28 - 16))

    def test_simulate_one_wave(self):
        """測試 2-4: 模擬一波戰鬥"""
        self.game.simulate_wave(1)
        total_damage = sum(self.game.stats["damage"].values())
        self.assertGreater(total_damage, 0)

    def test_simulate_three_waves(self):
        """測試 2-5: 模擬三波完整戰役"""
        self.game.simulate_battle()
        total_damage = sum(self.game.stats["damage"].values())
        self.assertGreater(total_damage, 0)

    def test_troop_loss_tracking(self):
        """測試 2-6: defaultdict 追蹤兵力損失"""
        self.game.simulate_battle()
        self.assertGreater(len(self.game.stats["losses"]), 0)

    def test_damage_ranking_most_common(self):
        """測試 2-7: most_common() 傷害排名"""
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        damages = [dmg for _, dmg in ranking]
        self.assertEqual(damages, sorted(damages, reverse=True))

    def test_faction_damage_stats(self):
        """測試 2-8: 按勢力統計傷害"""
        self.game.simulate_battle()
        faction_stats = self.game.get_faction_stats()
        self.assertGreater(faction_stats["蜀"], 0)

    def test_defeated_generals(self):
        """測試 2-9: 正確識別戰敗將領"""
        self.game.simulate_battle()
        defeated = self.game.get_defeated_generals()
        self.assertIsInstance(defeated, list)


class TestStage3Refactor(unittest.TestCase):
    """Stage 3: 重構測試"""

    def setUp(self):
        """每個測試前準備"""
        self.game = ChibiBattle()
        self.game.load_generals(os.path.join(TEST_DIR, "generals.txt"))

    def test_stats_unchanged_after_refactor(self):
        """測試 3-1: 重構後統計結果不變"""
        self.game.simulate_battle()
        damage_before = dict(self.game.stats["damage"])
        # 重新讀取（模擬重構後不影響邏輯）
        self.game = ChibiBattle()
        self.game.load_generals(os.path.join(TEST_DIR, "generals.txt"))
        self.game.simulate_battle()
        self.assertEqual(dict(self.game.stats["damage"]), damage_before)

    def test_all_stage1_tests_still_pass(self):
        """測試 3-2: Stage 1 測試仍通過"""
        self.game.load_generals(os.path.join(TEST_DIR, "generals.txt"))
        self.assertEqual(len(self.game.generals), 9)

    def test_all_stage2_tests_still_pass(self):
        """測試 3-3: Stage 2 測試仍通過"""
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        self.assertLessEqual(len(ranking), 5)


if __name__ == "__main__":
    unittest.main()
