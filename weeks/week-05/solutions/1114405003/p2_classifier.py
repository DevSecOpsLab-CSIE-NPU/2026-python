# -*- coding: utf-8 -*-
"""
大二紙牌遊戲 - Phase 2 牌型分類

實作 HandClassifier 類別，正確分類並比較牌型
"""

from enum import Enum
from typing import List, Optional, Tuple
from p1_models import Card, Hand


# ============================================================================
# 【牌型列舉】
# ============================================================================

class CardType(Enum):
    """
    牌型列舉
    
    定義遊戲中所有可能的牌型及其優先級
    優先級由低到高：
    SINGLE(1) < PAIR(2) < TRIPLE(3) < STRAIGHT(4) < FLUSH(5) < FULL_HOUSE(6) < FOUR_OF_A_KIND(7) < STRAIGHT_FLUSH(8)
    """
    SINGLE = 1           # 單張
    PAIR = 2             # 對子
    TRIPLE = 3           # 三條
    STRAIGHT = 4         # 順子（5張）
    FLUSH = 5            # 同花（5張）
    FULL_HOUSE = 6       # 滿堂紅（5張，3+2）
    FOUR_OF_A_KIND = 7   # 四條（5張，4+1）
    STRAIGHT_FLUSH = 8   # 順子同花（5張）


# ============================================================================
# 【分類器類別】
# ============================================================================

class HandClassifier:
    """
    牌型分類器
    
    根據牌的組合，分類為不同牌型、比較大小、檢查出牌合法性
    """
    
    @staticmethod
    def _is_straight(ranks: List[int]) -> bool:
        """
        檢查是否為順子
        
        支持 A-2-3-4-5 特殊情況（A 作為 1）
        
        Args:
            ranks: 排序後的等級列表
            
        Returns:
            True 如果為順子，False 否則
        """
        if len(ranks) != 5:
            return False
        
        sorted_ranks = sorted(ranks)
        
        # 普通順子：等級連續且跨度為4
        if sorted_ranks[-1] - sorted_ranks[0] == 4 and len(set(sorted_ranks)) == 5:
            return True
        
        # A-2-3-4-5 特殊順子（A作為1）
        if set(sorted_ranks) == {14, 2, 3, 4, 5}:
            return True
        
        return False
    
    @staticmethod
    def _is_flush(suits: List[int]) -> bool:
        """
        檢查是否為同花
        
        Args:
            suits: 花色列表
            
        Returns:
            True 如果所有牌都是同花色，False 否則
        """
        return len(set(suits)) == 1
    
    @staticmethod
    def _count_ranks(cards: List[Card]) -> dict:
        """
        計算每個等級的牌數
        
        Args:
            cards: Card 列表
            
        Returns:
            {rank: count} 字典
        """
        rank_counts = {}
        for card in cards:
            rank = card.rank
            rank_counts[rank] = rank_counts.get(rank, 0) + 1
        return rank_counts
    
    @staticmethod
    def classify(cards: List[Card]) -> Optional[Tuple[CardType, int, int]]:
        """
        分類牌型
        
        Args:
            cards: Card 列表
            
        Returns:
            (CardType, rank, suit) tuple，無法分類時回傳 None
        """
        if not cards:
            return None
        
        length = len(cards)
        
        # 單張
        if length == 1:
            card = cards[0]
            return (CardType.SINGLE, card.rank, card.suit)
        
        # 對子
        if length == 2:
            if cards[0].rank == cards[1].rank:
                return (CardType.PAIR, cards[0].rank, cards[0].suit)
            return None
        
        # 三條
        if length == 3:
            if cards[0].rank == cards[1].rank == cards[2].rank:
                return (CardType.TRIPLE, cards[0].rank, cards[0].suit)
            return None
        
        # 五張牌型
        if length == 5:
            ranks = [card.rank for card in cards]
            suits = [card.suit for card in cards]
            rank_counts = HandClassifier._count_ranks(cards)
            
            # 先判斷是否四條
            for rank, count in rank_counts.items():
                if count == 4:
                    return (CardType.FOUR_OF_A_KIND, rank, 0)
            
            # 再判斷是否滿堂紅
            if sorted(rank_counts.values()) == [2, 3]:
                for rank, count in rank_counts.items():
                    if count == 3:
                        return (CardType.FULL_HOUSE, rank, 0)
            
            # 再判斷是否順子同花
            if HandClassifier._is_flush(suits) and HandClassifier._is_straight(ranks):
                max_rank = max(ranks)
                # 特殊情況：A-2-3-4-5 順子，最大有效等級是 5
                if set(ranks) == {14, 2, 3, 4, 5}:
                    max_rank = 5
                return (CardType.STRAIGHT_FLUSH, max_rank, suits[0])
            
            # 再判斷是否同花
            if HandClassifier._is_flush(suits):
                return (CardType.FLUSH, max(ranks), suits[0])
            
            # 最後判斷是否順子
            if HandClassifier._is_straight(ranks):
                max_rank = max(ranks)
                # 特殊情況：A-2-3-4-5 順子，最大有效等級是 5
                if set(ranks) == {14, 2, 3, 4, 5}:
                    max_rank = 5
                return (CardType.STRAIGHT, max_rank, 0)
            
            return None
        
        return None
    
    @staticmethod
    def compare(classification1: Optional[Tuple[CardType, int, int]], 
                classification2: Optional[Tuple[CardType, int, int]]) -> int:
        """
        比較兩個牌型
        
        牌型優先級：
        1. 優先級高的牌型 > 優先級低的牌型
        2. 同牌型，等級高 > 等級低（等級 2 最高）
        3. 等級相同，花色高 > 花色低
        
        Args:
            classification1: (CardType, rank, suit) tuple
            classification2: (CardType, rank, suit) tuple
            
        Returns:
            1 if classification1 > classification2
            -1 if classification1 < classification2
            0 if equal
        """
        if not classification1 or not classification2:
            return 0
        
        type1, rank1, suit1 = classification1
        type2, rank2, suit2 = classification2
        
        # 先比較牌型等級
        if type1.value != type2.value:
            return 1 if type1.value > type2.value else -1
        
        # 同牌型，比較等級
        if rank1 != rank2:
            # 特殊情況：等級 2 最高
            if rank1 == 2:
                return 1
            if rank2 == 2:
                return -1
            return 1 if rank1 > rank2 else -1
        
        # 等級相同，比較花色
        if suit1 != suit2:
            return 1 if suit1 > suit2 else -1
        
        return 0
    
    @staticmethod
    def can_play(last_classification: Optional[Tuple[CardType, int, int]], 
                 cards_to_play: List[Card]) -> bool:
        """
        檢查是否能出牌
        
        規則：
        1. 首手（last_classification 為 None）必須包含梅花 3
        2. 非首手，必須牌張數相同、牌型相同或牌型更強
        3. 牌型相同時，大小要更大
        
        Args:
            last_classification: 上一手出的牌型，None 表示首手
            cards_to_play: 要出的牌列表
            
        Returns:
            True 可以出牌，False 不能出牌
        """
        # 首手必須包含梅花 3
        if last_classification is None:
            for card in cards_to_play:
                if card.rank == 3 and card.suit == 0:
                    return True
            return False
        
        # 非首手：分類牌型，檢查數量和牌型
        current_classification = HandClassifier.classify(cards_to_play)
        if not current_classification:
            return False
        
        # 牌張數相同
        played_len = len(list(cards_to_play)) if hasattr(cards_to_play, '__iter__') else len(cards_to_play)
        # 需要根據上一手的牌型推測牌數
        last_type = last_classification[0]
        
        # 根據牌型推測合理的牌數
        if last_type in [CardType.SINGLE]:
            required_len = 1
        elif last_type in [CardType.PAIR]:
            required_len = 2
        elif last_type in [CardType.TRIPLE]:
            required_len = 3
        elif last_type in [CardType.STRAIGHT, CardType.FLUSH, CardType.FULL_HOUSE, 
                           CardType.FOUR_OF_A_KIND, CardType.STRAIGHT_FLUSH]:
            required_len = 5
        else:
            required_len = played_len
        
        if played_len != required_len:
            return False
        
        # 牌型相同
        current_type = current_classification[0]
        if current_type != last_type:
            return False
        
        # 牌型相同，比較大小
        return HandClassifier.compare(current_classification, last_classification) > 0


