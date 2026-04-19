from __future__ import annotations

from .classifier import HandClassifier
from .models import Card, Hand


class AIStrategy:
    EMPTY_HAND_BONUS = 10000
    NEAR_EMPTY_BONUS = 500
    SPADE_BONUS = 5

    @staticmethod
    def score_play(cards: list[Card], hand: Hand, is_first: bool = False) -> float:
        classified = HandClassifier.classify(cards)
        if classified is None:
            return float("-inf")

        card_type, rank, _ = classified
        remaining = len(hand) - len(cards)

        score = float(card_type) * 100 + rank * 10
        if remaining == 0:
            score += AIStrategy.EMPTY_HAND_BONUS
        elif remaining <= 3:
            score += AIStrategy.NEAR_EMPTY_BONUS

        score += sum(AIStrategy.SPADE_BONUS for c in cards if c.suit == 3)

        if is_first and not any(c.rank == 3 and c.suit == 0 for c in cards):
            return float("-inf")

        return score

    @staticmethod
    def select_best(
        valid_plays: list[list[Card]], hand: Hand, is_first: bool = False
    ) -> list[Card] | None:
        if not valid_plays:
            return None

        best_play: list[Card] | None = None
        best_score = float("-inf")

        for play in valid_plays:
            score = AIStrategy.score_play(play, hand, is_first=is_first)
            if score > best_score:
                best_score = score
                best_play = play

        return best_play
