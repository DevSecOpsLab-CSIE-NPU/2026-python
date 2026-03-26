"""Phase 4: AI 出牌策略（貪心法）。"""

from __future__ import annotations

from typing import Dict, List, Optional

from .classifier import CardType, HandClassifier
from .models import Card, Hand


class AIStrategy:
    """根據目前手牌與合法出牌，選擇分數最高的出法。"""

    TYPE_SCORES: Dict[CardType, int] = {
        CardType.SINGLE: 1,
        CardType.PAIR: 2,
        CardType.TRIPLE: 3,
        CardType.STRAIGHT: 4,
        CardType.FLUSH: 5,
        CardType.FULL_HOUSE: 6,
        CardType.FOUR_OF_A_KIND: 7,
        CardType.STRAIGHT_FLUSH: 8,
    }

    EMPTY_HAND_BONUS = 10000
    NEAR_EMPTY_BONUS = 500
    SPADE_BONUS = 5

    @staticmethod
    def score_play(cards: List[Card], hand: Hand, is_first: bool = False) -> float:
        """計算出牌分數，分數越高越優先。"""
        cls = HandClassifier.classify(cards)
        if cls is None:
            return float("-inf")

        card_type, rank_score, _ = cls
        score = AIStrategy.TYPE_SCORES[card_type] * 100 + rank_score * 10

        remaining = len(hand) - len(cards)
        # 優先把手牌清空或逼近清空
        if remaining == 1:
            score += AIStrategy.EMPTY_HAND_BONUS
        elif remaining <= 3:
            score += AIStrategy.NEAR_EMPTY_BONUS

        # 黑桃有額外加權，鼓勵在同分情況下偏向高花色
        spade_count = sum(1 for c in cards if c.suit == 3)
        score += spade_count * AIStrategy.SPADE_BONUS

        # 第一回合仍使用同一評分模型，實際限制由 select_best 控制
        _ = is_first
        return float(score)

    @staticmethod
    def select_best(valid_plays: List[List[Card]], hand: Hand, is_first: bool = False) -> Optional[List[Card]]:
        """從合法出牌中挑選最佳解；若無可出則回傳 None。"""
        if not valid_plays:
            return None

        # 第一回合只能出 3♣，若合法列表含此選項直接回傳
        if is_first:
            for play in valid_plays:
                if any(c.rank == 3 and c.suit == 0 for c in play):
                    return play

        best_play: Optional[List[Card]] = None
        best_score = float("-inf")

        for play in valid_plays:
            score = AIStrategy.score_play(play, hand, is_first=is_first)
            if score > best_score:
                best_score = score
                best_play = play

        return best_play
