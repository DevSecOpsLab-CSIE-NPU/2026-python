# p4-ai-unit-test.py
# Phase 4 單元測試：AIStrategy
#
# 測試依據：p4-test.md
# 依賴：p1_models.py、p2_classifier.py、p4_ai.py（請自行建立實作）
#
# 評分公式（參見 p4-dev.md）：
#   score = 牌型值 × 100 + 代表點數 × 10 + 剩餘加分
#   剩餘 1 張  → +10000
#   剩餘 ≤ 3 張 → +500
#   每張 ♠    → +5
#
# 執行方式：
#   python p4-ai-unit-test.py

import unittest
from p1_models import Card, Hand
from p2_classifier import CardType

# 請在完成 p4_ai.py 後取消下方的 import 註解
from p4_ai import AIStrategy


# =========================================================
# TestScorePlay — 評分函數
# =========================================================
class TestScorePlay(unittest.TestCase):

    def test_score_single(self):
        """單張 ♠A，手牌剩 2 張：score = 1×100 + 14×10 = 240（無額外加分）。"""
        hand = Hand([Card(14, 3), Card(3, 0)])
        cards = [Card(14, 3)]
        score = AIStrategy.score_play(cards, hand)
        # 出完後手牌剩 1 張，但計算基底仍是 SINGLE×100 + 14×10
        # 若出完剩 1 張則 +10000；這裡驗證 score > SINGLE×100 + 14×10 基底
        base = CardType.SINGLE * 100 + 14 * 10  # 240
        self.assertGreaterEqual(score, base)

    def test_score_pair_higher_than_single(self):
        """對子出牌的分數應高於單張（相同點數下，PAIR(2) > SINGLE(1)）。"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(13, 0)])
        score_pair = AIStrategy.score_play([Card(14, 3), Card(14, 2)], hand)
        score_single = AIStrategy.score_play([Card(14, 3)], hand)
        self.assertGreater(score_pair, score_single)

    def test_score_triple_higher_than_pair(self):
        """三條出牌的分數應高於對子。"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0)])
        score_triple = AIStrategy.score_play(
            [Card(14, 3), Card(14, 2), Card(14, 1)], hand
        )
        score_pair = AIStrategy.score_play([Card(14, 3), Card(14, 2)], hand)
        self.assertGreater(score_triple, score_pair)

    def test_score_near_empty_bonus(self):
        """出完後剩 1 張，分數應超過 10000（加分觸發）。"""
        hand = Hand([Card(14, 3), Card(3, 0)])
        score = AIStrategy.score_play([Card(14, 3)], hand)
        self.assertGreater(score, 10000)

    def test_score_low_cards_bonus(self):
        """出完後剩 ≤ 3 張，分數應超過 500。"""
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0), Card(5, 1)])
        score = AIStrategy.score_play([Card(14, 3)], hand)
        self.assertGreater(score, 500)

    def test_score_spade_bonus(self):
        """出 ♠ 牌比出 ♣ 同點數的分數高（♠ 加分）。"""
        hand = Hand([Card(14, 3), Card(14, 0), Card(3, 0)])
        score_spade = AIStrategy.score_play([Card(14, 3)], hand)   # ♠A
        score_club = AIStrategy.score_play([Card(14, 0)], hand)    # ♣A
        self.assertGreater(score_spade, score_club)


# =========================================================
# TestSelectBest — 選擇最佳出牌
# =========================================================
class TestSelectBest(unittest.TestCase):

    def test_select_best_prefers_higher_type(self):
        """有對子與單張可選時，AI 應選擇牌型較高的對子。"""
        hand = Hand([Card(3, 0), Card(3, 1), Card(14, 3)])
        valid = [
            [Card(14, 3)],          # 單張 A
            [Card(3, 0), Card(3, 1)],  # 對 3
        ]
        best = AIStrategy.select_best(valid, hand)
        # 對子牌型（PAIR=2）> 單張（SINGLE=1），應選對 3
        self.assertEqual(len(best), 2)

    def test_select_first_turn(self):
        """第一回合（is_first=True），應選含 3♣ 的出牌。"""
        hand = Hand([Card(3, 0), Card(14, 3)])
        valid = [
            [Card(3, 0)],    # 3♣
            [Card(14, 3)],   # ♠A（不合規，但 valid 已預過濾）
        ]
        best = AIStrategy.select_best(valid, hand, is_first=True)
        self.assertIn(Card(3, 0), best)

    def test_select_empty(self):
        """合法出牌為空時，應回傳 None（表示 pass）。"""
        hand = Hand([Card(14, 3)])
        best = AIStrategy.select_best([], hand)
        self.assertIsNone(best)


# =========================================================
# TestAIStrategy — 完整策略
# =========================================================
class TestAIStrategy(unittest.TestCase):

    def test_ai_always_plays_when_possible(self):
        """只要有合法出牌，select_best 不應回傳 None。"""
        hand = Hand([Card(14, 3), Card(13, 2)])
        valid = [[Card(14, 3)], [Card(13, 2)]]
        result = AIStrategy.select_best(valid, hand)
        self.assertIsNotNone(result)

    def test_ai_prefers_high_card(self):
        """有高牌與低牌的單張可選時，AI 應選分數較高的（高牌）。"""
        hand = Hand([Card(14, 3), Card(3, 0)])
        valid = [[Card(14, 3)], [Card(3, 0)]]
        best = AIStrategy.select_best(valid, hand)
        # 高牌 ♠A（rank=14）分數 > 低牌 3♣（rank=3）
        self.assertIn(Card(14, 3), best)

    def test_ai_tries_to_empty_hand(self):
        """剩最後一張時，AI 應傾向選擇出完（near-empty bonus 驅動）。"""
        hand = Hand([Card(14, 3)])
        valid = [[Card(14, 3)]]
        best = AIStrategy.select_best(valid, hand)
        self.assertEqual(best, [Card(14, 3)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