if __name__ == "__main__":
    # 簡單測試
    print("=" * 50)
    print("大二紙牌遊戲 - Phase 2 牌型分類")
    print("=" * 50)
    
    # 建立測試牌
    print("\n【分類測試】")
    
    # 單張
    single = Hand([Card(14, 3)])
    result = HandClassifier.classify(single)
    print(f"單張 ♠A：{result}")
    
    # 對子
    pair = Hand([Card(14, 3), Card(14, 2)])
    result = HandClassifier.classify(pair)
    print(f"對 A：{result}")
    
    # 三條
    triple = Hand([Card(14, 3), Card(14, 2), Card(14, 1)])
    result = HandClassifier.classify(triple)
    print(f"三條 A：{result}")
    
    # 順子
    straight = Hand([Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)])
    result = HandClassifier.classify(straight)
    print(f"順子 3-7：{result}")
    
    # 同花
    flush = Hand([Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)])
    result = HandClassifier.classify(flush)
    print(f"同花 梅花：{result}")
    
    # 滿堂紅
    full_house = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(2, 0), Card(2, 1)])
    result = HandClassifier.classify(full_house)
    print(f"滿堂紅 3A + 2個2：{result}")
    
    # 四條
    four_kind = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 0)])
    result = HandClassifier.classify(four_kind)
    print(f"四條 4A + 1個3：{result}")
    
    # 順子同花
    straight_flush = Hand([Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)])
    result = HandClassifier.classify(straight_flush)
    print(f"順子同花 梅花3-7：{result}")
    
    # 比較
    print("\n【比較測試】")
    single_a = HandClassifier.classify(Hand([Card(14, 3)]))
    single_k = HandClassifier.classify(Hand([Card(13, 3)]))
    result = HandClassifier.compare(single_a, single_k)
    print(f"單A vs 單K：{result} (1=A大)")
    
    pair_a = HandClassifier.classify(Hand([Card(14, 3), Card(14, 2)]))
    single_a = HandClassifier.classify(Hand([Card(14, 3)]))
    result = HandClassifier.compare(pair_a, single_a)
    print(f"對A vs 單A：{result} (1=對子大)")
    
    # 出牌檢查
    print("\n【出牌檢查】")
    three_clubs = Hand([Card(3, 0)])
    can_play = HandClassifier.can_play(None, three_clubs)
    print(f"首手出梅花3：{can_play} (True=可以)")
    
    other_card = Hand([Card(14, 3)])
    can_play = HandClassifier.can_play(None, other_card)
    print(f"首手出黑桃A：{can_play} (False=不可以)")
    
    print("\n" + "=" * 50)
    print("✅ 所有操作完成")
    print("=" * 50)
