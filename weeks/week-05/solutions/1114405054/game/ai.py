"""Phase 4: AI 貪婪出牌策略。"""

from __future__ import annotations

from .classifier import CardType, HandClassifier
from .models import Card, Hand


class AIStrategy:
    """依照評分函數選出目前最佳出牌。"""

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
        info = HandClassifier.classify(cards)
        if info is None:
            return float("-inf")

        card_type, rank, _ = info
        score = AIStrategy.TYPE_SCORES[card_type] * 100 + rank * 10

        remaining = max(len(hand) - len(cards), 0)
        if remaining == 1:
            score += AIStrategy.EMPTY_HAND_BONUS
        elif remaining <= 3:
            score += AIStrategy.NEAR_EMPTY_BONUS

        score += sum(AIStrategy.SPADE_BONUS for card in cards if card.suit == 3)

        if is_first and Card(3, 0) in cards:
            score += 1

        return float(score)

    @staticmethod
    def select_best(valid_plays: list[list[Card]], hand: Hand, is_first: bool = False) -> list[Card] | None:
        if not valid_plays:
            return None

        if is_first:
            three_clubs = Card(3, 0)
            for play in valid_plays:
                if play == [three_clubs]:
                    return play
            for play in valid_plays:
                if three_clubs in play:
                    return play
            return None

        return max(
            valid_plays,
            key=lambda play: (
                AIStrategy.score_play(play, hand, is_first=False),
                len(play),
            ),
        )
