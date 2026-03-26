"""
Phase 2: 牌型分類 - HandClassifier 類別
"""
from enum import IntEnum
from typing import List, Optional, Tuple
from .models import Card


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
        
        Args:
            ranks: 點數列表（已排序）
            
        Returns:
            是否為順子
        """
        if len(ranks) != 5:
            return False
        
        # 檢查 A-2-3-4-5 特殊情況
        if set(ranks) == {14, 15, 3, 4, 5}:
            return True
        
        # 檢查連續性
        sorted_ranks = sorted(ranks)
        for i in range(1, len(sorted_ranks)):
            if sorted_ranks[i] != sorted_ranks[i-1] + 1:
                return False
        return True
    
    @staticmethod
    def _is_flush(suits: List[int]) -> bool:
        """
        檢查是否為同花
        
        Args:
            suits: 花色列表
            
        Returns:
            是否為同花
        """
        return len(set(suits)) == 1
    
    @staticmethod
    def _count_ranks(cards: List[Card]) -> dict:
        """
        統計各點數的數量
        
        Args:
            cards: 牌列表
            
        Returns:
            {rank: count, ...}
        """
        count = {}
        for card in cards:
            count[card.rank] = count.get(card.rank, 0) + 1
        return count
    
    @staticmethod
    def classify(cards: List[Card]) -> Optional[Tuple[CardType, int, int]]:
        """
        分類牌型
        
        Args:
            cards: 要分類的牌
            
        Returns:
            (牌型, 數字, 花色) 或 None
        """
        n = len(cards)
        
        if n == 1:
            # 單張
            return (CardType.SINGLE, cards[0].rank, cards[0].suit)
        
        if n == 2:
            # 對子
            if cards[0].rank == cards[1].rank:
                return (CardType.PAIR, cards[0].rank, max(cards[0].suit, cards[1].suit))
            return None
        
        if n == 3:
            # 三條
            if cards[0].rank == cards[1].rank == cards[2].rank:
                return (CardType.TRIPLE, cards[0].rank, max(c.suit for c in cards))
            return None
        
        if n == 5:
            ranks = [card.rank for card in cards]
            suits = [card.suit for card in cards]
            is_straight = HandClassifier._is_straight(ranks)
            is_flush = HandClassifier._is_flush(suits)
            
            # 同花順
            if is_straight and is_flush:
                max_rank = 5 if set(ranks) == {14, 15, 3, 4, 5} else max(ranks)
                return (CardType.STRAIGHT_FLUSH, max_rank, suits[0])
            
            # 四條
            rank_count = HandClassifier._count_ranks(cards)
            counts = list(rank_count.values())
            if 4 in counts:
                quad_rank = [r for r, c in rank_count.items() if c == 4][0]
                max_suit = max(c.suit for c in cards if c.rank == quad_rank)
                return (CardType.FOUR_OF_A_KIND, quad_rank, max_suit)
            
            # 葫蘆（三條+對子）
            if 3 in counts and 2 in counts:
                triple_rank = [r for r, c in rank_count.items() if c == 3][0]
                max_suit = max(c.suit for c in cards if c.rank == triple_rank)
                return (CardType.FULL_HOUSE, triple_rank, max_suit)
            
            # 同花
            if is_flush:
                max_rank = max(ranks)
                return (CardType.FLUSH, max_rank, suits[0])
            
            # 順子
            if is_straight:
                max_rank = 5 if set(ranks) == {14, 15, 3, 4, 5} else max(ranks)
                max_suit = max(c.suit for c in cards if c.rank == max_rank)
                return (CardType.STRAIGHT, max_rank, max_suit)
            
            return None
        
        return None
    
    @staticmethod
    def compare(play1: List[Card], play2: List[Card]) -> int:
        """
        比較兩手牌的大小
        
        Args:
            play1: 第一手牌
            play2: 第二手牌
            
        Returns:
            1 if play1 > play2, -1 if play1 < play2, 0 if equal
        """
        type1 = HandClassifier.classify(play1)
        type2 = HandClassifier.classify(play2)
        
        if type1 is None or type2 is None:
            return 0
        
        card_type1, num1, suit1 = type1
        card_type2, num2, suit2 = type2
        
        # 牌型不同，牌型高者勝
        if card_type1 != card_type2:
            return 1 if card_type1 > card_type2 else -1
        
        # 牌型相同，比較數字
        if num1 != num2:
            # 使用 RANK_ORDER 比較
            rank_order1 = Card.RANK_ORDER.get(num1, 0)
            rank_order2 = Card.RANK_ORDER.get(num2, 0)
            return 1 if rank_order1 > rank_order2 else -1
        
        # 數字相同，比較花色
        return 1 if suit1 > suit2 else (-1 if suit1 < suit2 else 0)
    
    @staticmethod
    def can_play(last_play: Optional[List[Card]], cards: List[Card]) -> bool:
        """
        檢查是否可以出牌
        
        Args:
            last_play: 上家的牌（None 表示第一回合）
            cards: 要出的牌
            
        Returns:
            是否可以出牌
        """
        # 第一回合只能出 3♣
        if last_play is None:
            if len(cards) == 1:
                card = cards[0]
                return card.rank == 3 and card.suit == 0
            return False
        
        # 分類檢查
        last_type = HandClassifier.classify(last_play)
        curr_type = HandClassifier.classify(cards)
        
        if last_type is None or curr_type is None:
            return False
        
        # 必須同一牌型
        if last_type[0] != curr_type[0]:
            return False
        
        # 必須比上家大
        return HandClassifier.compare(cards, last_play) > 0
