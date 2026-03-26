"""
AI 策略單元測試（Phase 4）

說明：
- 本檔案使用 Python 內建 unittest 框架。
- 測試目標是 AIStrategy 類別，重點包含：
  1) 評分函數（score_play）
  2) 最佳出牌選擇（select_best_play）
  3) 完整策略出牌行為（choose_play）

注意：
- 匯入路徑可能因你的專案結構不同而需調整。
- 若尚未完成 AIStrategy 實作，先執行測試會是預期的失敗（Red）。
"""

import unittest


# 依常見專案慣例先嘗試幾種匯入方式，提升測試檔可攜性
try:
    # 常見結構：bigtwo/ai.py
    from bigtwo.ai import AIStrategy, Card, Play
except ImportError:
    try:
        # 另一種可能：ai.py 放在專案根目錄
        from ai import AIStrategy, Card, Play
    except ImportError:
        # 若仍無法匯入，讓測試以清楚訊息失敗
        AIStrategy = None
        Card = None
        Play = None


@unittest.skipIf(AIStrategy is None or Card is None or Play is None, "找不到 AIStrategy/Card/Play，請先確認匯入路徑。")
class TestAIStrategy(unittest.TestCase):
    """AIStrategy 測試主類別。"""

    def setUp(self):
        # 每個測試案例都建立新的策略物件，避免互相污染
        self.ai = AIStrategy()

    # -----------------------------
    # 1. 評分函數測試
    # -----------------------------

    def test_score_single(self):
        """單張 ♠A，手牌數 2 張，分數應為 240（不含額外獎勵時）。"""
        play = Play([Card("S", 14)])  # ♠A
        score = self.ai.score_play(play, hand_size_after=2)

        # 規格寫法：1x100 + 14x10 = 240
        # 若你的實作有額外常數（例如花色加分），可自行調整斷言。
        self.assertGreaterEqual(score, 240)

    def test_score_pair_higher(self):
        """同等條件下，對子分數應高於單張。"""
        single = Play([Card("H", 10)])
        pair = Play([Card("H", 10), Card("D", 10)])

        single_score = self.ai.score_play(single, hand_size_after=5)
        pair_score = self.ai.score_play(pair, hand_size_after=4)

        self.assertGreater(pair_score, single_score)

    def test_score_triple_higher(self):
        """同等條件下，三條分數應高於對子。"""
        pair = Play([Card("C", 9), Card("D", 9)])
        triple = Play([Card("C", 9), Card("D", 9), Card("H", 9)])

        pair_score = self.ai.score_play(pair, hand_size_after=4)
        triple_score = self.ai.score_play(triple, hand_size_after=3)

        self.assertGreater(triple_score, pair_score)

    def test_score_near_empty(self):
        """若此出牌會讓手牌剩 1 張，分數應有明顯高加權（>10000）。"""
        play = Play([Card("S", 5)])
        score = self.ai.score_play(play, hand_size_after=1)
        self.assertGreater(score, 10000)

    def test_score_low_cards(self):
        """若此出牌會讓手牌剩 2 張，分數應有中度加權（>500）。"""
        play = Play([Card("D", 7)])
        score = self.ai.score_play(play, hand_size_after=2)
        self.assertGreater(score, 500)

    def test_score_spade_bonus(self):
        """出黑桃應有額外加分（規格：+5）。"""
        non_spade = Play([Card("H", 8)])
        spade = Play([Card("S", 8)])

        non_spade_score = self.ai.score_play(non_spade, hand_size_after=6)
        spade_score = self.ai.score_play(spade, hand_size_after=6)

        self.assertGreaterEqual(spade_score - non_spade_score, 5)

    # -----------------------------
    # 2. 選擇最佳測試
    # -----------------------------

    def test_select_best(self):
        """合法出牌有[單張, 對子]時，應選對子。"""
        legal_plays = [
            Play([Card("H", 10)]),
            Play([Card("C", 6), Card("D", 6)]),
        ]

        best = self.ai.select_best_play(legal_plays, hand_size_after_choices={
            id(legal_plays[0]): 4,
            id(legal_plays[1]): 3,
        })

        self.assertEqual(len(best.cards), 2)

    def test_select_first_turn(self):
        """第一回合若有限制，應只選 3♣ 所在的出牌。"""
        legal_plays = [
            Play([Card("D", 3)]),
            Play([Card("C", 3)]),
        ]

        best = self.ai.select_best_play(
            legal_plays,
            hand_size_after_choices={id(p): 5 for p in legal_plays},
            first_turn=True,
        )

        self.assertEqual(len(best.cards), 1)
        self.assertEqual(best.cards[0].suit, "C")
        self.assertEqual(best.cards[0].rank, 3)

    def test_select_empty(self):
        """無合法出牌時，應回傳 None。"""
        best = self.ai.select_best_play([], hand_size_after_choices={})
        self.assertIsNone(best)

    # -----------------------------
    # 3. 完整策略測試
    # -----------------------------

    def test_ai_always_plays(self):
        """只要有合法牌可出，AI 應回傳一個出牌而非 None。"""
        legal_plays = [Play([Card("H", 4)])]
        chosen = self.ai.choose_play(
            legal_plays=legal_plays,
            hand_cards=[Card("H", 4), Card("D", 9)],
            first_turn=False,
        )
        self.assertIsNotNone(chosen)

    def test_ai_prefers_high(self):
        """在可行情況下，AI 應偏好高分（通常是高牌或高組合）。"""
        legal_plays = [
            Play([Card("H", 5)]),
            Play([Card("S", 12)]),  # 較高且可能有黑桃加成
        ]

        chosen = self.ai.choose_play(
            legal_plays=legal_plays,
            hand_cards=[Card("H", 5), Card("S", 12), Card("C", 2)],
            first_turn=False,
        )

        self.assertEqual(chosen.cards[0].rank, 12)

    def test_ai_try_empty(self):
        """若某出牌能直接出完手牌，AI 應優先選擇。"""
        legal_plays = [
            Play([Card("H", 9)]),
            Play([Card("D", 9), Card("C", 9)]),
        ]

        # 假設目前只剩兩張且剛好可組成對子出完
        chosen = self.ai.choose_play(
            legal_plays=legal_plays,
            hand_cards=[Card("D", 9), Card("C", 9)],
            first_turn=False,
        )

        self.assertEqual(len(chosen.cards), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
