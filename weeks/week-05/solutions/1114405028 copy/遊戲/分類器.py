from typing import List, Optional, Tuple
from enum import Enum
from .models import Card

class CardType(Enum):
    SINGLE = 1        # 單張
    PAIR = 2          # 對子
    TRIPLE = 3       # 三條
    STRAIGHT = 4      # 順子
    FLUSH = 5         # 同花
    FULL_HOUSE = 6    # 葫芦
    FOUR_OF_A_KIND = 7 # 四條
    STRAIGHT_FLUSH = 8 # 同花順

class HandClassifier:
    @staticmethod
    def _is_straight(ranks: List[int]) -> bool:
        # 檢查是否為順子，處理 A-2-3-4-5 特殊情況
        sorted_ranks = sorted(ranks)
        # 正常順子
        if sorted_ranks == list(range(sorted_ranks[0], sorted_ranks[0] + 5)):
            return True
        # A-2-3-4-5 順子
        if sorted_ranks == [3, 4, 5, 14, 15]:
            return True
        return False
    
    @staticmethod
    def _is_flush(suits: List[int]) -> bool:
        # 檢查是否為同花
        return len(set(suits)) == 1
    
    @staticmethod
    def classify(cards: List[Card]) -> Optional[Tuple[CardType, int, int]]:
        # 分類牌型
        if not cards:
            return None
        
        n = len(cards)
        ranks = [c.rank for c in cards]
        suits = [c.suit for c in cards]
        
        if n == 1:
            # 單張
            return (CardType.SINGLE, ranks[0], suits[0])
        elif n == 2:
            # 對子
            if len(set(ranks)) == 1:
                return (CardType.PAIR, ranks[0], max(suits))
        elif n == 3:
            # 三條
            if len(set(ranks)) == 1:
                return (CardType.TRIPLE, ranks[0], max(suits))
        elif n == 5:
            rank_counts = {}
            for r in ranks:
                rank_counts[r] = rank_counts.get(r, 0) + 1
            
            is_flush = HandClassifier._is_flush(suits)
            is_straight = HandClassifier._is_straight(ranks)
            
            if is_flush and is_straight:
                # 同花順
                return (CardType.STRAIGHT_FLUSH, max(ranks), max(suits))
            elif 4 in rank_counts.values():
                # 四條
                four_rank = [r for r, c in rank_counts.items() if c == 4][0]
                return (CardType.FOUR_OF_A_KIND, four_rank, max(suits))
            elif 3 in rank_counts.values() and 2 in rank_counts.values():
                # 葫芦
                three_rank = [r for r, c in rank_counts.items() if c == 3][0]
                return (CardType.FULL_HOUSE, three_rank, max(suits))
            elif is_flush:
                # 同花
                return (CardType.FLUSH, max(ranks), max(suits))
            elif is_straight:
                # 順子
                return (CardType.STRAIGHT, max(ranks), max(suits))
        
        return None
    
    @staticmethod
    def compare(play1: List[Card], play2: List[Card]) -> int:
        # 比較兩手牌大小
        type1 = HandClassifier.classify(play1)
        type2 = HandClassifier.classify(play2)
        
        if type1 is None or type2 is None:
            return 0  # 無效牌型
        
        if type1[0].value != type2[0].value:
            # 不同牌型
            return 1 if type1[0].value > type2[0].value else -1
        
        # 同牌型，比較數字，花色
        if type1[1] != type2[1]:
            return 1 if type1[1] > type2[1] else -1
        if type1[2] != type2[2]:
            return 1 if type1[2] > type2[2] else -1
        return 0
    
    @staticmethod
    def can_play(last_play: Optional[List[Card]], cards: List[Card]) -> bool:
        # 檢查是否可以出牌
        if last_play is None:
            # 第一回合，只能出3♣
            return len(cards) == 1 and Card(3, 0) in cards
        
        # 後續回合，牌型相同，且大於上一手
        type_last = HandClassifier.classify(last_play)
        type_current = HandClassifier.classify(cards)
        
        if type_current is None:
            return False
        
        if type_last[0] != type_current[0]:
            return False
        
        return HandClassifier.compare(cards, last_play) == 1