import random
from functools import total_ordering

@total_ordering
class Card:
    """資工系專用：大老二撲克牌資料模型 (Phase 1)"""
    SUIT_ICONS = {0: '♣', 1: '♦', 2: '♥', 3: '♠'}
    RANK_LABELS = {10: 'T', 11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: '2'}

    def __init__(self, rank, suit):
        # rank: 3-15 (其中 14=A, 15=2)
        # suit: 0-3 (♣ < ♦ < ♥ < ♠)
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        label = self.RANK_LABELS.get(self.rank, str(self.rank))
        return f"{self.SUIT_ICONS[self.suit]}{label}"

    def __eq__(self, other):
        if not isinstance(other, Card): return False
        return self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        # 為了能放進 set，必須實作 __hash__
        return hash((self.rank, self.suit))

    def __lt__(self, other):
        # 資工系邏輯：利用元組進行優先級比較 (先比數字，數字同則比花色)
        return (self.rank, self.suit) < (other.rank, other.suit)

    def to_sort_key(self):
        """用於排序的鍵值"""
        return (self.rank, self.suit)

class Deck:
    """牌組類別，負責洗牌與發牌"""
    def __init__(self):
        self.cards = [Card(r, s) for r in range(3, 16) for s in range(4)]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        num_to_deal = min(n, len(self.cards))
        dealt = self.cards[:num_to_deal]
        self.cards = self.cards[num_to_deal:]
        return dealt

class Hand(list):
    """手牌類別，繼承自 list 並擴充特定功能"""
    def sort_desc(self):
        # 大老二排法：大的在前 (2 -> A -> ... -> 3)
        self.sort(reverse=True)

    def find_3_clubs(self):
        """尋找開局必備的梅花 3"""
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None

class Player:
    """玩家類別"""
    def __init__(self, name, is_ai=False):
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0

    def take_cards(self, cards):
        self.hand.extend(cards)
        self.hand.sort_desc()
