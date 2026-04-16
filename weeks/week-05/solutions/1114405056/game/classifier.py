from enum import Enum
from typing import List, Optional, Tuple
from collections import Counter


class CardType(Enum):
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
        s = sorted(ranks)
        if len(set(s)) == 5 and s[-1] - s[0] == 4:
            return True
        # A-2-3-4-5: ranks [3,4,5,14,15]
        if sorted(s) == [3, 4, 5, 14, 15]:
            return True
        return False

    @staticmethod
    def _is_flush(suits: List[int]) -> bool:
        return len(set(suits)) == 1

    @staticmethod
    def _straight_top(cards):
        ranks = sorted(c.rank for c in cards)
        if ranks == [3, 4, 5, 14, 15]:
            # A-2-3-4-5: top card is 5
            fives = [c for c in cards if c.rank == 5]
            return max(fives, key=lambda c: c.suit)
        return max(cards, key=lambda c: (c.rank, c.suit))

    @staticmethod
    def classify(cards) -> Optional[Tuple]:
        n = len(cards)
        if n == 0:
            return None
        if n == 1:
            c = cards[0]
            return (CardType.SINGLE, c.rank, c.suit)
        if n == 2:
            if cards[0].rank == cards[1].rank:
                max_suit = max(c.suit for c in cards)
                return (CardType.PAIR, cards[0].rank, max_suit)
            return None
        if n == 3:
            ranks = [c.rank for c in cards]
            if len(set(ranks)) == 1:
                max_suit = max(c.suit for c in cards)
                return (CardType.TRIPLE, ranks[0], max_suit)
            return None
        if n == 5:
            ranks = [c.rank for c in cards]
            suits = [c.suit for c in cards]
            rank_counts = Counter(ranks)
            is_s = HandClassifier._is_straight(ranks)
            is_f = HandClassifier._is_flush(suits)
            top = HandClassifier._straight_top(cards)
            counts = sorted(rank_counts.values(), reverse=True)

            if is_s and is_f:
                return (CardType.STRAIGHT_FLUSH, top.rank, top.suit)
            if counts[0] == 4:
                four_rank = max(r for r, cnt in rank_counts.items() if cnt == 4)
                return (CardType.FOUR_OF_A_KIND, four_rank, 0)
            if counts[0] == 3 and counts[1] == 2:
                three_rank = max(r for r, cnt in rank_counts.items() if cnt == 3)
                return (CardType.FULL_HOUSE, three_rank, 0)
            if is_f:
                top_card = max(cards, key=lambda c: (c.rank, c.suit))
                return (CardType.FLUSH, top_card.rank, suits[0])
            if is_s:
                return (CardType.STRAIGHT, top.rank, top.suit)
            return None
        return None

    @staticmethod
    def compare(play1, play2) -> int:
        r1 = HandClassifier.classify(play1)
        r2 = HandClassifier.classify(play2)
        if r1 is None or r2 is None:
            return 0
        t1 = (r1[0].value, r1[1], r1[2])
        t2 = (r2[0].value, r2[1], r2[2])
        if t1 > t2:
            return 1
        elif t1 < t2:
            return -1
        return 0

    @staticmethod
    def can_play(last_play, cards) -> bool:
        result = HandClassifier.classify(cards)
        if result is None:
            return False

        if last_play is None:
            # First turn: must include 3♣
            return any(c.rank == 3 and c.suit == 0 for c in cards)

        if len(last_play) != len(cards):
            return False

        last_result = HandClassifier.classify(last_play)
        if last_result is None:
            return False

        if len(cards) != 5:
            # Must be same CardType
            if last_result[0] != result[0]:
                return False

        return HandClassifier.compare(cards, last_play) == 1
