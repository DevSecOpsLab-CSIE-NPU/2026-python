# p1_models.py
# Phase 1：大老二資料模型實作
#
# 請依照 p1-dev.md 的類別設計，逐一填入以下 TODO 區塊。
# 完成後執行：
#   cd D:\python-0326\2026-python\weeks\week-05\solutions\1114405029
#   python p1-models-unit-test.py
#
# 花色編碼：0=♣  1=♦  2=♥  3=♠
# 點數編碼：3–9 照字面，T=10, J=11, Q=12, K=13, A=14, 2=15
# 大小順序：2 > A > K > Q > J > T > 9 > 8 > 7 > 6 > 5 > 4 > 3
# 花色順序：♠ > ♥ > ♦ > ♣

from __future__ import annotations
import random
from typing import List, Optional


# =========================================================
# Card 類別
# =========================================================
class Card:
    # 花色符號，索引對應 suit 編碼（0–3）
    SUITS = ["♣", "♦", "♥", "♠"]
    # 點數符號，索引 0–2 為佔位，從 3 開始有效；15 代表 2
    RANKS = ["", "", "", "3", "4", "5", "6", "7",
             "8", "9", "T", "J", "Q", "K", "A", "2"]

    def __init__(self, rank: int, suit: int) -> None:
        # 依規格直接儲存點數與花色編碼。
        # rank: 3~15（15 代表 2）
        # suit: 0~3（0=♣, 1=♦, 2=♥, 3=♠）
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        # 依題目需求回傳像「♠A」、「♣3」的可讀字串。
        # 花色符號放前面，點數符號放後面。
        return f"{self.SUITS[self.suit]}{self.RANKS[self.rank]}"

    def __eq__(self, other: object) -> bool:
        # 只有在 other 也是 Card，且 rank 與 suit 都一致時才算相等。
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other: Card) -> bool:
        # 比較規則：先比點數，再比花色。
        # 這會讓 Python 的排序/比較運算都符合大老二的牌力定義。
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.suit < other.suit

    def __hash__(self) -> int:
        # 與 __eq__ 一致：同 rank/suit 的牌必須有相同 hash。
        return hash((self.rank, self.suit))

    def to_sort_key(self) -> tuple[int, int]:
        # 提供明確排序鍵，方便外部需要時直接使用。
        return (self.rank, self.suit)


# =========================================================
# Deck 類別
# =========================================================
class Deck:
    def __init__(self) -> None:
        # 初始化時建立完整 52 張牌。
        self.cards: List[Card] = self._create_cards()

    def _create_cards(self) -> List[Card]:
        # 依規格建立 rank 3~15、suit 0~3 的所有組合，共 52 張。
        cards: List[Card] = []
        for rank in range(3, 16):
            for suit in range(4):
                cards.append(Card(rank, suit))
        return cards

    def shuffle(self) -> None:
        # 原地洗牌，不建立新清單。
        random.shuffle(self.cards)

    def deal(self, n: int) -> List[Card]:
        # 從牌堆前面發牌：先切出要發的區段，再同步移除。
        # 若 n 大於剩餘張數，Python 切片會自然回傳全部剩餘牌。
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt


# =========================================================
# Hand 類別（繼承 list）
# =========================================================
class Hand(list):
    def __init__(self, cards: Optional[List[Card]] = None) -> None:
        # 若未提供 cards，就建立空 list；否則以既有牌列表初始化。
        if cards is None:
            super().__init__()
        else:
            super().__init__(cards)

    def sort_desc(self) -> None:
        # 大老二排序規則：
        # 1) rank 由大到小
        # 2) rank 相同時，suit 由大到小（♠ > ♥ > ♦ > ♣）
        self.sort(key=lambda card: (card.rank, card.suit), reverse=True)

    def find_3_clubs(self) -> Optional[Card]:
        # 掃描手牌，找到 3♣（rank=3, suit=0）立即回傳。
        # 若找不到就回傳 None。
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None

    def remove(self, cards: List[Card]) -> None:  # type: ignore[override]
        # 逐張移除指定的牌。
        # 若某張牌不存在，依規格靜默忽略，不拋出例外。
        for card in cards:
            try:
                super().remove(card)
            except ValueError:
                # 不存在就忽略，保持程式流程穩定。
                continue


# =========================================================
# Player 類別
# =========================================================
class Player:
    def __init__(self, name: str, is_ai: bool = False) -> None:
        # 玩家基本資料：名稱、是否為 AI、手牌、分數。
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0

    def take_cards(self, cards: List[Card]) -> None:
        # 將新牌加入手牌尾端；是累加，不是覆蓋。
        self.hand.extend(cards)

    def play_cards(self, cards: List[Card]) -> List[Card]:
        # 先從手牌移除要出的牌，再回傳這次出的牌列表。
        self.hand.remove(cards)
        return cards
