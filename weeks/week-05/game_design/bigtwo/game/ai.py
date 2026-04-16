"""Big Two Card Game - AI Strategy"""

from typing import List, Optional
from .models import Card, Hand
from .classifier import CardType
from .finder import HandFinder


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

    @classmethod
    def score_play(cls, cards: List[Card], hand: Hand, is_first: bool = False) -> float:
        from .classifier import HandClassifier

        classification = HandClassifier.classify(cards)
        if classification is None:
            return -1

        card_type, rank, suit = classification
        score = cls.TYPE_SCORES[card_type] * 100 + rank * 10

        remaining = len(hand) - len(cards)
        if remaining == 0:
            score += cls.EMPTY_HAND_BONUS
        elif remaining <= 3:
            score += cls.NEAR_EMPTY_BONUS

        for card in cards:
            if card.suit == 3:
                score += cls.SPADE_BONUS

        return score

    @classmethod
    def select_best(
        cls, valid_plays: List[List[Card]], hand: Hand, is_first: bool = False
    ) -> Optional[List[Card]]:
        if not valid_plays:
            return None

        if is_first:
            for play in valid_plays:
                if len(play) == 1 and play[0].rank == 3 and play[0].suit == 0:
                    return play

        best_play = None
        best_score = -1

        for play in valid_plays:
            score = cls.score_play(play, hand, is_first)
            if score > best_score:
                best_score = score
                best_play = play

        return best_play
