from __future__ import annotations

from typing import List, Optional

from .cards import Card, Hand
from .classifier import CardType, HandClassifier
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

    @staticmethod
    def _score_play(cards: List[Card], hand: Hand, is_first: bool = False) -> float:
        classification = HandClassifier.classify(cards)
        if classification is None:
            return float("-inf")

        card_type, high_rank, _ = classification
        score = AIStrategy.TYPE_SCORES[card_type] * 100 + high_rank * 10

        hand_size = len(hand.cards)
        remaining = hand_size - len(cards)
        if hand_size == 1:
            score += AIStrategy.EMPTY_HAND_BONUS
        elif hand_size <= 3:
            score += AIStrategy.NEAR_EMPTY_BONUS

        spade_count = sum(1 for c in cards if c.suit == 3)
        score += spade_count * AIStrategy.SPADE_BONUS

        return float(score)

    @staticmethod
    def _select_best_play(valid_plays: List[List[Card]], hand: Hand, is_first: bool = False) -> Optional[List[Card]]:
        if not valid_plays:
            return None

        if is_first:
            first_turn_plays = [
                play for play in valid_plays if any(c.rank == 3 and c.suit == 0 for c in play)
            ]
            if first_turn_plays:
                valid_plays = first_turn_plays

        return max(valid_plays, key=lambda play: AIStrategy._score_play(play, hand, is_first))

    @staticmethod
    def select_play(hand: Hand, last_play: Optional[List[Card]], is_first_turn: bool = False) -> Optional[List[Card]]:
        if len(hand.cards) == 1:
            return [hand.cards[0]]

        valid_plays = HandFinder.get_all_valid_plays(hand, last_play)

        if is_first_turn:
            valid_plays = [
                play for play in valid_plays if any(c.rank == 3 and c.suit == 0 for c in play)
            ]

        return AIStrategy._select_best_play(valid_plays, hand, is_first=is_first_turn)
