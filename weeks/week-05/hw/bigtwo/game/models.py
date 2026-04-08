"""
Phase 1: 資料模型
Card, Deck, Hand, Player 類別實作
"""

from typing import List, Optional, Tuple
import random


class Card:
    """撲克牌類別"""
    
    # 花色符號對應
    SUIT_SYMBOLS = {0: '♣', 1: '♦', 2: '♥', 3: '♠'}
    # 數字符號對應
    RANK_SYMBOLS = {
        3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'T',
        11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: '2'
    }
    
    def __init__(self, rank: int, suit: int):
        """
        初始化牌
        :param rank: 牌的大小 (3-15, 其中14=A, 15=2)
        :param suit: 花色 (0=♣, 1=♦, 2=♥, 3=♠)
        """
        self.rank = rank
        self.suit = suit
    
    def __repr__(self) -> str:
        """回傳牌的字串表示 e.g., "♠A" """
        suit_symbol = self.SUIT_SYMBOLS[self.suit]
        rank_symbol = self.RANK_SYMBOLS[self.rank]
        return f"{suit_symbol}{rank_symbol}"
    
    def __eq__(self, other) -> bool:
        """比較牌是否相等"""
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit
    
    def __lt__(self, other) -> bool:
        """比較牌大小 (先比rank再比suit)"""
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.suit < other.suit
    
    def __le__(self, other) -> bool:
        return self < other or self == other
    
    def __gt__(self, other) -> bool:
        return not self <= other
    
    def __ge__(self, other) -> bool:
        return not self < other
    
    def __hash__(self) -> int:
        """使牌可以加入集合或字典"""
        return hash((self.rank, self.suit))
    
    def to_sort_key(self) -> Tuple[int, int]:
        """回傳排序用的鍵 (rank, suit)"""
        return (self.rank, self.suit)


class Deck:
    """牌堆類別"""
    
    def __init__(self):
        """初始化52張牌"""
        self.cards = self._create_cards()
    
    def _create_cards(self) -> List[Card]:
        """建立52張牌"""
        cards = []
        for rank in range(3, 16):  # 3 to 15
            for suit in range(4):  # 0 to 3
                cards.append(Card(rank, suit))
        return cards
    
    def shuffle(self) -> None:
        """洗牌"""
        random.shuffle(self.cards)
    
    def deal(self, n: int) -> List[Card]:
        """
        發n張牌，如果不足n張則全部發出
        :param n: 要發的牌數
        :return: 發出的牌列表
        """
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt


class Hand(list):
    """玩家手牌類別，繼承 list"""
    
    def __init__(self, cards: Optional[List[Card]] = None):
        """初始化手牌"""
        if cards is None:
            cards = []
        super().__init__(cards)
    
    def sort_desc(self) -> None:
        """
        按大小排序（rank倒序, suit正序）
        排序時 rank 大的在前，rank 相同時 suit 大的在前
        """
        self.sort(key=lambda c: (-c.rank, -c.suit))
    
    def find_3_clubs(self) -> Optional[Card]:
        """找3♣ (rank=3, suit=0)，回傳Card或None"""
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None
    
    def remove_cards(self, cards: List[Card]) -> None:
        """移除指定的牌"""
        for card in cards:
            if card in self:
                self.remove(card)


class Player:
    """玩家類別"""
    
    def __init__(self, name: str, is_ai: bool = False):
        """
        初始化玩家
        :param name: 玩家名稱
        :param is_ai: 是否為 AI
        """
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0
    
    def take_cards(self, cards: List[Card]) -> None:
        """拿牌到手牌"""
        self.hand.extend(cards)
    
    def play_cards(self, cards: List[Card]) -> List[Card]:
        """
        出牌，從手牌移除並回傳
        :param cards: 要出的牌
        :return: 出牌列表
        """
        self.hand.remove_cards(cards)
        return cards
    
    def __repr__(self) -> str:
        """玩家的字串表示"""
        player_type = "(AI)" if self.is_ai else "(Human)"
        return f"{self.name}{player_type}"
