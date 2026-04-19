from __future__ import annotations

from dataclasses import dataclass, field
import random
from typing import Iterable, Optional


SUIT_LABELS = ("C", "D", "H", "S")
RANK_LABELS = {
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


@dataclass(frozen=True, order=True)
class Card:
    rank: int
    suit: int

    def __post_init__(self) -> None:
        if self.rank < 3 or self.rank > 15:
            raise ValueError("rank must be in range [3, 15]")
        if self.suit < 0 or self.suit > 3:
            raise ValueError("suit must be in range [0, 3]")

    def to_sort_key(self) -> tuple[int, int]:
        return (self.rank, self.suit)

    def __repr__(self) -> str:
        return f"{SUIT_LABELS[self.suit]}{RANK_LABELS[self.rank]}"


class Deck:
    def __init__(self) -> None:
        self.cards = self._create_cards()

    def _create_cards(self) -> list[Card]:
        cards: list[Card] = []
        for rank in range(3, 16):
            for suit in range(4):
                cards.append(Card(rank, suit))
        return cards

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self, n: int) -> list[Card]:
        if n <= 0:
            return []
        n = min(n, len(self.cards))
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt


@dataclass
class Hand:
    cards: list[Card] = field(default_factory=list)

    def __iter__(self):
        return iter(self.cards)

    def __len__(self) -> int:
        return len(self.cards)

    def __getitem__(self, item: int) -> Card:
        return self.cards[item]

    def extend(self, new_cards: Iterable[Card]) -> None:
        self.cards.extend(new_cards)

    def sort_desc(self) -> None:
        self.cards.sort(key=lambda c: (-c.rank, c.suit))

    def find_3_clubs(self) -> Optional[Card]:
        for card in self.cards:
            if card.rank == 3 and card.suit == 0:
                return card
        return None

    def remove(self, cards_to_remove: Iterable[Card]) -> None:
        for card in cards_to_remove:
            try:
                self.cards.remove(card)
            except ValueError:
                continue


@dataclass
class Player:
    name: str
    is_ai: bool = False
    hand: Hand = field(default_factory=Hand)
    score: int = 0

    def take_cards(self, cards: Iterable[Card]) -> None:
        self.hand.extend(cards)
        self.hand.sort_desc()

    def play_cards(self, cards: list[Card]) -> list[Card]:
        self.hand.remove(cards)
        self.hand.sort_desc()
        return cards
