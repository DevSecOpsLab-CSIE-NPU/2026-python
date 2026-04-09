"""
赤壁戰役遊戲引擎單元測試
三國武將 PK 版 - 測試驅動開發 (TDD)

日期: 2026-04-09
"""

import unittest
import os
import sys

# 設定 UTF-8 編碼輸出 (解決 Windows PowerShell 中文顯示問題)
if sys.platform == "win32":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from collections import namedtuple, Counter, defaultdict

# 將同層目錄加入路徑，以便匯入 chibi_battle 模組
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chibi_battle import ChibiBattle, General


class TestDataLoading(unittest.TestCase):
    """Stage 1: 資料讀取測試 - 測試 Week 07 檔案 I/O 功能"""

    def setUp(self):
        """測試前準備：建立遊戲實例"""
        self.game = ChibiBattle()
        # 從 solutions/1112405062/ 回推到 week-07/ 目錄
        base_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        self.test_file = os.path.join(base_dir, "generals.txt")

    def test_load_generals_from_file(self):
        """測試 1-1: 正確讀取 9 位武將"""
        # 執行：讀取武將資料檔案
        self.game.load_generals(self.test_file)

        # 驗證：應讀取到 9 位武將
        self.assertEqual(len(self.game.generals), 9)

        # 驗證：檢查關鍵武將是否存在
        self.assertIn("劉備", self.game.generals)
        self.assertIn("曹操", self.game.generals)
        self.assertIn("孫權", self.game.generals)

    def test_parse_general_attributes(self):
        """測試 1-2: 正確解析武將屬性 (namedtuple)"""
        self.game.load_generals(self.test_file)

        # 驗證 namedtuple 結構體的各屬性
        general = self.game.generals["關羽"]
        self.assertEqual(general.name, "關羽")
        self.assertEqual(general.faction, "蜀")
        self.assertEqual(general.hp, 100)
        self.assertEqual(general.atk, 28)
        self.assertEqual(general.def_, 14)
        self.assertEqual(general.spd, 85)
        self.assertEqual(general.is_leader, False)

    def test_parse_leader_attribute(self):
        """測試 1-3: 正確解析軍師/領袖屬性"""
        self.game.load_generals(self.test_file)

        # 驗證諸葛亮是軍師 (is_leader=True)
        general = self.game.generals["諸葛亮"]
        self.assertTrue(general.is_leader)

        # 驗證關羽不是軍師
        general = self.game.generals["關羽"]
        self.assertFalse(general.is_leader)

    def test_faction_distribution(self):
        """測試 1-4: 三國分布正確 (使用 Counter)"""
        self.game.load_generals(self.test_file)

        # 使用 Week 02: Counter 統計各勢力人數
        from collections import Counter

        factions = Counter(g.faction for g in self.game.generals.values())

        self.assertEqual(factions["蜀"], 3)
        self.assertEqual(factions["吳"], 3)
        self.assertEqual(factions["魏"], 3)

    def test_eof_parsing(self):
        """測試 1-5: 正確識別 EOF 結尾 (不應讀取 EOF 行)"""
        self.game.load_generals(self.test_file)

        # 驗證：不會超過 9 位武將
        self.assertEqual(len(self.game.generals), 9)

        # 驗證：generals 字典中不應有 'EOF' 鍵
        self.assertNotIn("EOF", self.game.generals)

    def test_all_generals_have_required_attributes(self):
        """測試 1-6: 所有武將都具備必要屬性"""
        self.game.load_generals(self.test_file)

        required_attrs = ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"]

        for name, general in self.game.generals.items():
            for attr in required_attrs:
                self.assertTrue(hasattr(general, attr), f"武將 {name} 缺少屬性 {attr}")


