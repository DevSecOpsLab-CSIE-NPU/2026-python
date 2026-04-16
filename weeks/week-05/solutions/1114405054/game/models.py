"""Phase 1: Big Two 資料模型實作。"""

from __future__ import annotations

from dataclasses import dataclass
from functools import total_ordering
import random


@total_ordering
@dataclass(frozen=True)
class Card:
    """表示一張撲克牌，先比數字再比花色。"""

    rank: int
    suit: int

    SUIT_SYMBOLS = ("♣", "♦", "♥", "♠")
    RANK_LABELS = {
        11: "J",
        12: "Q",
        13: "K",
        14: "A",
        15: "2",
    }

    def __post_init__(self) -> None:
        if not 3 <= self.rank <= 15:
            raise ValueError("rank 必須介於 3 到 15 之間")
        if not 0 <= self.suit <= 3:
            raise ValueError("suit 必須介於 0 到 3 之間")

    def __repr__(self) -> str:
        rank_text = self.RANK_LABELS.get(self.rank, str(self.rank))
        return f"{self.SUIT_SYMBOLS[self.suit]}{rank_text}"

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self.to_sort_key() < other.to_sort_key()

    def to_sort_key(self) -> tuple[int, int]:
        return (self.rank, self.suit)


class Deck:
    """表示一副 52 張牌的牌組。"""

    def __init__(self) -> None:
        self.cards = self._create_cards()

    def _create_cards(self) -> list[Card]:
        return [Card(rank, suit) for rank in range(3, 16) for suit in range(4)]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self, n: int) -> list[Card]:
        actual = min(max(n, 0), len(self.cards))
        dealt = self.cards[:actual]
        del self.cards[:actual]
        return dealt


class Hand(list[Card]):
    """表示玩家手上的牌，沿用 list 操作並補上常用方法。"""

    def __init__(self, cards: list[Card] | None = None) -> None:
        super().__init__(cards or [])

    def sort_desc(self) -> None:
        self.sort(key=lambda card: card.to_sort_key(), reverse=True)

    def find_3_clubs(self) -> Card | None:
        target = Card(3, 0)
        for card in self:
            if card == target:
                return card
        return None

    def remove(self, cards) -> None:  # type: ignore[override]
        for card in cards:
            try:
                super().remove(card)
            except ValueError:
                pass


class Player:
    """表示一位玩家，包含手牌、名稱與 AI 身分。"""

    def __init__(self, name: str, is_ai: bool = False) -> None:
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0

    def take_cards(self, cards: list[Card]) -> None:
        self.hand.extend(cards)

    def play_cards(self, cards: list[Card]) -> list[Card]:
        self.hand.remove(cards)
        return list(cards)
