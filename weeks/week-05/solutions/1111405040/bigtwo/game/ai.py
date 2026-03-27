"""
AI 出牌策略。
"""

from __future__ import annotations

from math import inf

from game.classifier import CardType, HandClassifier
from game.models import Card, Hand


class AIStrategy:
    """簡單但可預測的 AI 評分策略。"""

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

    @classmethod
    def score_play(cls, cards: list[Card], hand: Hand, is_first_turn: bool = False) -> float:
        info = HandClassifier.classify(cards)
        if info is None:
            return -inf

        card_type, rank, suit = info
        score = cls.TYPE_SCORES[card_type] * 100 + rank * 10 + suit
        remaining = len(hand) - len(cards)

        if remaining == 0:
            score += cls.EMPTY_HAND_BONUS
        elif remaining <= 3:
            score += cls.NEAR_EMPTY_BONUS

        score += sum(cls.SPADE_BONUS for card in cards if card.suit == 3)

        if is_first_turn and Card(3, 0) in cards:
            score += 50

        return score

    @classmethod
    def select_best(
        cls,
        valid_plays: list[list[Card]],
        hand: Hand,
        is_first_turn: bool = False,
    ) -> list[Card] | None:
        if not valid_plays:
            return None

        if is_first_turn:
            first_turn_plays = [play for play in valid_plays if Card(3, 0) in play]
            if first_turn_plays:
                return min(
                    first_turn_plays,
                    key=lambda play: (
                        len(play),
                        cls.score_play(play, hand, is_first_turn=False),
                    ),
                )

        return max(valid_plays, key=lambda play: cls.score_play(play, hand))
