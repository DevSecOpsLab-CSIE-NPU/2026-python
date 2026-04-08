"""
Phase 2: 牌型分類
HandClassifier 類別實作
"""

from enum import IntEnum
from typing import List, Optional, Tuple, Dict
from collections import Counter
from game.models import Card


class CardType(IntEnum):
    """牌型列舉"""
    SINGLE = 1
    PAIR = 2
    TRIPLE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8


class HandClassifier:
    """牌型分類器"""
    
    @staticmethod
    def _is_straight(ranks: List[int]) -> bool:
        """
        檢查是否為順子
        :param ranks: 牌的 rank 列表
        :return: 是否為順子
        """
        if len(ranks) != 5:
            return False
        
        sorted_ranks = sorted(ranks)
        
        # 檢查普通順子 (連續5張)
        if sorted_ranks[-1] - sorted_ranks[0] == 4 and len(set(ranks)) == 5:
            return True
        
        # 檢查 A-2-3-4-5 特殊情況 (rank: 14,15,3,4,5)
        if set(ranks) == {3, 4, 5, 14, 15}:
            return True
        
        return False
    
    @staticmethod
    def _is_flush(suits: List[int]) -> bool:
        """
        檢查是否為同花
        :param suits: 牌的 suit 列表
        :return: 是否為同花
        """
        return len(set(suits)) == 1
    
    @staticmethod
    def classify(cards: List[Card]) -> Optional[Tuple[CardType, int, int]]:
        """
        分類牌型
        :param cards: 牌的列表
        :return: (牌型, 主要數字, 花色) 或 None
        """
        if not cards:
            return None
        
        n = len(cards)
        ranks = [c.rank for c in cards]
        suits = [c.suit for c in cards]
        rank_counts = Counter(ranks)
        suit_counts = Counter(suits)
        
        # 1. 單張
        if n == 1:
            return (CardType.SINGLE, cards[0].rank, cards[0].suit)
        
        # 2. 對子 (2張相同rank)
        if n == 2:
            if ranks[0] == ranks[1]:
                return (CardType.PAIR, ranks[0], suits[0])
            return None
        
        # 3. 三條 (3張相同rank)
        if n == 3:
            if len(rank_counts) == 1:
                return (CardType.TRIPLE, ranks[0], suits[0])
            return None
        
        # 4. 5張牌型
        if n == 5:
            is_straight = HandClassifier._is_straight(ranks)
            is_flush = HandClassifier._is_flush(suits)
            
            # 4.1 同花順
            if is_straight and is_flush:
                # 計算最大rank（A-2-3-4-5時取5）
                sorted_ranks = sorted(set(ranks))
                if set(ranks) == {3, 4, 5, 14, 15}:
                    max_rank = 5
                else:
                    max_rank = sorted_ranks[-1]
                return (CardType.STRAIGHT_FLUSH, max_rank, suits[0])
            
            # 4.2 四條 (4張相同rank)
            if 4 in rank_counts.values():
                quad_rank = [r for r, c in rank_counts.items() if c == 4][0]
                quad_suit = [c.suit for c in cards if c.rank == quad_rank][0]
                return (CardType.FOUR_OF_A_KIND, quad_rank, quad_suit)
            
            # 4.3 葫蘆 (3+2)
            if 3 in rank_counts.values() and 2 in rank_counts.values():
                triple_rank = [r for r, c in rank_counts.items() if c == 3][0]
                triple_suit = [c.suit for c in cards if c.rank == triple_rank][0]
                return (CardType.FULL_HOUSE, triple_rank, triple_suit)
            
            # 4.4 同花
            if is_flush:
                max_rank = max(ranks)
                return (CardType.FLUSH, max_rank, suits[0])
            
            # 4.5 順子
            if is_straight:
                sorted_ranks = sorted(set(ranks))
                if set(ranks) == {3, 4, 5, 14, 15}:
                    max_rank = 5
                else:
                    max_rank = sorted_ranks[-1]
                # 找最大flower的牌作為代表
                max_suit = max([c.suit for c in cards if c.rank == max_rank])
                return (CardType.STRAIGHT, max_rank, max_suit)
            
            return None
        
        # 其他情況
        return None
    
    @staticmethod
    def compare(play1: List[Card], play2: List[Card]) -> int:
        """
        比較兩手牌大小
        :param play1: 第一手牌
        :param play2: 第二手牌
        :return: 1 if play1 > play2, -1 if play1 < play2, 0 if equal
        """
        result1 = HandClassifier.classify(play1)
        result2 = HandClassifier.classify(play2)
        
        # 牌型不合法
        if result1 is None or result2 is None:
            return 0
        
        type1, rank1, suit1 = result1
        type2, rank2, suit2 = result2
        
        # 不同牌型
        if type1 != type2:
            if type1 > type2:
                return 1
            else:
                return -1
        
        # 同牌型，比大小
        if rank1 != rank2:
            if rank1 > rank2:
                return 1
            else:
                return -1
        
        # rank相同，比花色
        if suit1 != suit2:
            if suit1 > suit2:
                return 1
            else:
                return -1
        
        # 完全相同
        return 0
    
    @staticmethod
    def can_play(last_play: Optional[Tuple[List[Card], str]], cards: List[Card]) -> bool:
        """
        檢查是否可以出牌
        :param last_play: 上家的牌和玩家名稱
        :param cards: 想要出的牌
        :return: 是否可以出牌
        """
        # 第一回合，只能出3♣
        if last_play is None:
            if len(cards) != 1:
                return False
            card = cards[0]
            return card.rank == 3 and card.suit == 0
        
        # 上家出牌，需要根據牌型進行比較
        last_cards, _ = last_play
        
        # 牌數必須相同
        if len(cards) != len(last_cards):
            return False
        
        # 分類兩手牌
        result_last = HandClassifier.classify(last_cards)
        result_curr = HandClassifier.classify(cards)
        
        if result_last is None or result_curr is None:
            return False
        
        type_last, rank_last, suit_last = result_last
        type_curr, rank_curr, suit_curr = result_curr
        
        # 如果牌型不同，新牌必須是更大的牌型
        if type_curr != type_last:
            return type_curr > type_last
        
        # 牌型相同，比大小
        return HandClassifier.compare(cards, last_cards) > 0
