"""Phase 1: Data models - Card, Deck, Hand, Player."""

from typing import Optional, List
import random


class Card:
    """單張牌牌的資料模型。"""

    RANK_NAMES = {3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
                   9: '9', 10: 'T', 11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: '2'}
    SUIT_SYMBOLS = {0: '♣', 1: '♦', 2: '♥', 3: '♠'}
    SUIT_NAMES = {0: 'clubs', 1: 'diamonds', 2: 'hearts', 3: 'spades'}

    def __init__(self, rank: int, suit: int) -> None:
        """初始化牌。
        
        Args:
            rank: 牌的數字 (3-14: 3-A, 15: 2)
            suit: 花色 (0: ♣, 1: ♦, 2: ♥, 3: ♠)
        """
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        """回傳牌的字串表示，格式: ♠A。"""
        return f"{self.SUIT_SYMBOLS[self.suit]}{self.RANK_NAMES[self.rank]}"

    def __eq__(self, other: object) -> bool:
        """比較是否相同。"""
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other: 'Card') -> bool:
        """比較大小 (先比rank再比suit)。"""
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.suit < other.suit

    def __le__(self, other: 'Card') -> bool:
        """小於等於。"""
        return self == other or self < other

    def __gt__(self, other: 'Card') -> bool:
        """大於。"""
        return not (self <= other)

    def __ge__(self, other: 'Card') -> bool:
        """大於等於。"""
        return not (self < other)

    def __hash__(self) -> int:
        """雜湊值，用於set和dict。"""
        return hash((self.rank, self.suit))

    def to_sort_key(self) -> tuple[int, int]:
        """回傳排序鍵。"""
        return (self.rank, self.suit)


class Deck:
    """牌堆。"""

    def __init__(self) -> None:
        """初始化含52張牌的牌堆。"""
        self.cards: List[Card] = self._create_cards()

    def _create_cards(self) -> List[Card]:
        """建立52張牌組。"""
        cards: List[Card] = []
        for suit in range(4):
            for rank in range(3, 16):
                cards.append(Card(rank, suit))
        return cards

    def shuffle(self) -> None:
        """洗牌。"""
        random.shuffle(self.cards)

    def deal(self, n: int) -> List[Card]:
        """發n張牌。
        
        Args:
            n: 發牌數量
            
        Returns:
            發出的牌列表
        """
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt


class Hand(list):
    """玩家手牌，繼承自 list。"""

    def __init__(self, cards: Optional[List[Card]] = None) -> None:
        """初始化手牌。
        
        Args:
            cards: 初始牌組
        """
        super().__init__(cards or [])

    def sort_desc(self) -> None:
        """倒序排列 (rank倒序, suit正序)。"""
        super().sort(key=lambda card: (-card.rank, card.suit))

    def find_3_clubs(self) -> Optional[Card]:
        """查找3♣。
        
        Returns:
            3♣ Card 或 None
        """
        target = Card(3, 0)
        for card in self:
            if card == target:
                return card
        return None

    def remove(self, cards: List[Card]) -> None:
        """移除指定的牌。
        
        Args:
            cards: 要移除的牌列表
        """
        for card in cards:
            if card in self:
                super().remove(card)


class Player:
    """玩家。"""

    def __init__(self, name: str, is_ai: bool = False) -> None:
        """初始化玩家。
        
        Args:
            name: 玩家名稱
            is_ai: 是否為AI
        """
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0

    def take_cards(self, cards: List[Card]) -> None:
        """拿牌到手牌。
        
        Args:
            cards: 要拿的牌列表
        """
        self.hand.extend(cards)

    def play_cards(self, cards: List[Card]) -> List[Card]:
        """出牌。
        
        Args:
            cards: 要出的牌
            
        Returns:
            出牌列表
        """
        self.hand.remove(cards)
        return cards
