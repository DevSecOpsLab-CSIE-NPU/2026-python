"""
Phase 3: 牌型搜尋 - HandFinder 類別
"""
from typing import List, Optional
from itertools import combinations
from .models import Card, Hand
from .classifier import HandClassifier, CardType


class HandFinder:
    """牌型搜尋器"""
    
    @staticmethod
    def find_singles(hand: Hand) -> List[List[Card]]:
        """
        找出所有單張組合
        
        Args:
            hand: 玩家手牌
            
        Returns:
            所有單張組合
        """
        return [[card] for card in hand]
    
    @staticmethod
    def find_pairs(hand: Hand) -> List[List[Card]]:
        """
        找出所有對子組合
        
        Args:
            hand: 玩家手牌
            
        Returns:
            所有對子組合
        """
        pairs = []
        ranks_dict = {}
        
        # 按點數分組
        for card in hand:
            if card.rank not in ranks_dict:
                ranks_dict[card.rank] = []
            ranks_dict[card.rank].append(card)
        
        # 對每個點數，找所有可能的對子
        for rank, cards in ranks_dict.items():
            if len(cards) >= 2:
                for combo in combinations(cards, 2):
                    pairs.append(list(combo))
        
        return pairs
    
    @staticmethod
    def find_triples(hand: Hand) -> List[List[Card]]:
        """
        找出所有三條組合
        
        Args:
            hand: 玩家手牌
            
        Returns:
            所有三條組合
        """
        triples = []
        ranks_dict = {}
        
        # 按點數分組
        for card in hand:
            if card.rank not in ranks_dict:
                ranks_dict[card.rank] = []
            ranks_dict[card.rank].append(card)
        
        # 對每個點數，找所有可能的三條
        for rank, cards in ranks_dict.items():
            if len(cards) >= 3:
                for combo in combinations(cards, 3):
                    triples.append(list(combo))
        
        return triples
    
    @staticmethod
    def _find_straight_from(hand: Hand, start_rank: int) -> Optional[List[Card]]:
        """
        從指定點數開始查找順子
        
        Args:
            hand: 玩家手牌
            start_rank: 開始點數
            
        Returns:
            順子或 None
        """
        # 特殊情況：A-2-3-4-5
        if start_rank == 5:
            ranks_needed = [14, 15, 3, 4, 5]
        else:
            ranks_needed = list(range(start_rank - 4, start_rank + 1))
        
        result = []
        for rank in sorted(ranks_needed):
            # 找該點數的任意花色
            found = False
            for card in hand:
                if card.rank == rank and card not in result:
                    result.append(card)
                    found = True
                    break
            if not found:
                return None
        
        return result if len(result) == 5 else None
    
    @staticmethod
    def find_fives(hand: Hand) -> List[List[Card]]:
        """
        找出所有五張牌型
        
        Args:
            hand: 玩家手牌
            
        Returns:
            所有五張牌型（順子、同花、葫蘆、四條、同花順）
        """
        fives = []
        
        if len(hand) < 5:
            return fives
        
        # 對所有五張組合進行分類
        for combo in combinations(hand, 5):
            cards = list(combo)
            classification = HandClassifier.classify(cards)
            if classification is not None:
                # 只保留有效的五張牌型
                card_type = classification[0]
                if card_type in [CardType.STRAIGHT, CardType.FLUSH, 
                                CardType.FULL_HOUSE, CardType.FOUR_OF_A_KIND,
                                CardType.STRAIGHT_FLUSH]:
                    fives.append(cards)
        
        return fives
    
    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: Optional[List[Card]]) -> List[List[Card]]:
        """
        找出所有合法的出牌
        
        Args:
            hand: 玩家手牌
            last_play: 上家的牌（None 表示第一回合）
            
        Returns:
            所有合法的出牌組合
        """
        valid_plays = []
        
        # 第一回合
        if last_play is None:
            # 只能出 3♣
            for card in hand:
                if card.rank == 3 and card.suit == 0:
                    valid_plays.append([card])
                    break
            return valid_plays
        
        # 取得上家的牌型
        last_type = HandClassifier.classify(last_play)
        if last_type is None:
            return []
        
        card_type = last_type[0]
        
        # 根據牌型查找對應的組合
        if card_type == CardType.SINGLE:
            candidates = HandFinder.find_singles(hand)
        elif card_type == CardType.PAIR:
            candidates = HandFinder.find_pairs(hand)
        elif card_type == CardType.TRIPLE:
            candidates = HandFinder.find_triples(hand)
        elif card_type in [CardType.STRAIGHT, CardType.FLUSH, 
                          CardType.FULL_HOUSE, CardType.FOUR_OF_A_KIND,
                          CardType.STRAIGHT_FLUSH]:
            candidates = HandFinder.find_fives(hand)
        else:
            candidates = []
        
        # 檢查合法性
        for combo in candidates:
            if HandClassifier.can_play(last_play, combo):
                valid_plays.append(combo)
        
        return valid_plays