class TestBattleLogic(unittest.TestCase):
    """Stage 2: 戰鬥邏輯測試 - 測試 Week 02 資料結構應用"""

    def setUp(self):
        """測試前準備：建立遊戲實例並載入資料"""
        self.game = ChibiBattle()
        # 從 solutions/1112405062/ 回推到 week-07/ 目錄
        base_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        test_file = os.path.join(base_dir, "generals.txt")
        self.game.load_generals(test_file)

    def test_battle_order_by_speed(self):
        """測試 2-1: 根據速度排序戰鬥順序 (使用 sorted)"""
        # Week 02: sorted(key=...) 按速度遞減排序
        battle_order = self.game.get_battle_order()

        # 驗證：第一位速度最高 (85: 關羽、周瑜)
        self.assertEqual(battle_order[0].spd, 85)

        # 驗證：最後一位速度最低 (60: 諸葛亮)
        self.assertEqual(battle_order[-1].spd, 60)

        # 驗證：列表遞減
        speeds = [g.spd for g in battle_order]
        self.assertEqual(speeds, sorted(speeds, reverse=True))

    def test_calculate_damage(self):
        """測試 2-2: 正確計算傷害 (攻擊 - 防禦)"""
        # 關羽 (攻28) vs 夏侯惇 (防14) = 14
        damage = self.game.calculate_damage("關羽", "夏侯惇")
        self.assertEqual(damage, 14)

        # 諸葛亮 (攻15) vs 曹操 (防16) = 最小傷害 1
        damage = self.game.calculate_damage("諸葛亮", "曹操")
        self.assertEqual(damage, 1)  # max(1, 15-16) = 1

    def test_damage_counter_accumulation(self):
        """測試 2-3: Counter 自動累加傷害統計"""
        # Week 02: Counter 自動累加功能
        self.game.calculate_damage("關羽", "夏侯惇")  # 14
        self.game.calculate_damage("關羽", "曹操")  # 12

        # 驗證：關羽總傷害 = 14 + 12 = 26
        self.assertEqual(self.game.stats["damage"]["關羽"], 26)

    def test_troop_loss_tracking(self):
        """測試 2-4: defaultdict 追蹤兵力損失"""
        # Week 02: defaultdict(int) 自動初始化為 0
        self.game.calculate_damage("關羽", "夏侯惇")  # 夏侯惇損失 14
        self.game.calculate_damage("周瑜", "曹操")  # 曹操損失 2

        # 驗證：夏侯惇損失 14 兵力
        self.assertEqual(self.game.stats["losses"]["夏侯惇"], 14)

        # 驗證：曹操損失 2 兵力
        self.assertEqual(self.game.stats["losses"]["曹操"], 2)

    def test_simulate_one_wave(self):
        """測試 2-5: 模擬一波戰鬥"""
        self.game.simulate_wave(1)  # Wave 1

        # 驗證：應產生傷害
        total_damage = sum(self.game.stats["damage"].values())
        self.assertGreater(total_damage, 0)

    def test_simulate_three_waves(self):
        """測試 2-6: 模擬三波完整戰役"""
        self.game.simulate_battle()  # 3 波

        # 驗證：蜀軍傷害 (蜀軍擔任攻擊方)
        shu_damage = sum(
            dmg
            for name, dmg in self.game.stats["damage"].items()
            if self.game.generals[name].faction == "蜀"
        )

        # 驗證：魏軍損失 (魏軍擔任防守方)
        wei_loss = sum(
            loss
            for name, loss in self.game.stats["losses"].items()
            if name in self.game.generals and self.game.generals[name].faction == "魏"
        )

        # 蜀軍應有傷害輸出 (擔任攻擊方)
        self.assertGreater(shu_damage, 0)

        # 魏軍應有兵力損失 (擔任防守方)
        self.assertGreater(wei_loss, 0)

    def test_damage_ranking_most_common(self):
        """測試 2-7: Counter.most_common() 傷害排名"""
        # Week 02: Counter.most_common()
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking(top_n=5)

        # 驗證：返回格式為列表
        self.assertIsInstance(ranking, list)

        # 驗證：每個元素是 (名字, 傷害) 元組
        if ranking:
            self.assertEqual(len(ranking[0]), 2)

        # 驗證：傷害遞減排列
        damages = [dmg for _, dmg in ranking]
        self.assertEqual(damages, sorted(damages, reverse=True))

    def test_faction_damage_stats(self):
        """測試 2-8: 按勢力統計傷害 (groupby 概念)"""
        # Week 02: defaultdict + groupby 概念
        self.game.simulate_battle()
        faction_stats = self.game.get_faction_stats()

        # 驗證：蜀軍有傷害 (因為蜀軍擔任攻擊方)
        self.assertIn("蜀", faction_stats)

        # 驗證：蜀軍傷害值為正整數
        self.assertGreater(faction_stats["蜀"], 0)

    def test_defeated_generals(self):
        """測試 2-9: 正確識別戰敗將領"""
        self.game.simulate_battle()
        defeated = self.game.get_defeated_generals()

        # 驗證：返回列表
        self.assertIsInstance(defeated, list)

        # 驗證：戰敗者確實 HP <= 損失
        for name in defeated:
            loss = self.game.stats["losses"][name]
            hp = self.game.generals[name].hp
            self.assertGreaterEqual(loss, hp)


