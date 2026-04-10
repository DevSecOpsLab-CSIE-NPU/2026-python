from enum import IntEnum
from typing import List, Tuple, Optional

class CardType(IntEnum):
    INVALID = 0
    SINGLE = 1
    PAIR = 2
    TRIPLE = 3
    STRAIGHT = 4        # 順子
    FLUSH = 5           # 同花
    FULL_HOUSE = 6      # 葫蘆
    FOUR_OF_A_KIND = 7  # 鐵支
    STRAIGHT_FLUSH = 8  # 同花順

class HandClassifier:
    """判定牌型與比較大小的絕對規則引擎"""
    
    @staticmethod
    def classify(cards: List['Card']) -> Optional[Tuple[CardType, int, int]]:
        """回傳 (牌型, 權重數字, 權重花色)"""
        if not cards: return None
        n = len(cards)
        s_cards = sorted(cards)
        ranks = [c.rank for c in s_cards]
        suits = [c.suit for c in s_cards]

        if n == 1: return (CardType.SINGLE, ranks[0], suits[0])
        if n == 2 and ranks[0] == ranks[1]: return (CardType.PAIR, ranks[0], max(suits))
        if n == 3 and ranks[0] == ranks[1] == ranks[2]: return (CardType.TRIPLE, ranks[0], max(suits))
        
        if n == 5:
            is_straight, s_rank, s_suit = HandClassifier._check_straight(s_cards)
            is_flush = len(set(suits)) == 1
            f_rank, f_suit = ranks[4], suits[4]

            if is_straight and is_flush: return (CardType.STRAIGHT_FLUSH, s_rank, s_suit)
            
            # 鐵支 (4+1)
            for r in set(ranks):
                if ranks.count(r) == 4: return (CardType.FOUR_OF_A_KIND, r, 0)
            
            # 葫蘆 (3+2)
            if len(set(ranks)) == 2:
                for r in set(ranks):
                    if ranks.count(r) == 3: return (CardType.FULL_HOUSE, r, 0)
            
            if is_flush: return (CardType.FLUSH, f_rank, f_suit)
            if is_straight: return (CardType.STRAIGHT, s_rank, s_suit)

        return None

    @staticmethod
    def _check_straight(cards: List['Card']) -> Tuple[bool, int, int]:
        ranks = sorted([c.rank for c in cards])
        # 特例：A-2-3-4-5 (14, 15, 3, 4, 5) -> 最大牌為 2(15)
        if set(ranks) == {14, 15, 3, 4, 5}:
            max_c = next(c for c in cards if c.rank == 15)
            return True, 15, max_c.suit
        # 特例：2-3-4-5-6 (15, 3, 4, 5, 6) -> 最大牌為 2(15)
        if set(ranks) == {15, 3, 4, 5, 6}:
            max_c = next(c for c in cards if c.rank == 15)
            return True, 15, max_c.suit
        
        # 一般順子
        if all(ranks[i] + 1 == ranks[i+1] for i in range(4)):
            max_c = next(c for c in cards if c.rank == ranks[4])
            return True, ranks[4], max_c.suit
        return False, 0, 0

    @staticmethod
    def compare(play1: List['Card'], play2: List['Card']) -> int:
        """回傳 1(play1贏), -1(play2贏), 0(不合法)"""
        c1 = HandClassifier.classify(play1)
        c2 = HandClassifier.classify(play2)
        if not c1 or not c2: return 0
        if len(play1) != len(play2): return 0
        
        # 5張牌互壓 (例：葫蘆壓順子)
        if c1[0] != c2[0]:
            if len(play1) == 5: return 1 if c1[0] > c2[0] else -1
            return 0
            
        # 同牌型比數字
        if c1[1] != c2[1]: return 1 if c1[1] > c2[1] else -1
        # 數字同比花色
        if c1[2] != c2[2]: return 1 if c1[2] > c2[2] else -1
        return 0