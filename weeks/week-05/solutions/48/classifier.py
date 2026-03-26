from __future__ import annotations

from collections import Counter
from enum import Enum
from typing import Optional

from models import Card


class CardType(Enum):
    """牌型列舉，數值越大代表牌型層級越高。"""

    SINGLE = 1
    PAIR = 2
    TRIPLE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8


class HandClassifier:
    """Big Two 牌型分類與比較工具。"""

    @staticmethod
    def _is_straight(ranks: list[int]) -> bool:
        ok, _ = HandClassifier._straight_high_rank(ranks)
        return ok

    @staticmethod
    def _straight_high_rank(ranks: list[int]) -> tuple[bool, int]:
        """判斷順子，並回傳是否成立與順子最高點數。"""
        if len(ranks) != 5:
            return False, 0

        unique = set(ranks)
        if len(unique) != 5:
            return False, 0

        # 特例：A-2-3-4-5，最高點數按 5 計算。
        if unique == {14, 15, 3, 4, 5}:
            return True, 5

        sorted_ranks = sorted(unique)
        for i in range(4):
            if sorted_ranks[i + 1] - sorted_ranks[i] != 1:
                return False, 0
        return True, sorted_ranks[-1]

    @staticmethod
    def _is_flush(suits: list[int]) -> bool:
        return len(set(suits)) == 1

    @staticmethod
    def classify(cards: list[Card]) -> Optional[tuple[CardType, int, int]]:
        """分類牌型並回傳 (牌型, 數字比較值, 花色比較值)；不合法回傳 None。"""
        n = len(cards)
        if n == 0:
            return None

        ranks = [c.rank for c in cards]
        suits = [c.suit for c in cards]
        rank_counter = Counter(ranks)

        if n == 1:
            c = cards[0]
            return CardType.SINGLE, c.rank, c.suit

        if n == 2:
            if len(rank_counter) == 1:
                rank = ranks[0]
                return CardType.PAIR, rank, 0
            return None

        if n == 3:
            if len(rank_counter) == 1:
                rank = ranks[0]
                return CardType.TRIPLE, rank, 0
            return None

        if n != 5:
            return None

        is_flush = HandClassifier._is_flush(suits)
        is_straight, straight_high = HandClassifier._straight_high_rank(ranks)

        if is_flush and is_straight:
            return CardType.STRAIGHT_FLUSH, straight_high, 0

        if 4 in rank_counter.values():
            four_rank = next(rank for rank, cnt in rank_counter.items() if cnt == 4)
            return CardType.FOUR_OF_A_KIND, four_rank, 0

        if sorted(rank_counter.values()) == [2, 3]:
            triple_rank = next(rank for rank, cnt in rank_counter.items() if cnt == 3)
            return CardType.FULL_HOUSE, triple_rank, 0

        if is_flush:
            return CardType.FLUSH, max(ranks), 0

        if is_straight:
            return CardType.STRAIGHT, straight_high, 0

        return None

    @staticmethod
    def compare(play1: list[Card], play2: list[Card]) -> int:
        """比較兩手牌：1=play1大、-1=play2大、0=平手或無法比較。"""
        c1 = HandClassifier.classify(play1)
        c2 = HandClassifier.classify(play2)
        if c1 is None or c2 is None:
            return 0

        t1, r1, s1 = c1
        t2, r2, s2 = c2

        if t1.value != t2.value:
            return 1 if t1.value > t2.value else -1

        if r1 != r2:
            return 1 if r1 > r2 else -1

        # 對子/三條在同點數時，額外比該手中的最大花色。
        if t1 in (CardType.PAIR, CardType.TRIPLE):
            max_s1 = max(card.suit for card in play1)
            max_s2 = max(card.suit for card in play2)
            if max_s1 != max_s2:
                return 1 if max_s1 > max_s2 else -1

        if s1 != s2:
            return 1 if s1 > s2 else -1

        return 0

    @staticmethod
    def can_play(last_play: Optional[list[Card]], cards: list[Card]) -> bool:
        """檢查是否可出牌：首出需含 3♣，其餘需能壓過上一手。"""
        current = HandClassifier.classify(cards)
        if current is None:
            return False

        if last_play is None:
            # 第一手需包含 3♣。
            return Card(3, 0) in cards

        last = HandClassifier.classify(last_play)
        if last is None:
            return False

        # 非五張牌通常必須同張數；五張牌可跨牌型比較。
        if len(cards) != len(last_play):
            return False

        if len(cards) != 5 and current[0] != last[0]:
            return False

        return HandClassifier.compare(cards, last_play) == 1