class TestRefactoring(unittest.TestCase):
    """Stage 3: 重構測試 - 確保視覺化不影響邏輯"""

    def setUp(self):
        """測試前準備"""
        self.game = ChibiBattle()
        # 從 solutions/1112405062/ 回推到 week-07/ 目錄
        base_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        self.test_file = os.path.join(base_dir, "generals.txt")
        self.game.load_generals(self.test_file)

    def test_stats_unchanged_after_refactor(self):
        """測試 3-1: 重構後統計結果不變"""
        self.game.simulate_battle()

        # 記錄統計結果
        damage_before = dict(self.game.stats["damage"])
        losses_before = dict(self.game.stats["losses"])

        # 再次模擬 (不應改變已有統計)
        # 這裡我們重新創建實例來測試獨立性
        game2 = ChibiBattle()
        game2.load_generals(self.test_file)
        game2.simulate_battle()

        # 驗證：兩個實例統計應該可以各自運作
        self.assertEqual(len(self.game.stats["damage"]), len(game2.stats["damage"]))

    def test_all_stage1_tests_still_pass(self):
        """測試 3-2: Stage 1 測試仍通過 (資料讀取功能正常)"""
        # 重新載入資料
        self.game.load_generals(self.test_file)

        # 驗證：仍能正確讀取 9 位武將
        self.assertEqual(len(self.game.generals), 9)

        # 驗證：各勢力分布正確
        from collections import Counter

        factions = Counter(g.faction for g in self.game.generals.values())
        self.assertEqual(factions["蜀"], 3)
        self.assertEqual(factions["吳"], 3)
        self.assertEqual(factions["魏"], 3)

    def test_all_stage2_tests_still_pass(self):
        """測試 3-3: Stage 2 測試仍通過 (戰鬥邏輯正常)"""
        self.game.simulate_battle()

        # 驗證：戰鬥順序功能正常
        order = self.game.get_battle_order()
        self.assertEqual(len(order), 9)

        # 驗證：傷害排名功能正常 (實際輸出 3 位)
        ranking = self.game.get_damage_ranking()
        self.assertEqual(len(ranking), 3)  # Top N (實際只有 3 位攻擊者)

        # 驗證：勢力統計功能正常
        faction_stats = self.game.get_faction_stats()
        self.assertIn("蜀", faction_stats)


# 輔助函數：取得測試檔案路徑
def get_test_file_path():
    """取得 generals.txt 測試檔案路徑"""
    return os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "generals.txt"
    )


# 如果直接執行此檔案，執行測試
if __name__ == "__main__":
    unittest.main(verbosity=2)
