"""
Phase 3: 牌型搜尋
HandFinder 類別實作
"""

from typing import List, Optional
from itertools import combinations
from game.models import Card, Hand
from game.classifier import HandClassifier, CardType


class HandFinder:
    """牌型搜尋器"""
    
    @staticmethod
    def find_singles(hand: Hand) -> List[List[Card]]:
        """
        找出所有單張可能
        :param hand: 手牌
        :return: [[card1], [card2], ...]
        """
        return [[card] for card in hand]
    
    @staticmethod
    def find_pairs(hand: Hand) -> List[List[Card]]:
        """
        找出所有對子可能
        :param hand: 手牌
        :return: 所有對子組合
        """
        result = []
        
        # 對每個rank找出所有相同的牌
        rank_groups = {}
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)
        
        # 每個rank組中選2張
        for rank, cards in rank_groups.items():
            if len(cards) >= 2:
                for pair in combinations(cards, 2):
                    result.append(list(pair))
        
        return result
    
    @staticmethod
    def find_triples(hand: Hand) -> List[List[Card]]:
        """
        找出所有三條可能
        :param hand: 手牌
        :return: 所有三條組合
        """
        result = []
        
        # 對每個rank找出所有相同的牌
        rank_groups = {}
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)
        
        # 每個rank組中選3張
        for rank, cards in rank_groups.items():
            if len(cards) >= 3:
                for triple in combinations(cards, 3):
                    result.append(list(triple))
        
        return result
    
    @staticmethod
    def _find_straight_from(hand: Hand, start_rank: int) -> Optional[List[Card]]:
        """
        從指定 rank 找順子
        :param hand: 手牌
        :param start_rank: 開始的rank
        :return: 找到的順子或None
        """
        # 需要5張牌
        needed_ranks = list(range(start_rank, start_rank + 5))
        
        # 構造rank -> cards的對應
        rank_to_cards = {}
        for card in hand:
            if card.rank not in rank_to_cards:
                rank_to_cards[card.rank] = []
            rank_to_cards[card.rank].append(card)
        
        # 檢查每個需要的rank是否都有牌
        straight_cards = []
        for rank in needed_ranks:
            if rank not in rank_to_cards or not rank_to_cards[rank]:
                return None
            straight_cards.append(rank_to_cards[rank][0])
        
        return straight_cards
    
    @staticmethod
    def find_fives(hand: Hand) -> List[List[Card]]:
        """
        找出所有5張牌型（順子、同花、葫蘆、四條、同花順）
        :param hand: 手牌
        :return: 所有5張牌組合
        """
        result = []
        
        # 1. 尋找同花順
        for start_rank in range(3, 11):  # 3-6-7-8-9-10-J-Q-K-A
            # 普通順子
            straight = HandFinder._find_straight_from(hand, start_rank)
            if straight:
                # 檢查是否同花
                suits = [c.suit for c in straight]
                if len(set(suits)) == 1:
                    result.append(straight)
        
        # 2. A-2-3-4-5 特殊順子（同花順）
        rank_to_cards = {}
        for card in hand:
            if card.rank not in rank_to_cards:
                rank_to_cards[card.rank] = []
            rank_to_cards[card.rank].append(card)
        
        if all(r in rank_to_cards for r in [14, 15, 3, 4, 5]):
            cards_for_wheel = [rank_to_cards[r][0] for r in [15, 4, 5, 3, 14]]
            suits = [c.suit for c in cards_for_wheel]
            if len(set(suits)) == 1:
                result.append(cards_for_wheel)
        
        # 3. 尋找普通順子（非同花）
        for start_rank in range(3, 11):
            straight = HandFinder._find_straight_from(hand, start_rank)
            if straight:
                suits = [c.suit for c in straight]
                if len(set(suits)) != 1:  # 不是同花
                    result.append(straight)
        
        # 4. A-2-3-4-5 普通順子
        if all(r in rank_to_cards for r in [14, 15, 3, 4, 5]):
            cards_for_wheel = [rank_to_cards[r][0] for r in [15, 4, 5, 3, 14]]
            suits = [c.suit for c in cards_for_wheel]
            if len(set(suits)) != 1:
                result.append(cards_for_wheel)
        
        # 5. 尋找同花
        suit_to_cards = {}
        for card in hand:
            if card.suit not in suit_to_cards:
                suit_to_cards[card.suit] = []
            suit_to_cards[card.suit].append(card)
        
        for suit, cards in suit_to_cards.items():
            if len(cards) >= 5:
                for flush in combinations(cards, 5):
                    flush_list = list(flush)
                    # 檢查是否已經在順子中
                    if flush_list not in result:
                        result.append(flush_list)
        
        # 6. 尋找葫蘆、四條
        from collections import Counter
        for combo in combinations(hand, 5):
            result_found = HandClassifier.classify(list(combo))
            if result_found and result_found[0] in [CardType.FULL_HOUSE, CardType.FOUR_OF_A_KIND]:
                if list(combo) not in result:
                    result.append(list(combo))
        
        return result
    
    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: Optional[tuple]) -> List[List[Card]]:
        """
        根據上家的牌型，回傳所有合法出牌
        :param hand: 手牌
        :param last_play: (cards, player_name) 或 None
        :return: 所有合法出牌
        """
        result = []
        
        # 第一回合
        if last_play is None:
            three_clubs = hand.find_3_clubs()
            if three_clubs:
                result.append([three_clubs])
            return result
        
        last_cards, _ = last_play
        last_result = HandClassifier.classify(last_cards)
        
        if last_result is None:
            return result
        
        last_type, _, _ = last_result
        last_len = len(last_cards)
        
        # 根據上家牌的長度尋找合法出牌
        if last_len == 1:
            # 單張
            for single in HandFinder.find_singles(hand):
                if HandClassifier.can_play(last_play, single):
                    result.append(single)
        
        elif last_len == 2:
            # 對子
            for pair in HandFinder.find_pairs(hand):
                if HandClassifier.can_play(last_play, pair):
                    result.append(pair)
        
        elif last_len == 3:
            # 三條
            for triple in HandFinder.find_triples(hand):
                if HandClassifier.can_play(last_play, triple):
                    result.append(triple)
        
        elif last_len == 5:
            # 5張牌型
            for five in HandFinder.find_fives(hand):
                if HandClassifier.can_play(last_play, five):
                    result.append(five)
        
        return result
