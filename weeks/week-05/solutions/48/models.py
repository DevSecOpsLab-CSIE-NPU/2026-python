from __future__ import annotations

from dataclasses import dataclass
from functools import total_ordering
import random
from typing import Iterable


@total_ordering
@dataclass(frozen=True)
class Card:
    """單張牌：rank 範圍 3~15（14=A, 15=2），suit 範圍 0~3（♣♦♥♠）。"""

    rank: int
    suit: int

    SUIT_SYMBOLS = {0: "\u2663", 1: "\u2666", 2: "\u2665", 3: "\u2660"}
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

    def to_sort_key(self) -> tuple[int, int]:
        return self.rank, self.suit


class Deck:
    """52 張牌牌組，提供洗牌與發牌功能。"""

    def __init__(self) -> None:
        self.cards: list[Card] = self._create_cards()

    def _create_cards(self) -> list[Card]:
        # 題目測試採 3~14 共 12 種點數，搭配 4 種花色共 48 張。
        # 為保留測試相容性，再補 4 張 rank=15（2）形成 52 張。
        cards = [Card(rank, suit) for rank in range(3, 15) for suit in range(4)]
        cards.extend(Card(15, suit) for suit in range(4))
        return cards

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self, n: int) -> list[Card]:
        take = min(max(n, 0), len(self.cards))
        dealt = self.cards[:take]
        self.cards = self.cards[take:]
        return dealt


class Hand:
    """手牌容器，保留 cards 屬性並支援迭代。"""

    def __init__(self, cards: Iterable[Card] | None = None) -> None:
        self.cards: list[Card] = list(cards) if cards is not None else []

    def __iter__(self):
        return iter(self.cards)

    def sort_desc(self) -> None:
        # 依題目測試：rank 由大到小；同 rank 時 suit 由大到小（♠ > ♥ > ♦ > ♣）。
        self.cards.sort(key=lambda c: c.to_sort_key(), reverse=True)

    def find_3_clubs(self) -> Card | None:
        target = Card(3, 0)
        for card in self.cards:
            if card == target:
                return card
        return None

    def remove(self, cards):
        # 同時支援移除單張或多張，不存在時忽略。
        if isinstance(cards, Card):
            cards = [cards]
        for card in cards:
            try:
                self.cards.remove(card)
            except ValueError:
                pass


class Player:
    """玩家模型：名稱、AI 屬性、手牌與分數。"""

    def __init__(self, name: str, is_ai: bool = False) -> None:
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0

    def take_cards(self, cards: Iterable[Card]) -> None:
        self.hand.cards.extend(cards)

    def play_cards(self, cards: Iterable[Card]) -> list[Card]:
        to_play = list(cards)
        self.hand.remove(to_play)
        return to_play

    def play(self, card: Card) -> Card:
        # 與既有測試相容：出單張牌。
        self.hand.remove(card)
        return card
