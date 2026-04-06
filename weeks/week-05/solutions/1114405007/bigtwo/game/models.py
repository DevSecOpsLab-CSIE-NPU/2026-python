from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Iterable, Optional


RANK_TO_TEXT = {
    11: "J",
    12: "Q",
    13: "K",
    14: "A",
    15: "2",
}
SUIT_TO_TEXT = {
    0: "♣",
    1: "♦",
    2: "♥",
    3: "♠",
}


@dataclass(frozen=True, order=False)
class Card:
    rank: int
    suit: int

    def __post_init__(self) -> None:
        if not (3 <= self.rank <= 15):
            raise ValueError("rank must be in [3, 15]")
        if self.suit not in (0, 1, 2, 3):
            raise ValueError("suit must be in [0, 3]")

    def __repr__(self) -> str:
        rank_text = RANK_TO_TEXT.get(self.rank, str(self.rank))
        suit_text = SUIT_TO_TEXT[self.suit]
        return f"{suit_text}{rank_text}"

    def to_sort_key(self) -> tuple[int, int]:
        return self.rank, self.suit

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self.to_sort_key() < other.to_sort_key()


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
        count = min(n, len(self.cards))
        dealt = self.cards[:count]
        self.cards = self.cards[count:]
        return dealt


class Hand(list[Card]):
    def __init__(self, cards: Optional[Iterable[Card]] = None):
        super().__init__(cards or [])

    def sort_desc(self) -> None:
        self.sort(key=lambda c: (-c.rank, c.suit))

    def find_3_clubs(self) -> Optional[Card]:
        target = Card(3, 0)
        for card in self:
            if card == target:
                return card
        return None

    def remove_cards(self, cards: Iterable[Card]) -> None:
        for card in cards:
            try:
                super().remove(card)
            except ValueError:
                # Ignore missing cards so caller can safely submit mixed sets.
                continue

    def remove(self, cards):  # type: ignore[override]
        if isinstance(cards, Card):
            return super().remove(cards)
        self.remove_cards(cards)
        return None


class Player:
    def __init__(self, name: str, is_ai: bool = False) -> None:
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0

    def take_cards(self, cards: Iterable[Card]) -> None:
        self.hand.extend(cards)

    def play_cards(self, cards: list[Card]) -> list[Card]:
        self.hand.remove_cards(cards)
        return list(cards)
