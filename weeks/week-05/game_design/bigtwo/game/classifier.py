"""Big Two Card Game - Hand Classification"""

from typing import List, Optional, Tuple
from enum import IntEnum
from collections import Counter


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
    def _is_straight(ranks: List[int]) -> bool:
        if len(ranks) != 5:
            return False
        unique_ranks = sorted(set(ranks))
        if len(unique_ranks) != 5:
            return False

        if unique_ranks == [3, 4, 5, 6, 14]:
            return True

        for i in range(1, 5):
            if unique_ranks[i] - unique_ranks[i - 1] != 1:
                return False
        return True

    @staticmethod
    def _is_flush(suits: List[int]) -> bool:
        return len(set(suits)) == 1

    @classmethod
    def classify(cls, cards: List) -> Optional[Tuple[CardType, int, int]]:
        if not cards:
            return None

        n = len(cards)
        ranks = [c.rank if hasattr(c, "rank") else c[0] for c in cards]
        suits = [c.suit if hasattr(c, "suit") else c[1] for c in cards]

        if n == 1:
            return (CardType.SINGLE, ranks[0], suits[0])

        if n == 2:
            if ranks[0] == ranks[1]:
                return (CardType.PAIR, ranks[0], max(suits))
            return None

        if n == 3:
            if ranks[0] == ranks[1] == ranks[2]:
                return (CardType.TRIPLE, ranks[0], max(suits))
            return None

        if n == 5:
            rank_counts = Counter(ranks)
            count_values = sorted(rank_counts.values(), reverse=True)

            is_flush = cls._is_flush(suits)
            is_straight = cls._is_straight(ranks)

            if is_flush and is_straight:
                return (CardType.STRAIGHT_FLUSH, max(ranks), max(suits))

            if count_values == [4, 1]:
                main_rank = [r for r, c in rank_counts.items() if c == 4][0]
                return (CardType.FOUR_OF_A_KIND, main_rank, max(suits))

            if count_values == [3, 2]:
                main_rank = [r for r, c in rank_counts.items() if c == 3][0]
                return (CardType.FULL_HOUSE, main_rank, max(suits))

            if is_flush:
                return (CardType.FLUSH, max(ranks), max(suits))

            if is_straight:
                return (CardType.STRAIGHT, max(ranks), max(suits))

        return None

    @classmethod
    def get_type_name(cls, card_type: CardType) -> str:
        names = {
            CardType.SINGLE: "單張",
            CardType.PAIR: "對子",
            CardType.TRIPLE: "三條",
            CardType.STRAIGHT: "順子",
            CardType.FLUSH: "同花",
            CardType.FULL_HOUSE: "葫蘆",
            CardType.FOUR_OF_A_KIND: "四條",
            CardType.STRAIGHT_FLUSH: "同花順",
        }
        return names.get(card_type, "未知")

    @classmethod
    def compare(cls, play1: List, play2: List) -> int:
        type1 = cls.classify(play1)
        type2 = cls.classify(play2)

        if type1 is None or type2 is None:
            return 0

        if type1[0] != type2[0]:
            return 1 if type1[0] > type2[0] else -1

        if type1[1] != type2[1]:
            return 1 if type1[1] > type2[1] else -1

        if type1[2] != type2[2]:
            return 1 if type1[2] > type2[2] else -1

        return 0

    @classmethod
    def can_play(cls, last_play: Optional[List], cards: List) -> bool:
        if last_play is None:
            return len(cards) == 1 and cards[0].rank == 3 and cards[0].suit == 0

        classification = cls.classify(cards)
        if classification is None:
            return False

        last_classification = cls.classify(last_play)
        if last_classification is None:
            return False

        if len(cards) != len(last_play):
            return False

        return cls.compare(cards, last_play) > 0
