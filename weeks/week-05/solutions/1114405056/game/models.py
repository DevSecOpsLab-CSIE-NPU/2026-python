import random
from typing import List, Optional

SUIT_SYMBOLS = ['♣', '♦', '♥', '♠']
RANK_SYMBOLS = {
    3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'T',
    11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: '2'
}


class Card:
    def __init__(self, rank: int, suit: int):
        self.rank = rank   # 3-14 = 3-A, 15 = 2
        self.suit = suit   # 0=♣, 1=♦, 2=♥, 3=♠

    def __repr__(self) -> str:
        return SUIT_SYMBOLS[self.suit] + RANK_SYMBOLS[self.rank]

    def __eq__(self, other) -> bool:
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other) -> bool:
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.suit < other.suit

    def __gt__(self, other) -> bool:
        return other < self

    def __le__(self, other) -> bool:
        return self == other or self < other

    def __ge__(self, other) -> bool:
        return self == other or self > other

    def __hash__(self) -> int:
        return hash((self.rank, self.suit))

    def to_sort_key(self):
        return (self.rank, self.suit)


class Deck:
    def __init__(self):
        self.cards: List[Card] = self._create_cards()

    def _create_cards(self) -> List[Card]:
        cards = []
        for rank in list(range(3, 15)) + [15]:
            for suit in range(4):
                cards.append(Card(rank, suit))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n: int) -> List[Card]:
        n = min(n, len(self.cards))
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt


class Hand(list):
    def __init__(self, cards=None):
        super().__init__(cards or [])

    def sort_desc(self):
        self.sort(key=lambda c: (c.rank, c.suit), reverse=True)

    def find_3_clubs(self) -> Optional[Card]:
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None

    def remove(self, cards):
        for card in cards:
            for i, c in enumerate(self):
                if c == card:
                    del self[i]
                    break


class Player:
    def __init__(self, name: str, is_ai: bool = False):
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0

    def take_cards(self, cards: List[Card]):
        self.hand.extend(cards)

    def play_cards(self, cards: List[Card]) -> List[Card]:
        self.hand.remove(cards)
        return cards
