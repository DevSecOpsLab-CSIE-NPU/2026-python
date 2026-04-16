"""Phase 1 資料模型（-easy 簡化記憶版）。

這版特別追求「容易記、容易寫」：
- 比較規則都用同一個 key = (rank, suit)
- 牌組建立用雙層迴圈一眼看懂
- 手牌排序用單行 key
"""

from __future__ import annotations

import random


class Card:
    # 類別常數：花色與特殊點數顯示
    SUITS = ["♣", "♦", "♥", "♠"]
    FACE = {11: "J", 12: "Q", 13: "K", 14: "A", 15: "2"}

    def __init__(self, rank: int, suit: int):
        # 先做簡單範圍檢查，錯誤輸入立刻報錯。
        if rank < 3 or rank > 15:
            raise ValueError("rank 必須在 3~15")
        if suit < 0 or suit > 3:
            raise ValueError("suit 必須在 0~3")
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        # 沒有在 FACE 裡的點數直接顯示數字。
        return f"{self.SUITS[self.suit]}{self.FACE.get(self.rank, self.rank)}"

    def key(self) -> tuple[int, int]:
        return (self.rank, self.suit)

    def to_sort_key(self) -> tuple[int, int]:
        return self.key()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self.key() == other.key()

    def __lt__(self, other: Card) -> bool:
        return self.key() < other.key()

    def __hash__(self) -> int:
        return hash(self.key())


class Deck:
    def __init__(self):
        self.cards: list[Card] = []
        for rank in range(3, 16):
            for suit in range(4):
                self.cards.append(Card(rank, suit))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self, n: int) -> list[Card]:
        if n <= 0:
            return []
        n = min(n, len(self.cards))
        result = self.cards[:n]
        self.cards = self.cards[n:]
        return result


class Hand(list[Card]):
    def __init__(self, cards=None):
        super().__init__(cards or [])

    def sort_desc(self) -> None:
        # 記憶口訣：大的先（-rank），同點數小花色先（suit）。
        self.sort(key=lambda c: (-c.rank, c.suit))

    def find_3_clubs(self):
        for c in self:
            if c.rank == 3 and c.suit == 0:
                return c
        return None

    def remove(self, cards):  # type: ignore[override]
        if isinstance(cards, Card):
            super().remove(cards)
            return
        for c in cards:
            if c in self:
                super().remove(c)


class Player:
    def __init__(self, name: str, is_ai: bool = False):
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0

    def take_cards(self, cards) -> None:
        self.hand.extend(cards)

    def play_cards(self, cards):
        played = []
        for c in cards:
            if c in self.hand:
                self.hand.remove(c)
                played.append(c)
        return played
