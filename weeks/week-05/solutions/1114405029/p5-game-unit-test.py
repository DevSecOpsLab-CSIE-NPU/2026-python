# p5-game-unit-test.py
# Phase 5 單元測試：BigTwoGame
#
# 測試依據：p5-test.md
# 依賴：p1_models.py、p2_classifier.py、p5_game.py（請自行建立實作）
#
# 執行方式：
#   python p5-game-unit-test.py

import unittest
from p1_models import Card, Hand, Player

# 請在完成 p5_game.py 後取消下方的 import 註解
from p5_game import BigTwoGame


# =========================================================
# TestGameSetup — 遊戲初始化
# =========================================================
class TestGameSetup(unittest.TestCase):

    def setUp(self):
        """每個測試前建立並初始化一局遊戲。"""
        self.game = BigTwoGame()
        self.game.setup()

    def test_game_has_4_players(self):
        """setup() 後，遊戲應有恰好 4 位玩家。"""
        self.assertEqual(len(self.game.players), 4)

    def test_each_player_13_cards(self):
        """每位玩家手牌應恰好 13 張。"""
        for p in self.game.players:
            self.assertEqual(len(p.hand), 13,
                             msg=f"玩家 {p.name} 應有 13 張，實際 {len(p.hand)} 張")

    def test_total_cards_distributed(self):
        """所有玩家手牌合計應為 52 張。"""
        total = sum(len(p.hand) for p in self.game.players)
        self.assertEqual(total, 52)

    def test_first_player_has_3_clubs(self):
        """先手玩家（current_player）的手牌必定含有 3♣。"""
        first = self.game.get_current_player()
        self.assertIsNotNone(first.hand.find_3_clubs())

    def test_one_human_three_ai(self):
        """遊戲應有 1 位人類玩家與 3 位 AI。"""
        humans = [p for p in self.game.players if not p.is_ai]
        ais = [p for p in self.game.players if p.is_ai]
        self.assertEqual(len(humans), 1)
        self.assertEqual(len(ais), 3)


# =========================================================
# TestPlayFlow — 出牌流程
# =========================================================
class TestPlayFlow(unittest.TestCase):

    def setUp(self):
        self.game = BigTwoGame()
        self.game.setup()
        # 取得先手玩家（持有 3♣）
        self.first = self.game.get_current_player()

    def test_play_removes_cards(self):
        """出牌後先手玩家手牌應減少。"""
        before = len(self.first.hand)
        result = self.game.play(self.first, [Card(3, 0)])
        self.assertTrue(result)
        self.assertEqual(len(self.first.hand), before - 1)

    def test_play_sets_last_play(self):
        """合法出牌後，last_play 應更新為剛才出的牌。"""
        self.game.play(self.first, [Card(3, 0)])
        self.assertIsNotNone(self.game.last_play)

    def test_invalid_play_returns_false(self):
        """第一回合出非 3♣ 的牌 → 應回傳 False，手牌不變。"""
        # 找一張不是 3♣ 的牌
        other = next(c for c in self.first.hand if c != Card(3, 0))
        before = len(self.first.hand)
        result = self.game.play(self.first, [other])
        self.assertFalse(result)
        self.assertEqual(len(self.first.hand), before)

    def test_pass_increments_count(self):
        """過牌後 pass_count 應加 1。"""
        before = self.game.pass_count
        self.game.pass_(self.first)
        self.assertEqual(self.game.pass_count, before + 1)


# =========================================================
# TestRoundLogic — 回合判定
# =========================================================
class TestRoundLogic(unittest.TestCase):

    def setUp(self):
        self.game = BigTwoGame()
        self.game.setup()
        # 讓先手出 3♣，建立非 None 的 last_play
        first = self.game.get_current_player()
        self.game.play(first, [Card(3, 0)])
        self.game.next_turn()

    def test_three_passes_resets(self):
        """連續 3 人過牌後，last_play 應重置為 None（新回合）。"""
        for _ in range(3):
            p = self.game.get_current_player()
            self.game.pass_(p)
            self.game.next_turn()
        self.game.check_round_reset()
        self.assertIsNone(self.game.last_play)

    def test_turn_rotates(self):
        """next_turn() 應將 current_player 移至下一位（模 4）。"""
        before = self.game.current_player
        self.game.next_turn()
        self.assertEqual(self.game.current_player, (before + 1) % 4)


# =========================================================
# TestWinCondition — 獲勝判定
# =========================================================
class TestWinCondition(unittest.TestCase):

    def setUp(self):
        self.game = BigTwoGame()
        self.game.setup()

    def test_no_winner_at_start(self):
        """遊戲剛開始，尚無勝者，check_winner() 應回傳 None。"""
        self.assertIsNone(self.game.check_winner())

    def test_detect_winner(self):
        """將某位玩家手牌清空後，check_winner() 應回傳該玩家。"""
        target = self.game.players[0]
        target.hand.clear()          # 模擬該玩家出完所有牌
        winner = self.game.check_winner()
        self.assertEqual(winner, target)

    def test_game_over_false_at_start(self):
        """遊戲剛開始，is_game_over() 應為 False。"""
        self.assertFalse(self.game.is_game_over())

    def test_game_ends_when_winner(self):
        """有玩家手牌清空後，is_game_over() 應為 True。"""
        self.game.players[0].hand.clear()
        self.game.winner = self.game.check_winner()
        self.assertTrue(self.game.is_game_over())


if __name__ == "__main__":
    unittest.main(verbosity=2)
