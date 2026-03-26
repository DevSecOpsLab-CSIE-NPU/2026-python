import importlib
import unittest


# 動態匯入：若 ai/classifier/models 尚未完成，先以 skip 顯示。
try:
    models = importlib.import_module("models")
    classifier_mod = importlib.import_module("classifier")
    ai_mod = importlib.import_module("ai")

    Card = models.Card
    Hand = models.Hand
    CardType = classifier_mod.CardType
    AIStrategy = ai_mod.AIStrategy

    AI_AVAILABLE = True
except Exception:
    Card = Hand = CardType = AIStrategy = None
    AI_AVAILABLE = False


def c(rank: int, suit: int):
    """建立測試卡牌。"""
    return Card(rank, suit)


@unittest.skipUnless(AI_AVAILABLE, "找不到 ai.py / classifier.py / models.py，請先完成 Phase 4 實作")
class TestAIScore(unittest.TestCase):
    """評分函數測試。"""

    def test_score_single(self):
        # 單張 A，且手上共有 2 張牌：
        # 1*100 + 14*10 + 500(剩 <=3 張) = 740
        hand = Hand([c(14, 3), c(3, 0)])
        score = AIStrategy.score_play([c(14, 3)], hand)
        self.assertEqual(score, 740)

    def test_score_pair_higher(self):
        hand = Hand([c(14, 3), c(14, 2), c(3, 0), c(4, 1)])
        single_score = AIStrategy.score_play([c(14, 3)], hand)
        pair_score = AIStrategy.score_play([c(14, 3), c(14, 2)], hand)
        self.assertGreater(pair_score, single_score)

    def test_score_triple_higher(self):
        hand = Hand([c(14, 3), c(14, 2), c(14, 1), c(3, 0), c(4, 1)])
        pair_score = AIStrategy.score_play([c(14, 3), c(14, 2)], hand)
        triple_score = AIStrategy.score_play([c(14, 3), c(14, 2), c(14, 1)], hand)
        self.assertGreater(triple_score, pair_score)

    def test_score_near_empty(self):
        # 出完後只剩 1 張，應有超大加分。
        hand = Hand([c(14, 3), c(3, 0)])
        score = AIStrategy.score_play([c(14, 3)], hand)
        self.assertGreater(score, 10000)

    def test_score_low_cards(self):
        # 出完後剩 2 張，應至少含 near-empty 加分。
        hand = Hand([c(14, 3), c(3, 0), c(4, 1)])
        score = AIStrategy.score_play([c(14, 3)], hand)
        self.assertGreater(score, 500)

    def test_score_spade_bonus(self):
        hand = Hand([c(14, 3), c(14, 2), c(3, 0), c(4, 1), c(5, 2)])
        spade_score = AIStrategy.score_play([c(14, 3)], hand)
        heart_score = AIStrategy.score_play([c(14, 2)], hand)
        self.assertEqual(spade_score - heart_score, 5)


@unittest.skipUnless(AI_AVAILABLE, "找不到 ai.py / classifier.py / models.py，請先完成 Phase 4 實作")
class TestAISelectBest(unittest.TestCase):
    """選擇最佳出牌測試。"""

    def test_select_best(self):
        hand = Hand([c(14, 3), c(14, 2), c(3, 0), c(4, 1)])
        valid_plays = [[c(14, 3)], [c(14, 3), c(14, 2)]]
        selected = AIStrategy.select_best(valid_plays, hand)
        self.assertEqual(selected, [c(14, 3), c(14, 2)])

    def test_select_first_turn(self):
        # 第一回合應優先出含 3♣ 的牌。
        hand = Hand([c(3, 0), c(14, 3), c(14, 2)])
        valid_plays = [[c(14, 3)], [c(3, 0)], [c(14, 3), c(14, 2)]]
        selected = AIStrategy.select_best(valid_plays, hand, is_first=True)
        self.assertEqual(selected, [c(3, 0)])

    def test_select_empty(self):
        hand = Hand([c(14, 3)])
        selected = AIStrategy.select_best([], hand)
        self.assertIsNone(selected)


@unittest.skipUnless(AI_AVAILABLE, "找不到 ai.py / classifier.py / models.py，請先完成 Phase 4 實作")
class TestAIStrategyIntegration(unittest.TestCase):
    """完整策略行為測試。"""

    def test_ai_always_plays(self):
        hand = Hand([c(14, 3), c(13, 2)])
        valid_plays = [[c(14, 3)], [c(13, 2)]]
        selected = AIStrategy.select_best(valid_plays, hand)
        self.assertIsNotNone(selected)

    def test_ai_prefers_high(self):
        hand = Hand([c(14, 3), c(5, 0)])
        valid_plays = [[c(5, 0)], [c(14, 3)]]
        selected = AIStrategy.select_best(valid_plays, hand)
        self.assertEqual(selected, [c(14, 3)])

    def test_ai_try_empty(self):
        # 剩最後一張時，應選擇可直接出完的牌。
        hand = Hand([c(14, 3)])
        valid_plays = [[c(14, 3)]]
        selected = AIStrategy.select_best(valid_plays, hand)
        self.assertEqual(selected, [c(14, 3)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
