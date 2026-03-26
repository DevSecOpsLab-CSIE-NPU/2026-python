# p4_ai.py
# Phase 4：AI 策略模組
#
# 功能：實作 AIStrategy 類別，讓 AI 玩家能從合法出牌中挑出最佳選擇。
# 依賴：p1_models.py（Card, Hand）、p2_classifier.py（CardType, HandClassifier）
#
# 評分公式：
#   score = 牌型值 × 100 + 代表點數 × 10
#         + 剩餘加分（剩 0 或 1 張 → +10000；剩 2~3 張 → +500）
#         + 黑桃加分（每張 ♠ → +5）
#
# 執行測試：
#   python p4-ai-unit-test.py

from __future__ import annotations

from typing import List, Optional

from p1_models import Card, Hand
from p2_classifier import CardType, HandClassifier


class AIStrategy:
    """AI 策略器：評估每組出牌的分數，並從合法出牌中選出最佳一手。"""

    # -------------------------------------------------------
    # 類別常數：各牌型的基礎分數倍率（與 CardType 數值相同）
    # -------------------------------------------------------
    TYPE_SCORES = {
        CardType.SINGLE:        1,
        CardType.PAIR:          2,
        CardType.TRIPLE:        3,
        CardType.STRAIGHT:      4,
        CardType.FLUSH:         5,
        CardType.FULL_HOUSE:    6,
        CardType.FOUR_OF_A_KIND: 7,
        CardType.STRAIGHT_FLUSH: 8,
    }

    # 剩 0 或 1 張時，大幅加分（快速結束最優先）
    EMPTY_HAND_BONUS = 10000
    # 剩 2 或 3 張時，輕微加分（手牌快空了）
    NEAR_EMPTY_BONUS = 500
    # 每張黑桃（suit == 3）加分
    SPADE_BONUS = 5

    # -------------------------------------------------------
    # 評分函數
    # -------------------------------------------------------

    @staticmethod
    def score_play(
        cards: List[Card],
        hand: Hand,
        is_first: bool = False,
    ) -> float:
        """
        計算某組出牌的分數。

        分數越高，代表這組出牌對 AI 越有利。

        步驟：
          1. 用 HandClassifier.classify(cards) 取得牌型資訊
             - 若無法分類（回傳 None）→ 回傳 float("-inf")（極差分）
          2. 基礎分 = 牌型值 × 100 + 代表點數 × 10
          3. 剩餘加分：
             - 出完後剩 0 或 1 張 → +EMPTY_HAND_BONUS (10000)
             - 出完後剩 2 或 3 張 → +NEAR_EMPTY_BONUS (500)
          4. 黑桃加分：每張 ♠（suit == 3）→ +SPADE_BONUS (5)
          5. 回傳總分

        :param cards:    要出的牌（出牌組合）
        :param hand:     玩家目前持有的手牌（用來計算剩餘張數）
        :param is_first: 是否為第一回合（保留參數，未來可使用）
        :return: 出牌分數（float）
        """
        # ── 步驟 1：分類 ──────────────────────────────────────
        classified = HandClassifier.classify(cards)
        if classified is None:
            # 無效出牌，給予極低分數，讓 AI 絕對不會選它
            return float("-inf")

        card_type, rank_key, suit_key = classified

        # ── 步驟 2：基礎分 ────────────────────────────────────
        # 牌型值：CardType 的整數值（SINGLE=1, PAIR=2, ..., STRAIGHT_FLUSH=8）
        # 代表點數（rank_key）越大，代表這組牌的大小越高
        type_value = int(card_type)          # 例：PAIR → 2
        score: float = type_value * 100 + rank_key * 10

        # ── 步驟 3：出完後剩餘張數加分 ──────────────────────
        remaining = len(hand) - len(cards)

        if remaining <= 1:
            # 剩 0 張（出完）或剩 1 張，最優先加大分
            score += AIStrategy.EMPTY_HAND_BONUS
        elif remaining <= 3:
            # 剩 2 或 3 張，手牌快空了，輕微加分
            score += AIStrategy.NEAR_EMPTY_BONUS

        # ── 步驟 4：黑桃加分 ─────────────────────────────────
        # suit == 3 代表 ♠（黑桃），比同點數其他花色更強
        for card in cards:
            if card.suit == 3:
                score += AIStrategy.SPADE_BONUS

        return score

    # -------------------------------------------------------
    # 選擇最佳出牌
    # -------------------------------------------------------

    @staticmethod
    def select_best(
        valid_plays: List[List[Card]],
        hand: Hand,
        is_first: bool = False,
    ) -> Optional[List[Card]]:
        """
        從所有合法出牌中，挑出分數最高的一手。

        規則：
          (1) valid_plays 為空 → 回傳 None（表示本回合 pass）
          (2) is_first == True：
              - 優先從「包含 ♣3（Card(3,0)）」的出牌中挑最高分
              - 若沒有含 ♣3 的出牌，退回一般最高分邏輯
          (3) 一般情況：
              - 計算每組出牌的 score_play 分數
              - 回傳分數最高的出牌組合

        :param valid_plays: 所有合法出牌的清單（每個元素是 List[Card]）
        :param hand:        玩家目前的手牌
        :param is_first:    是否為第一回合
        :return: 最佳出牌組合，或 None（無法出牌）
        """
        # ── 情況 (1)：無合法出牌 ──────────────────────────────
        if not valid_plays:
            return None

        three_clubs = Card(3, 0)  # ♣3，第一回合的必出牌

        # ── 情況 (2)：第一回合，優先選含 ♣3 的出牌 ─────────
        if is_first:
            # 篩選出包含 ♣3 的出牌
            plays_with_3c = [
                play for play in valid_plays if three_clubs in play
            ]
            if plays_with_3c:
                # 從含 ♣3 的出牌中選分數最高的
                return max(
                    plays_with_3c,
                    key=lambda play: AIStrategy.score_play(play, hand, is_first),
                )
            # 若沒有含 ♣3 的出牌，退回一般邏輯

        # ── 情況 (3)：一般情況，選分數最高的出牌 ────────────
        return max(
            valid_plays,
            key=lambda play: AIStrategy.score_play(play, hand, is_first),
        )
