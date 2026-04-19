from __future__ import annotations

from collections import Counter
from enum import IntEnum
from typing import Optional

from .models import Card


class CardType(IntEnum):
    SINGLE = 1
    PAIR = 2
    TRIPLE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8


class HandClassifier:
    @staticmethod
    def _is_straight(ranks: list[int]) -> bool:
        if len(ranks) != 5:
            return False
        unique = sorted(set(ranks))
        if len(unique) != 5:
            return False

        if unique == [3, 4, 5, 14, 15]:
            return True

        return unique[-1] - unique[0] == 4 and all(
            unique[i] + 1 == unique[i + 1] for i in range(4)
        )

    @staticmethod
    def _is_flush(suits: list[int]) -> bool:
        return len(suits) == 5 and len(set(suits)) == 1

    @staticmethod
    def _straight_high(ranks: list[int]) -> int:
        unique = sorted(set(ranks))
        if unique == [3, 4, 5, 14, 15]:
            return 5
        return max(unique)

    @staticmethod
    def classify(cards: list[Card]) -> Optional[tuple[CardType, int, int]]:
        n = len(cards)
        if n == 0:
            return None

        ranks = [c.rank for c in cards]
        suits = [c.suit for c in cards]
        rank_counts = Counter(ranks)

        if n == 1:
            card = cards[0]
            return (CardType.SINGLE, card.rank, card.suit)

        if n == 2:
            if len(rank_counts) == 1:
                return (CardType.PAIR, cards[0].rank, 0)
            return None

        if n == 3:
            if len(rank_counts) == 1:
                return (CardType.TRIPLE, cards[0].rank, 0)
            return None

        if n != 5:
            return None

        is_straight = HandClassifier._is_straight(ranks)
        is_flush = HandClassifier._is_flush(suits)
        sorted_cards = sorted(cards)

        if is_straight and is_flush:
            return (CardType.STRAIGHT_FLUSH, HandClassifier._straight_high(ranks), 0)

        count_values = sorted(rank_counts.values(), reverse=True)
        if count_values == [4, 1]:
            four_rank = max(rank for rank, count in rank_counts.items() if count == 4)
            return (CardType.FOUR_OF_A_KIND, four_rank, 0)

        if count_values == [3, 2]:
            triple_rank = max(rank for rank, count in rank_counts.items() if count == 3)
            return (CardType.FULL_HOUSE, triple_rank, 0)

        if is_flush:
            top = sorted_cards[-1]
            return (CardType.FLUSH, top.rank, top.suit)

        if is_straight:
            return (CardType.STRAIGHT, HandClassifier._straight_high(ranks), 0)

        return None

    @staticmethod
    def compare(play1: list[Card], play2: list[Card]) -> int:
        c1 = HandClassifier.classify(play1)
        c2 = HandClassifier.classify(play2)
        if c1 is None or c2 is None:
            raise ValueError("cannot compare invalid plays")

        if c1[0] != c2[0]:
            return 1 if c1[0] > c2[0] else -1

        if c1[1] != c2[1]:
            return 1 if c1[1] > c2[1] else -1

        if c1[2] != c2[2]:
            return 1 if c1[2] > c2[2] else -1

        return 0

    @staticmethod
    def can_play(last_play: Optional[list[Card]], cards: list[Card]) -> bool:
        if HandClassifier.classify(cards) is None:
            return False

        if last_play is None:
            return any(c.rank == 3 and c.suit == 0 for c in cards)

        if HandClassifier.classify(last_play) is None:
            return False

        if len(last_play) != len(cards):
            return False

        new_type = HandClassifier.classify(cards)
        last_type = HandClassifier.classify(last_play)
        if new_type is None or last_type is None:
            return False

        if len(cards) in (1, 2, 3) and new_type[0] != last_type[0]:
            return False

        return HandClassifier.compare(cards, last_play) > 0
