"""Phase 1: 大老二資料模型。"""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Iterable, List, Optional, Tuple


@dataclass(frozen=True)
class Card:
    """單張撲克牌。"""

    rank: int
    suit: int

    SUIT_SYMBOLS = {0: "♣", 1: "♦", 2: "♥", 3: "♠"}
    RANK_SYMBOLS = {
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

    def __repr__(self) -> str:
        return f"{self.SUIT_SYMBOLS[self.suit]}{self.RANK_SYMBOLS[self.rank]}"

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self.to_sort_key() < other.to_sort_key()

    def to_sort_key(self) -> Tuple[int, int]:
        # 先比點數，再比花色
        return (self.rank, self.suit)


class Deck:
    """52 張標準撲克牌牌堆。"""

    def __init__(self) -> None:
        self.cards: List[Card] = self._create_cards()

    def _create_cards(self) -> List[Card]:
        cards: List[Card] = []
        for rank in range(3, 16):
            for suit in range(4):
                cards.append(Card(rank=rank, suit=suit))
        return cards

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self, n: int) -> List[Card]:
        # 超過剩餘牌數時，回傳所有剩餘牌
        n = min(n, len(self.cards))
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt


class Hand(list):
    """玩家手牌，繼承 list 方便迭代與索引。"""

    def __init__(self, cards: Optional[Iterable[Card]] = None) -> None:
        super().__init__(cards or [])

    def sort_desc(self) -> None:
        # 依需求：rank 倒序、suit 倒序（♠ > ♥ > ♦ > ♣）
        self.sort(key=lambda c: c.to_sort_key(), reverse=True)

    def find_3_clubs(self) -> Optional[Card]:
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None

    def remove(self, cards) -> None:  # type: ignore[override]
        # 支援移除單張或多張，不存在則略過
        if isinstance(cards, Card):
            cards_to_remove = [cards]
        else:
            cards_to_remove = list(cards)

        for card in cards_to_remove:
            if card in self:
                super().remove(card)


class Player:
    """玩家資料與操作。"""

    def __init__(self, name: str, is_ai: bool = False) -> None:
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0

    def take_cards(self, cards: Iterable[Card]) -> None:
        self.hand.extend(cards)

    def play_cards(self, cards: Iterable[Card]) -> List[Card]:
        cards_list = list(cards)
        self.hand.remove(cards_list)
        return cards_list
