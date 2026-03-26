import unittest

from game.cards import Card, Hand

# 說明：若專案尚未實作 AIStrategy，此測試檔可先建立（Red 階段）。
# 後續只要補上 game.ai.AIStrategy 即可直接驗證。
from game.ai import AIStrategy  # type: ignore


def C(suit: int, rank: int) -> Card:
    """建立測試用 Card 物件的簡寫函式。"""
    return Card(suit=suit, rank=rank)


class TestAIScore(unittest.TestCase):
    """測試 AI 評分函數 _score_play 的核心規則。"""

    def setUp(self) -> None:
        self.ai = AIStrategy()

    def test_score_single(self):
        # 規格：單張分數 = 牌型權重(1*100) + 點數(14*10)；手牌 2 張不觸發收尾加成。
        hand = Hand([C(3, 14), C(0, 5)])
        play = [C(3, 14)]
        score = self.ai._score_play(play, hand)  # type: ignore[attr-defined]
        self.assertEqual(score, 240)

    def test_score_pair_higher(self):
        # 規格：對子分數應高於單張。
        hand = Hand([C(0, 9), C(1, 9), C(2, 4)])
        single_score = self.ai._score_play([C(2, 4)], hand)  # type: ignore[attr-defined]
        pair_score = self.ai._score_play([C(0, 9), C(1, 9)], hand)  # type: ignore[attr-defined]
        self.assertGreater(pair_score, single_score)

    def test_score_triple_higher(self):
        # 規格：三條分數應高於對子。
        hand = Hand([C(0, 8), C(1, 8), C(2, 8), C(3, 7)])
        pair_score = self.ai._score_play([C(0, 8), C(1, 8)], hand)  # type: ignore[attr-defined]
        triple_score = self.ai._score_play([C(0, 8), C(1, 8), C(2, 8)], hand)  # type: ignore[attr-defined]
        self.assertGreater(triple_score, pair_score)

    def test_score_near_empty(self):
        # 規格：當手上只剩 1 張且本次出牌可出完時，分數需非常高（>10000）。
        hand = Hand([C(3, 13)])
        play = [C(3, 13)]
        score = self.ai._score_play(play, hand)  # type: ignore[attr-defined]
        self.assertGreater(score, 10000)

    def test_score_low_cards(self):
        # 規格：當手上剩 2 張且本次出牌可收尾時，分數應有明顯加成（>500）。
        hand = Hand([C(0, 6), C(1, 6)])
        play = [C(0, 6), C(1, 6)]
        score = self.ai._score_play(play, hand)  # type: ignore[attr-defined]
        self.assertGreater(score, 500)

    def test_score_spade_bonus(self):
        # 規格：若出牌包含黑桃（suit=3），分數需有額外 +5（至少反映為黑桃比分較高）。
        hand = Hand([C(3, 10), C(2, 10)])
        spade_score = self.ai._score_play([C(3, 10)], hand)  # type: ignore[attr-defined]
        non_spade_score = self.ai._score_play([C(2, 10)], hand)  # type: ignore[attr-defined]
        self.assertGreaterEqual(spade_score, non_spade_score + 5)


class TestAISelectBest(unittest.TestCase):
    """測試 AI 在多個合法出牌中如何挑選最佳策略。"""

    def setUp(self) -> None:
        self.ai = AIStrategy()

    def test_select_best(self):
        # 規格：合法出牌同時有單張與對子時，應優先選擇對子。
        hand = Hand([C(0, 6), C(1, 6), C(2, 4)])
        valid_plays = [[C(2, 4)], [C(0, 6), C(1, 6)]]
        best = self.ai._select_best_play(valid_plays, hand)  # type: ignore[attr-defined]
        self.assertEqual(best, [C(0, 6), C(1, 6)])

    def test_select_first_turn(self):
        # 規格：第一回合限制需出 3♣（suit=0, rank=3）。
        hand = Hand([C(0, 3), C(3, 14), C(1, 7)])
        valid_plays = [[C(0, 3)], [C(3, 14)]]
        best = self.ai.select_play(hand, last_play=None, is_first_turn=True)
        self.assertEqual(best, [C(0, 3)])

    def test_select_empty(self):
        # 規格：若無合法出牌，應回傳 None。
        hand = Hand([C(2, 9)])
        best = self.ai._select_best_play([], hand)  # type: ignore[attr-defined]
        self.assertIsNone(best)


class TestAIStrategyIntegration(unittest.TestCase):
    """測試完整策略流程（含找合法牌與評分決策）。"""

    def setUp(self) -> None:
        self.ai = AIStrategy()

    def test_ai_always_plays(self):
        # 規格：只要存在合法出牌，AI 不應該 pass。
        hand = Hand([C(0, 3), C(1, 5), C(2, 5)])
        play = self.ai.select_play(hand, last_play=None, is_first_turn=True)
        self.assertIsNotNone(play)

    def test_ai_prefers_high(self):
        # 規格：在可比較的同類型牌中，AI 應傾向出較大牌。
        hand = Hand([C(0, 8), C(1, 11), C(2, 6), C(3, 3)])
        play = self.ai.select_play(hand, last_play=[C(0, 7)], is_first_turn=False)
        self.assertIsNotNone(play)
        self.assertEqual(len(play), 1)
        self.assertEqual(play[0].rank, 11)

    def test_ai_try_empty(self):
        # 規格：剩最後一張時，AI 應選擇可直接出完的那張。
        hand = Hand([C(1, 9)])
        play = self.ai.select_play(hand, last_play=None, is_first_turn=False)
        self.assertEqual(play, [C(1, 9)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
