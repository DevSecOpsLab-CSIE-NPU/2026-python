from __future__ import annotations

from typing import Optional

from .classifier import CardType, HandClassifier
from .models import Card, Hand


class AIStrategy:
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
        classified = HandClassifier.classify(cards)
        if classified is None:
            return float("-inf")

        card_type, rank, suit = classified
        base = AIStrategy.TYPE_SCORES[card_type] * 100 + rank * 10 + suit

        remaining = len(hand) - len(cards)
        if remaining == 0:
            base += AIStrategy.EMPTY_HAND_BONUS
        elif remaining <= 3:
            base += AIStrategy.NEAR_EMPTY_BONUS

        base += sum(AIStrategy.SPADE_BONUS for c in cards if c.suit == 3)

        if is_first and not any(c.rank == 3 and c.suit == 0 for c in cards):
            return float("-inf")

        return float(base)

    @staticmethod
    def select_best(valid_plays: list[list[Card]], hand: Hand, is_first: bool = False) -> Optional[list[Card]]:
        if not valid_plays:
            return None

        if is_first:
            for play in valid_plays:
                if any(c.rank == 3 and c.suit == 0 for c in play):
                    return play
            return None

        return max(valid_plays, key=lambda p: AIStrategy.score_play(p, hand, is_first=False))
