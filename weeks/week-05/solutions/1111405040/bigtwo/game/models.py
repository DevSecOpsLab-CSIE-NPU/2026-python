"""
遊戲資料模型。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import total_ordering
from random import Random


RANK_LABELS = {
    11: "J",
    12: "Q",
    13: "K",
    14: "A",
    15: "2",
}
SUIT_LABELS = {
    0: "C",
    1: "D",
    2: "H",
    3: "S",
}


@total_ordering
@dataclass(frozen=True)
class Card:
    """單張牌。"""

    rank: int
    suit: int

    def __post_init__(self) -> None:
        if self.rank not in range(3, 16):
            raise ValueError("rank 必須介於 3 到 15 之間。")
        if self.suit not in range(4):
            raise ValueError("suit 必須介於 0 到 3 之間。")

    def __repr__(self) -> str:
        rank = RANK_LABELS.get(self.rank, str(self.rank))
        suit = SUIT_LABELS[self.suit]
        return f"{rank}{suit}"

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self.to_sort_key() < other.to_sort_key()

    def to_sort_key(self) -> tuple[int, int]:
        """回傳排序依據：先比數字，再比花色。"""

        return self.rank, self.suit


class Deck:
    """一副 52 張牌。"""

    def __init__(self, shuffle_on_init: bool = True, seed: int | None = None) -> None:
        self._rng = Random(seed)
        self.cards = self._create_cards()
        if shuffle_on_init:
            self.shuffle()

    @staticmethod
    def _create_cards() -> list[Card]:
        return [Card(rank, suit) for rank in range(3, 16) for suit in range(4)]

    def shuffle(self) -> None:
        self._rng.shuffle(self.cards)

    def deal(self, count: int) -> list[Card]:
        actual = min(count, len(self.cards))
        dealt = self.cards[:actual]
        self.cards = self.cards[actual:]
        return dealt


@dataclass
class Hand:
    """玩家手牌容器。"""

    cards: list[Card] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.cards = list(self.cards)
        self.sort_desc()

    def __iter__(self):
        return iter(self.cards)

    def __len__(self) -> int:
        return len(self.cards)

    def add_cards(self, cards: list[Card]) -> None:
        self.cards.extend(cards)
        self.sort_desc()

    def sort_desc(self) -> None:
        self.cards.sort(key=lambda card: card.to_sort_key(), reverse=True)

    def find_3_clubs(self) -> Card | None:
        for card in self.cards:
            if card.rank == 3 and card.suit == 0:
                return card
        return None

    def has_cards(self, cards: list[Card]) -> bool:
        remaining = list(self.cards)
        for card in cards:
            if card not in remaining:
                return False
            remaining.remove(card)
        return True

    def remove_cards(self, cards: list[Card]) -> bool:
        if not self.has_cards(cards):
            return False

        remaining = list(self.cards)
        for card in cards:
            remaining.remove(card)

        self.cards = remaining
        self.sort_desc()
        return True


@dataclass
class Player:
    """玩家資料。"""

    name: str
    is_ai: bool = False
    hand: Hand = field(default_factory=Hand)
    score: int = 0

    def take_cards(self, cards: list[Card]) -> None:
        self.hand.add_cards(cards)

    def play_cards(self, cards: list[Card]) -> bool:
        return self.hand.remove_cards(cards)
