"""
牌型辨識與比較。
"""

from __future__ import annotations

from collections import Counter
from enum import IntEnum

from game.models import Card


class CardType(IntEnum):
    """牌型強度。"""

    SINGLE = 1
    PAIR = 2
    TRIPLE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8


class HandClassifier:
    """Big Two 牌型工具。"""

    @staticmethod
    def _is_straight(ranks: list[int]) -> tuple[bool, int]:
        ordered = sorted(ranks)
        if len(set(ordered)) != 5:
            return False, 0

        if ordered == [3, 4, 5, 14, 15]:
            return True, 5

        for index in range(4):
            if ordered[index + 1] - ordered[index] != 1:
                return False, 0
        return True, ordered[-1]

    @staticmethod
    def _highest_card_of_rank(cards: list[Card], rank: int) -> Card:
        return max((card for card in cards if card.rank == rank), key=lambda card: card.suit)

    @classmethod
    def classify(cls, cards: list[Card]) -> tuple[CardType, int, int] | None:
        if not cards:
            return None

        cards = list(cards)
        size = len(cards)
        ranks = [card.rank for card in cards]
        suits = [card.suit for card in cards]
        counts = Counter(ranks)

        if size == 1:
            card = cards[0]
            return CardType.SINGLE, card.rank, card.suit

        if size == 2 and len(counts) == 1:
            rank = ranks[0]
            return CardType.PAIR, rank, max(suits)

        if size == 3 and len(counts) == 1:
            rank = ranks[0]
            return CardType.TRIPLE, rank, max(suits)

        if size != 5:
            return None

        is_flush = len(set(suits)) == 1
        is_straight, straight_high = cls._is_straight(ranks)

        if is_straight and is_flush:
            high_card = cls._highest_card_of_rank(cards, straight_high)
            return CardType.STRAIGHT_FLUSH, straight_high, high_card.suit

        if sorted(counts.values(), reverse=True) == [4, 1]:
            main_rank = next(rank for rank, count in counts.items() if count == 4)
            high_card = cls._highest_card_of_rank(cards, main_rank)
            return CardType.FOUR_OF_A_KIND, main_rank, high_card.suit

        if sorted(counts.values(), reverse=True) == [3, 2]:
            main_rank = next(rank for rank, count in counts.items() if count == 3)
            high_card = cls._highest_card_of_rank(cards, main_rank)
            return CardType.FULL_HOUSE, main_rank, high_card.suit

        if is_flush:
            high_card = max(cards, key=lambda card: card.to_sort_key())
            return CardType.FLUSH, high_card.rank, high_card.suit

        if is_straight:
            high_card = cls._highest_card_of_rank(cards, straight_high)
            return CardType.STRAIGHT, straight_high, high_card.suit

        return None

    @classmethod
    def compare(cls, play1: list[Card], play2: list[Card]) -> int:
        info1 = cls.classify(play1)
        info2 = cls.classify(play2)
        if info1 is None or info2 is None:
            return 0

        if info1[0] != info2[0]:
            return 1 if info1[0] > info2[0] else -1

        if info1[1] != info2[1]:
            return 1 if info1[1] > info2[1] else -1

        if info1[2] != info2[2]:
            return 1 if info1[2] > info2[2] else -1

        return 0

    @staticmethod
    def contains_3_clubs(cards: list[Card]) -> bool:
        return Card(3, 0) in cards

    @classmethod
    def can_play(
        cls,
        last_play: list[Card] | None,
        cards: list[Card],
        is_first_turn: bool = False,
    ) -> bool:
        current_info = cls.classify(cards)
        if current_info is None:
            return False

        if is_first_turn and not cls.contains_3_clubs(cards):
            return False

        if last_play is None:
            return True

        last_info = cls.classify(last_play)
        if last_info is None:
            return True

        if len(cards) != len(last_play):
            return False

        if len(cards) != 5 and current_info[0] != last_info[0]:
            return False

        return cls.compare(cards, last_play) > 0
