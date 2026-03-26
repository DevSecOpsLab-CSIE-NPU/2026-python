from __future__ import annotations
from collections import Counter
from enum import IntEnum
from typing import List, Optional, Tuple
from p1_models import Card


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
    def _straight_high_rank(ranks: List[int]) -> Optional[int]:
        if len(ranks) != 5:
            return None

        sorted_ranks = sorted(ranks)

        if len(set(sorted_ranks)) != 5:
            return None

        # A-2-3-4-5
        if sorted_ranks == [3, 4, 5, 14, 15]:
            return 5

        for i in range(4):
            if sorted_ranks[i + 1] - sorted_ranks[i] != 1:
                return None

        return sorted_ranks[-1]

    @staticmethod
    def _is_straight(ranks: List[int]) -> bool:
        return HandClassifier._straight_high_rank(ranks) is not None

    @staticmethod
    def _is_flush(suits: List[int]) -> bool:
        return len(suits) == 5 and len(set(suits)) == 1

    @staticmethod
    def classify(cards: List[Card]) -> Optional[Tuple[CardType, int, int]]:
        n = len(cards)
        if n == 0:
            return None

        ranks = [card.rank for card in cards]
        suits = [card.suit for card in cards]

        # 單張
        if n == 1:
            return (CardType.SINGLE, ranks[0], suits[0])

        # 對子
        if n == 2:
            if ranks[0] == ranks[1]:
                return (CardType.PAIR, ranks[0], max(suits))
            return None

        # 三條
        if n == 3:
            if ranks[0] == ranks[1] == ranks[2]:
                return (CardType.TRIPLE, ranks[0], 0)
            return None

        # 五張牌
        if n == 5:
            rank_counter = Counter(ranks)
            count_values = sorted(rank_counter.values(), reverse=True)

            is_flush = HandClassifier._is_flush(suits)
            straight_high = HandClassifier._straight_high_rank(ranks)
            is_straight = straight_high is not None

            # 同花順
            if is_flush and is_straight:
                return (CardType.STRAIGHT_FLUSH, straight_high, suits[0])

            # 四條
            if count_values == [4, 1]:
                four_rank = next(rank for rank, cnt in rank_counter.items() if cnt == 4)
                return (CardType.FOUR_OF_A_KIND, four_rank, 0)

            # 葫蘆
            if count_values == [3, 2]:
                triple_rank = next(rank for rank, cnt in rank_counter.items() if cnt == 3)
                return (CardType.FULL_HOUSE, triple_rank, 0)

            # 同花
            if is_flush:
                return (CardType.FLUSH, max(ranks), suits[0])

            # 順子
            if is_straight:
                return (CardType.STRAIGHT, straight_high, 0)

            return None

        return None

    @staticmethod
    def compare(play1: List[Card], play2: List[Card]) -> int:
        c1 = HandClassifier.classify(play1)
        c2 = HandClassifier.classify(play2)

        if c1 is None and c2 is None:
            return 0
        if c1 is not None and c2 is None:
            return 1
        if c1 is None and c2 is not None:
            return -1

        assert c1 is not None and c2 is not None

        t1, r1, s1 = c1
        t2, r2, s2 = c2

        if t1 != t2:
            return 1 if t1 > t2 else -1

        if r1 != r2:
            return 1 if r1 > r2 else -1

        if t1 == CardType.SINGLE:
            if s1 == s2:
                return 0
            return 1 if s1 > s2 else -1

        if t1 == CardType.PAIR:
            max_suit_1 = max(card.suit for card in play1)
            max_suit_2 = max(card.suit for card in play2)
            if max_suit_1 == max_suit_2:
                return 0
            return 1 if max_suit_1 > max_suit_2 else -1

        if t1 == CardType.FLUSH:
            if s1 == s2:
                return 0
            return 1 if s1 > s2 else -1

        if t1 == CardType.STRAIGHT_FLUSH:
            if s1 == s2:
                return 0
            return 1 if s1 > s2 else -1

        return 0

    @staticmethod
    def can_play(last_play: Optional[List[Card]], cards: List[Card]) -> bool:
        current = HandClassifier.classify(cards)
        if current is None:
            return False

        if last_play is None:
            return (
                len(cards) == 1
                and cards[0].rank == 3
                and cards[0].suit == 0
            )

        previous = HandClassifier.classify(last_play)
        if previous is None:
            return False

        if len(cards) != len(last_play):
            return False

        if current[0] != previous[0]:
            return False

        return HandClassifier.compare(cards, last_play) == 1