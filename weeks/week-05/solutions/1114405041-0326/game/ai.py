"""Phase 4：AI 貪心策略。"""

from __future__ import annotations

from game.classifier import CardType, HandClassifier
from game.models import Card, Hand


class AIStrategy:
    """簡單可解釋的貪心 AI。"""

    TYPE_SCORES = {
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
    def score_play(cards: list[Card], hand: Hand, is_first: bool = False) -> float:
        """計算出牌分數。

        公式：牌型*100 + 點數*10 + 額外加分
        """
        classify = HandClassifier.classify(cards)
        if classify is None:
            return float("-inf")

        card_type, rank, _ = classify
        score = AIStrategy.TYPE_SCORES[card_type] * 100 + rank * 10

        # 模擬出牌後剩餘手牌張數。
        remain = len(hand) - len(cards)
        if remain == 1:
            score += AIStrategy.EMPTY_HAND_BONUS
        elif remain <= 3:
            score += AIStrategy.NEAR_EMPTY_BONUS

        # 偏好出黑桃，有助於同點數比較。
        score += sum(1 for c in cards if c.suit == 3) * AIStrategy.SPADE_BONUS

        # 第一手固定是 3♣，不需要額外加分。
        if is_first and not any(c.rank == 3 and c.suit == 0 for c in cards):
            return float("-inf")

        return float(score)

    @staticmethod
    def select_best(valid_plays: list[list[Card]], hand: Hand, is_first: bool = False) -> list[Card] | None:
        if not valid_plays:
            return None

        if is_first:
            for play in valid_plays:
                if len(play) == 1 and play[0].rank == 3 and play[0].suit == 0:
                    return play
            return None

        # 取分數最高，若同分則取排序鍵較大的（較高牌）。
        return max(
            valid_plays,
            key=lambda p: (
                AIStrategy.score_play(p, hand, is_first=False),
                sorted((c.rank, c.suit) for c in p),
            ),
        )
