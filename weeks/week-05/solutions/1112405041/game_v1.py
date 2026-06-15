import random
from functools import total_ordering

@total_ordering
class Card:
    """
    大老二撲克牌類別
    數字等級：3=3, ..., 10=10, 11=J, 12=Q, 13=K, 14=A, 15=2
    花色等級：0=♣, 1=♦, 2=♥, 3=♠
    """
    SUIT_ICONS = {0: '♣', 1: '♦', 2: '♥', 3: '♠'}
    RANK_LABELS = {11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: '2'}

    def __init__(self, rank: int, suit: int):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        label = self.RANK_LABELS.get(self.rank, str(self.rank))
        if self.rank == 10: label = "T"
        return f"{self.SUIT_ICONS[self.suit]}{label}"

    def __eq__(self, other):
        if not isinstance(other, Card): return False
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.suit < other.suit

class Deck:
    """牌組類別，負責初始化、洗牌與發牌"""
    def __init__(self):
        self.cards = [Card(r, s) for r in range(3, 16) for s in range(4)]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n: int):
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt

class Hand(list):
    """玩家手牌，繼承自 list 並擴充功能"""
    def sort_cards(self):
        # 大老二通常由大到小排，方便玩家看牌
        self.sort(reverse=True)

    def find_3_clubs(self):
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None

class Player:
    """玩家類別"""
    def __init__(self, name: str, is_ai: bool = False):
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()

    def add_to_hand(self, cards):
        self.hand.extend(cards)
        self.hand.sort_cards()

    def __repr__(self):
        return f"玩家 {self.name} | 手牌數: {len(self.hand)}"
