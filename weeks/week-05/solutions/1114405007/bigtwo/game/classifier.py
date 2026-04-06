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
    def _is_flush(suits: list[int]) -> bool:
        return len(set(suits)) == 1

    @staticmethod
    def _is_straight(ranks: list[int]) -> tuple[bool, int]:
        uniq = sorted(set(ranks))
        if len(uniq) != 5:
            return False, 0

        # Special case: A-2-3-4-5
        if uniq == [3, 4, 5, 14, 15]:
            return True, 5

        for i in range(4):
            if uniq[i + 1] - uniq[i] != 1:
                return False, 0
        return True, uniq[-1]

    @staticmethod
    def classify(cards: list[Card]) -> Optional[tuple[CardType, int, int]]:
        if not cards:
            return None

        n = len(cards)
        ranks = [c.rank for c in cards]
        suits = [c.suit for c in cards]
        rank_counter = Counter(ranks)

        if n == 1:
            c = cards[0]
            return CardType.SINGLE, c.rank, c.suit

        if n == 2:
            if len(rank_counter) == 1:
                return CardType.PAIR, cards[0].rank, 0
            return None

        if n == 3:
            if len(rank_counter) == 1:
                return CardType.TRIPLE, cards[0].rank, 0
            return None

        if n != 5:
            return None

        is_flush = HandClassifier._is_flush(suits)
        is_straight, straight_high = HandClassifier._is_straight(ranks)

        if is_flush and is_straight:
            return CardType.STRAIGHT_FLUSH, straight_high, suits[0]

        if 4 in rank_counter.values():
            four_rank = max(r for r, count in rank_counter.items() if count == 4)
            return CardType.FOUR_OF_A_KIND, four_rank, 0

        if sorted(rank_counter.values()) == [2, 3]:
            triple_rank = max(r for r, count in rank_counter.items() if count == 3)
            return CardType.FULL_HOUSE, triple_rank, 0

        if is_flush:
            return CardType.FLUSH, max(ranks), suits[0]

        if is_straight:
            return CardType.STRAIGHT, straight_high, 0

        return None

    @staticmethod
    def compare(play1: list[Card], play2: list[Card]) -> int:
        c1 = HandClassifier.classify(play1)
        c2 = HandClassifier.classify(play2)
        if c1 is None and c2 is None:
            return 0
        if c1 is None:
            return -1
        if c2 is None:
            return 1

        t1, r1, s1 = c1
        t2, r2, s2 = c2

        if t1 != t2:
            return 1 if t1 > t2 else -1
        if r1 != r2:
            return 1 if r1 > r2 else -1
        if s1 != s2:
            return 1 if s1 > s2 else -1
        return 0

    @staticmethod
    def can_play(last_play: Optional[list[Card]], cards: list[Card]) -> bool:
        current_type = HandClassifier.classify(cards)
        if current_type is None:
            return False

        if last_play is None:
            return any(c.rank == 3 and c.suit == 0 for c in cards)

        last_type = HandClassifier.classify(last_play)
        if last_type is None:
            return True

        if len(last_play) != len(cards):
            return False

        # In Big Two, 5-card plays can beat each other by hand type hierarchy.
        if len(cards) == 5:
            return HandClassifier.compare(cards, last_play) > 0

        if current_type[0] != last_type[0]:
            return False

        return HandClassifier.compare(cards, last_play) > 0
