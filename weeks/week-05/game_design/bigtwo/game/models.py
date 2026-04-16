"""Big Two Card Game - Data Models"""

from typing import List, Optional
import random


class Card:
    SUITS = ["♣", "♦", "♥", "♠"]
    SUIT_SYMBOLS = {0: "♣", 1: "♦", 2: "♥", 3: "♠"}
    RANK_SYMBOLS = {
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "T",
        11: "J",
        12: "Q",
        13: "K",
        14: "A",
        15: "2",
    }
    RANK_NAMES = {
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "J",
        12: "Q",
        13: "K",
        14: "A",
        15: "2",
    }

    def __init__(self, rank: int, suit: int):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f"{self.SUIT_SYMBOLS[self.suit]}{self.RANK_SYMBOLS[self.rank]}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other) -> bool:
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.suit < other.suit

    def __hash__(self) -> int:
        return hash((self.rank, self.suit))

    def to_sort_key(self) -> tuple:
        return (self.rank, self.suit)


class Deck:
    def __init__(self):
        self.cards: List[Card] = self._create_cards()

    def _create_cards(self) -> List[Card]:
        cards = []
        for suit in range(4):
            for rank in range(3, 16):
                cards.append(Card(rank, suit))
        return cards

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self, n: int) -> List[Card]:
        if n > len(self.cards):
            n = len(self.cards)
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt


class Hand(list):
    def __init__(self, cards: Optional[List[Card]] = None):
        super().__init__(cards if cards else [])

    def sort_desc(self) -> None:
        self.sort(key=lambda c: (-c.rank, -c.suit))

    def find_3_clubs(self) -> Optional[Card]:
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None

    def remove(self, cards) -> None:
        if isinstance(cards, list):
            for card in cards:
                if card in self:
                    super().remove(card)
        else:
            if cards in self:
                super().remove(cards)


class Player:
    def __init__(self, name: str, is_ai: bool = False, position: int = 0):
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0
        self.position = position
        self.cards_played = []

    def take_cards(self, cards) -> None:
        self.hand.extend(cards)

    def play_cards(self, cards) -> None:
        self.hand.remove(cards)
