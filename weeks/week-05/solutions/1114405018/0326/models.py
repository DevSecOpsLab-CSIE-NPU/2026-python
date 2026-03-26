"""
Phase 1: Big Two 資料模型實作

提供以下四個核心類別：
- Card   : 單張牌，含比較、顯示與排序鍵值
- Deck   : 一副 52 張牌，含洗牌與發牌
- Hand   : 玩家手牌容器，含排序、搜尋與移除
- Player : 玩家資料，含拿牌與出牌

此檔案對應 test_p1_models.py 的測試需求。
"""

from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Iterable, Iterator, List


# 花色顯示對照：0=梅花、1=方塊、2=紅心、3=黑桃
SUIT_SYMBOLS = {
    0: "♣",
    1: "♦",
    2: "♥",
    3: "♠",
}

# 點數顯示對照：11=J, 12=Q, 13=K, 14=A, 15=2
RANK_LABELS = {
    11: "J",
    12: "Q",
    13: "K",
    14: "A",
    15: "2",
}


@dataclass(frozen=True)
class Card:
    """單張牌資料模型。"""

    rank: int
    suit: int

    def __post_init__(self) -> None:
        """建立時驗證 rank/suit 範圍。"""
        if self.rank < 3 or self.rank > 15:
            raise ValueError("rank 必須介於 3~15")
        if self.suit < 0 or self.suit > 3:
            raise ValueError("suit 必須介於 0~3")

    def __repr__(self) -> str:
        """回傳例如 ♠A、♣3 這樣的易讀表示。"""
        suit_symbol = SUIT_SYMBOLS[self.suit]
        rank_label = RANK_LABELS.get(self.rank, str(self.rank))
        return f"{suit_symbol}{rank_label}"

    def __gt__(self, other: object) -> bool:
        """定義大於比較：先比 rank，再比 suit。"""
        if not isinstance(other, Card):
            return NotImplemented
        return self.to_sort_key() > other.to_sort_key()

    def to_sort_key(self) -> tuple[int, int]:
        """提供排序鍵值 (rank, suit)。"""
        return (self.rank, self.suit)


class Deck:
    """一副 52 張牌。"""

    def __init__(self) -> None:
        # Big Two 牌點通常由 3 到 2（以數值 3~15 表示）
        # 每個點數 4 種花色，共 13*4 = 52 張
        self.cards: List[Card] = [
            Card(rank, suit)
            for rank in range(3, 16)
            for suit in range(4)
        ]

    def shuffle(self) -> None:
        """原地洗牌。"""
        random.shuffle(self.cards)

    def deal(self, n: int) -> List[Card]:
        """發出前 n 張牌；若 n 超過剩餘數量，則全數發出。"""
        if n <= 0:
            return []
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt


class Hand:
    """手牌容器，提供排序、搜尋、移除與迭代。"""

    def __init__(self, cards: Iterable[Card] | None = None) -> None:
        self.cards: List[Card] = list(cards) if cards is not None else []

    def __iter__(self) -> Iterator[Card]:
        return iter(self.cards)

    def sort_desc(self) -> None:
        """依點數與花色由大到小排序。"""
        self.cards.sort(key=lambda c: c.to_sort_key(), reverse=True)

    def find_3_clubs(self) -> Card | None:
        """找出梅花 3（♣3），若不存在回傳 None。"""
        for card in self.cards:
            if card.rank == 3 and card.suit == 0:
                return card
        return None

    def remove(self, target: Card) -> None:
        """移除指定牌；若不存在則保持不變。"""
        for i, card in enumerate(self.cards):
            if card.rank == target.rank and card.suit == target.suit:
                del self.cards[i]
                return


class Player:
    """玩家資料：名稱、是否 AI、手牌。"""

    def __init__(self, name: str, is_ai: bool) -> None:
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()

    def take_cards(self, cards: Iterable[Card]) -> None:
        """將多張牌加入玩家手牌。"""
        self.hand.cards.extend(cards)

    def play(self, card: Card) -> Card:
        """打出指定牌並回傳該牌；若牌不存在則拋出例外。"""
        for i, c in enumerate(self.hand.cards):
            if c.rank == card.rank and c.suit == card.suit:
                return self.hand.cards.pop(i)
        raise ValueError("玩家手牌中不存在該卡牌")
