from typing import List, Optional

from game.models import Card, Hand
from game.classifier import HandClassifier, CardType


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
    def score_play(cards: List[Card], hand: Hand, is_first: bool = False) -> float:
        result = HandClassifier.classify(cards)
        if result is None:
            return -1

        card_type, rank, _ = result
        type_score = AIStrategy.TYPE_SCORES.get(card_type, 0)
        base = type_score * 100 + rank * 10

        # Remaining cards after play
        remaining = len(hand) - len(cards)
        if remaining == 0:
            base += AIStrategy.EMPTY_HAND_BONUS
        elif remaining <= 3:
            base += AIStrategy.NEAR_EMPTY_BONUS

        # Spade bonus
        spade_count = sum(1 for c in cards if c.suit == 3)
        base += spade_count * AIStrategy.SPADE_BONUS

        return base

    @staticmethod
    def select_best(valid_plays: List[List[Card]], hand: Hand,
                    is_first: bool = False) -> Optional[List[Card]]:
        if not valid_plays:
            return None

        if is_first:
            # Must play 3♣
            for play in valid_plays:
                if any(c.rank == 3 and c.suit == 0 for c in play):
                    return play
            return None

        best = max(valid_plays, key=lambda p: AIStrategy.score_play(p, hand))
        return best
