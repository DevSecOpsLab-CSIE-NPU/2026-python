from enum import Enum

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
    # 牌型分數對照表，用於 compare 跨牌型比較
    TYPE_SCORES = {
        CardType.SINGLE: 1, CardType.PAIR: 2, CardType.TRIPLE: 3,
        CardType.STRAIGHT: 4, CardType.FLUSH: 5, CardType.FULL_HOUSE: 6,
        CardType.FOUR_OF_A_KIND: 7, CardType.STRAIGHT_FLUSH: 8,
    }

    @staticmethod
    def _ranks(cards):
        return [c.rank for c in cards]

    @staticmethod
    def _suits(cards):
        return [c.suit for c in cards]

    @staticmethod
    def _is_straight(ranks):
        s = sorted(set(ranks))
        if len(s) < 5:
            return False
        if s[-1] - s[0] == 4:
            return True
        if set(ranks) == {14, 15, 3, 4, 5}:
            return True
        return False

    @staticmethod
    def _straight_high(ranks):
        s = sorted(set(ranks))
        if s[-1] - s[0] == 4:
            return s[-1]
        return 5

    @staticmethod
    def _is_flush(suits):
        return len(set(suits)) == 1

    @staticmethod
    def classify(cards):
        n = len(cards)
        if n == 1:
            return (CardType.SINGLE, cards[0].rank, cards[0].suit)
        if n == 2:
            if cards[0].rank == cards[1].rank:
                return (CardType.PAIR, cards[0].rank, max(c.suit for c in cards))
            return None
        if n == 3:
            if cards[0].rank == cards[1].rank == cards[2].rank:
                return (CardType.TRIPLE, cards[0].rank, max(c.suit for c in cards))
            return None
        if n == 5:
            ranks = HandClassifier._ranks(cards)
            suits = HandClassifier._suits(cards)
            straight = HandClassifier._is_straight(ranks)
            flush = HandClassifier._is_flush(suits)
            from collections import Counter
            rc = Counter(ranks)
            count_vals = sorted(rc.values(), reverse=True)
            if straight and flush:
                return (CardType.STRAIGHT_FLUSH, HandClassifier._straight_high(ranks), 0)
            if count_vals == [4, 1]:
                four_rank = [r for r, c in rc.items() if c == 4][0]
                return (CardType.FOUR_OF_A_KIND, four_rank, 0)
            if count_vals == [3, 2]:
                three_rank = [r for r, c in rc.items() if c == 3][0]
                return (CardType.FULL_HOUSE, three_rank, 0)
            if flush:
                return (CardType.FLUSH, max(ranks), max(suits))
            if straight:
                return (CardType.STRAIGHT, HandClassifier._straight_high(ranks), 0)
            return None
        return None

    @staticmethod
    def compare(play1, play2):
        r1 = HandClassifier.classify(play1)
        r2 = HandClassifier.classify(play2)
        if not r1 or not r2:
            return 0
        t1, rank1, suit1 = r1
        t2, rank2, suit2 = r2
        if t1 != t2:
            return 1 if HandClassifier.TYPE_SCORES[t1] > HandClassifier.TYPE_SCORES[t2] else -1
        if rank1 != rank2:
            return 1 if rank1 > rank2 else -1
        if suit1 != suit2:
            return 1 if suit1 > suit2 else -1
        return 0

    @staticmethod
    def can_play(last_play, cards):
        if last_play is None:
            return any(c.rank == 3 and c.suit == 0 for c in cards)
        if len(cards) != len(last_play):
            return False
        return HandClassifier.compare(cards, last_play) == 1
