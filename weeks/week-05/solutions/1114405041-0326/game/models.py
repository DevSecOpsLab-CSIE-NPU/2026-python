"""Phase 1 資料模型（標準版）。

本檔實作 Card、Deck、Hand、Player 四個核心類別，
並以清楚的型別註記與繁體中文註解說明每個步驟。
"""

from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Iterable


@dataclass(frozen=True, order=False)
class Card:
    """一張撲克牌。

    rank: 3~15（11=J, 12=Q, 13=K, 14=A, 15=2）
    suit: 0~3（0=♣, 1=♦, 2=♥, 3=♠）
    """

    rank: int
    suit: int

    # 使用類別屬性管理顯示字元，避免魔法字串散落程式中。
    SUIT_SYMBOLS = ("♣", "♦", "♥", "♠")
    RANK_LABELS = {
        11: "J",
        12: "Q",
        13: "K",
        14: "A",
        15: "2",
    }

    def __post_init__(self) -> None:
        # 嚴格檢查輸入範圍，讓錯誤早點被發現。
        if not (3 <= self.rank <= 15):
            raise ValueError(f"rank 必須介於 3~15，收到: {self.rank}")
        if not (0 <= self.suit <= 3):
            raise ValueError(f"suit 必須介於 0~3，收到: {self.suit}")

    def __repr__(self) -> str:
        # 先把數字 rank 轉成顯示字串，再組成花色+點數的可讀格式。
        rank_text = self.RANK_LABELS.get(self.rank, str(self.rank))
        return f"{self.SUIT_SYMBOLS[self.suit]}{rank_text}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)

    def __lt__(self, other: Card) -> bool:
        # 先比 rank，再比 suit；可自然支援 >, <= 等比較。
        return self.to_sort_key() < other.to_sort_key()

    def __hash__(self) -> int:
        return hash((self.rank, self.suit))

    def to_sort_key(self) -> tuple[int, int]:
        return (self.rank, self.suit)


class Deck:
    """一副 52 張牌。"""

    def __init__(self) -> None:
        self.cards: list[Card] = self._create_cards()

    def _create_cards(self) -> list[Card]:
        # 大老二使用 3..15 共 13 種點數，每個點數 4 種花色。
        return [Card(rank, suit) for rank in range(3, 16) for suit in range(4)]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self, n: int) -> list[Card]:
        # 若 n 超過剩餘牌數，直接發出所有剩餘牌，避免丟例外。
        n = max(0, n)
        actual = min(n, len(self.cards))
        dealt = self.cards[:actual]
        self.cards = self.cards[actual:]
        return dealt


class Hand(list[Card]):
    """手牌容器，繼承 list 以沿用迭代、索引等操作。"""

    def __init__(self, cards: Iterable[Card] | None = None):
        super().__init__(cards or [])

    def sort_desc(self) -> None:
        # 需求是 rank 倒序、suit 正序。
        self.sort(key=lambda c: (-c.rank, c.suit))

    def find_3_clubs(self) -> Card | None:
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None

    def remove(self, cards):  # type: ignore[override]
        # 需求介面為 remove(cards)。
        # 若傳入單張 Card，沿用 list.remove 行為；若傳入可迭代，做批次移除。
        if isinstance(cards, Card):
            super().remove(cards)
            return
        for card in cards:
            if card in self:
                super().remove(card)


class Player:
    """玩家資料模型。"""

    def __init__(self, name: str, is_ai: bool = False):
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0

    def take_cards(self, cards: Iterable[Card]) -> None:
        self.hand.extend(cards)

    def play_cards(self, cards: Iterable[Card]) -> list[Card]:
        # 僅回傳且移除「實際存在於手牌」的牌，避免資料不一致。
        played: list[Card] = []
        for card in cards:
            if card in self.hand:
                self.hand.remove(card)
                played.append(card)
        return played
