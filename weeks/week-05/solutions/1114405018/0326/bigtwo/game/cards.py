from __future__ import annotations

from dataclasses import dataclass
from random import shuffle
from typing import List


@dataclass(frozen=True)
class Card:
    suit: int
    rank: int


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = [Card(suit, rank) for suit in range(4) for rank in range(3, 16)]

    def shuffle(self) -> None:
        shuffle(self.cards)

    def deal(self, n: int) -> List[Card]:
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt


class Hand:
    def __init__(self, cards: List[Card] | None = None) -> None:
        self.cards = cards or []

    def add(self, card: Card) -> None:
        self.cards.append(card)


class Player:
    def __init__(self, name: str, hand: Hand | None = None) -> None:
        self.name = name
        self.hand = hand or Hand()
