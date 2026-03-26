"""
Phase 1: 資料模型 - Card、Deck、Hand、Player 類別實現
"""
import random
from typing import List, Optional, Tuple


class Card:
    """撲克牌類別"""
    
    # 花色符號對應
    SUIT_SYMBOLS = {0: '♣', 1: '♦', 2: '♥', 3: '♠'}
    # 點數符號對應
    RANK_SYMBOLS = {3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 
                    8: '8', 9: '9', 10: 'T', 11: 'J', 12: 'Q', 
                    13: 'K', 14: 'A', 15: '2'}
    # 點數順序（用於比較）
    RANK_ORDER = {3: 0, 4: 1, 5: 2, 6: 3, 7: 4, 8: 5, 9: 6, 
                  10: 7, 11: 8, 12: 9, 13: 10, 14: 11, 15: 12}
    
    def __init__(self, rank: int, suit: int):
        """
        初始化撲克牌
        
        Args:
            rank: 點數 (3-15, 其中14=A, 15=2)
            suit: 花色 (0=♣, 1=♦, 2=♥, 3=♠)
        """
        self.rank = rank
        self.suit = suit
    
    def __repr__(self) -> str:
        """回傳卡牌的字符串表示"""
        return f"{self.SUIT_SYMBOLS[self.suit]}{self.RANK_SYMBOLS[self.rank]}"
    
    def __eq__(self, other: 'Card') -> bool:
        """比較兩張牌是否相同"""
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit
    
    def __lt__(self, other: 'Card') -> bool:
        """
        比較牌的大小
        比較邏輯：先比較點數，再比較花色
        """
        if not isinstance(other, Card):
            return NotImplemented
        if self.rank != other.rank:
            return self.RANK_ORDER[self.rank] < self.RANK_ORDER[other.rank]
        return self.suit < other.suit
    
    def __le__(self, other: 'Card') -> bool:
        """小於等於比較"""
        return self == other or self < other
    
    def __gt__(self, other: 'Card') -> bool:
        """大於比較"""
        return not self <= other
    
    def __ge__(self, other: 'Card') -> bool:
        """大於等於比較"""
        return not self < other
    
    def __hash__(self) -> int:
        """計算雜湊值，用於集合和字典"""
        return hash((self.rank, self.suit))
    
    def to_sort_key(self) -> Tuple[int, int]:
        """回傳排序鍵值"""
        return (self.rank, self.suit)


class Deck:
    """撲克牌組類別"""
    
    def __init__(self):
        """初始化牌組，包含52張牌"""
        self.cards: List[Card] = []
        self._create_cards()
    
    def _create_cards(self) -> None:
        """建立52張牌"""
        for suit in range(4):  # 4種花色
            for rank in range(3, 16):  # 3到15點數
                self.cards.append(Card(rank, suit))
    
    def shuffle(self) -> None:
        """洗牌"""
        random.shuffle(self.cards)
    
    def deal(self, n: int) -> List[Card]:
        """
        發n張牌
        
        Args:
            n: 要發的牌數
            
        Returns:
            發出的牌列表（最多n張）
        """
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt


class Hand(list):
    """玩家手牌類別，繼承自 list"""
    
    def __init__(self, cards: Optional[List[Card]] = None):
        """
        初始化手牌
        
        Args:
            cards: 牌列表，若為 None 則為空
        """
        super().__init__(cards if cards else [])
    
    def sort_desc(self) -> None:
        """
        按點數倒序排序，相同點數按花色正序
        排序後：點數高→低，花色強→弱
        """
        self.sort(key=lambda card: (-Card.RANK_ORDER[card.rank], card.suit))
    
    def find_3_clubs(self) -> Optional[Card]:
        """
        查找 3♣（梅花3）
        
        Returns:
            Card: 若找到 3♣ 回傳該牌，否則回傳 None
        """
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None
    
    def remove(self, cards: List[Card]) -> None:
        """
        移除指定的牌
        
        Args:
            cards: 要移除的牌列表
        """
        for card in cards:
            if card in self:
                super().remove(card)


class Player:
    """玩家類別"""
    
    def __init__(self, name: str, is_ai: bool = False):
        """
        初始化玩家
        
        Args:
            name: 玩家名字
            is_ai: 是否為 AI 玩家
        """
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0
    
    def take_cards(self, cards: List[Card]) -> None:
        """
        拿牌到手牌
        
        Args:
            cards: 要拿的牌列表
        """
        self.hand.extend(cards)
    
    def play_cards(self, cards: List[Card]) -> List[Card]:
        """
        出牌
        
        Args:
            cards: 要出的牌列表
            
        Returns:
            實際出牌列表
        """
        self.hand.remove(cards)
        return cards
