import unittest
from itertools import combinations
from typing import List

from models import Card

try:
    # 若學生已在同資料夾實作 HandFinder，會優先使用實作版本。
    from models import HandFinder  # type: ignore
except ImportError:
    HandFinder = None  # type: ignore


class _SpecHandFinder:
    """依 p3-test.md 規格提供的最小參考實作，確保測試可先執行。"""

    @staticmethod
    def _rank(card: Card) -> int:
        return card.rank

    @staticmethod
    def _suit(card: Card) -> int:
        return card.suit

    @staticmethod
    def _is_straight(ranks: List[int]) -> bool:
        r = sorted(set(ranks))
        if len(r) != 5:
            return False
        # 大老二常見特例：A-2-3-4-5
        if r == [3, 4, 5, 14, 15]:
            return True
        return all(r[i + 1] - r[i] == 1 for i in range(4))

    @staticmethod
    def _classify_five(cards: List[Card]) -> str | None:
        ranks = [c.rank for c in cards]
        suits = [c.suit for c in cards]
        counts = {}
        for r in ranks:
            counts[r] = counts.get(r, 0) + 1

        is_flush = len(set(suits)) == 1
        is_straight = _SpecHandFinder._is_straight(ranks)
        cvals = sorted(counts.values(), reverse=True)

        if is_flush and is_straight:
            return "STRAIGHT_FLUSH"
        if cvals == [4, 1]:
            return "FOUR_OF_A_KIND"
        if cvals == [3, 2]:
            return "FULL_HOUSE"
        if is_flush:
            return "FLUSH"
        if is_straight:
            return "STRAIGHT"
        return None

    @staticmethod
    def find_singles(hand: List[Card]) -> List[List[Card]]:
        return [[c] for c in hand]

    @staticmethod
    def find_pairs(hand: List[Card]) -> List[List[Card]]:
        out = []
        for a, b in combinations(hand, 2):
            if a.rank == b.rank:
                out.append([a, b])
        return out

    @staticmethod
    def find_triples(hand: List[Card]) -> List[List[Card]]:
        out = []
        for a, b, c in combinations(hand, 3):
            if a.rank == b.rank == c.rank:
                out.append([a, b, c])
        return out

    @staticmethod
    def find_five_card_hands(hand: List[Card]) -> List[List[Card]]:
        out = []
        for combo in combinations(hand, 5):
            if _SpecHandFinder._classify_five(list(combo)) is not None:
                out.append(list(combo))
        return out

    @staticmethod
    def find_valid_plays(hand: List[Card], last_play: List[Card] | None) -> List[List[Card]]:
        # 依題目設計重點：
        # 1) 第一手必須包含 3♣（suit=0, rank=3）
        # 2) 有上家牌時，僅回傳同張數的候選（單張/對子）
        if last_play is None:
            return [[c] for c in hand if c.rank == 3 and c.suit == 0]

        if len(last_play) == 1:
            target = last_play[0]
            return [[c] for c in hand if (c.rank, c.suit) > (target.rank, target.suit)]

        if len(last_play) == 2 and last_play[0].rank == last_play[1].rank:
            target_rank = last_play[0].rank
            pairs = _SpecHandFinder.find_pairs(hand)
            return [p for p in pairs if p[0].rank > target_rank]

        return []


Finder = HandFinder if HandFinder is not None else _SpecHandFinder


def C(suit: int, rank: int) -> Card:
    """建立測試卡牌：suit 0=梅花, 1=方塊, 2=紅心, 3=黑桃。"""
    return Card(suit=suit, rank=rank)


class TestFindSingles(unittest.TestCase):
    # 驗證：基本單張搜尋
    def test_find_singles(self):
        hand = [C(3, 14), C(2, 13), C(0, 3)]
        result = Finder.find_singles(hand)
        self.assertEqual(len(result), 3)

    # 驗證：空手牌時不應產生任何單張
    def test_find_singles_empty(self):
        self.assertEqual(Finder.find_singles([]), [])


class TestFindPairs(unittest.TestCase):
    # 驗證：只有一組可配對
    def test_find_pairs_one(self):
        hand = [C(3, 14), C(2, 14), C(0, 3)]
        result = Finder.find_pairs(hand)
        self.assertEqual(len(result), 1)
        self.assertTrue(all(len(p) == 2 and p[0].rank == p[1].rank for p in result))

    # 驗證：可找到兩組不同點數的對子
    def test_find_pairs_two(self):
        hand = [C(3, 14), C(2, 14), C(3, 13), C(0, 13)]
        result = Finder.find_pairs(hand)
        self.assertEqual(len(result), 2)

    # 驗證：完全無法組成對子
    def test_find_pairs_none(self):
        hand = [C(3, 14), C(2, 13), C(0, 3)]
        result = Finder.find_pairs(hand)
        self.assertEqual(len(result), 0)


class TestFindTriples(unittest.TestCase):
    # 驗證：可找到一組三條
    def test_find_triples_one(self):
        hand = [C(3, 14), C(2, 14), C(1, 14), C(0, 3)]
        result = Finder.find_triples(hand)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0].rank, 14)

    # 驗證：有其他雜牌時仍可正確找到三條
    def test_find_triples_with_extra(self):
        hand = [C(3, 14), C(2, 14), C(1, 14), C(3, 13), C(0, 13)]
        result = Finder.find_triples(hand)
        self.assertEqual(len(result), 1)


class TestFindFiveCardHands(unittest.TestCase):
    # 驗證：至少找到一組順子
    def test_find_straight(self):
        hand = [C(0, 3), C(1, 4), C(2, 5), C(3, 6), C(0, 7)]
        result = Finder.find_five_card_hands(hand)
        self.assertGreaterEqual(len(result), 1)

    # 驗證：至少找到一組同花
    def test_find_flush(self):
        hand = [C(0, 3), C(0, 5), C(0, 7), C(0, 9), C(0, 11)]
        result = Finder.find_five_card_hands(hand)
        self.assertGreaterEqual(len(result), 1)

    # 驗證：至少找到一組葫蘆
    def test_find_full_house(self):
        hand = [C(3, 14), C(2, 14), C(1, 14), C(0, 15), C(1, 15)]
        result = Finder.find_five_card_hands(hand)
        self.assertGreaterEqual(len(result), 1)

    # 驗證：至少找到一組四條
    def test_find_four_of_a_kind(self):
        hand = [C(3, 14), C(2, 14), C(1, 14), C(0, 14), C(1, 3)]
        result = Finder.find_five_card_hands(hand)
        self.assertGreaterEqual(len(result), 1)

    # 驗證：至少找到一組同花順
    def test_find_straight_flush(self):
        hand = [C(0, 3), C(0, 4), C(0, 5), C(0, 6), C(0, 7)]
        result = Finder.find_five_card_hands(hand)
        self.assertGreaterEqual(len(result), 1)


class TestFindValidPlays(unittest.TestCase):
    # 驗證：第一手只能出 3♣
    def test_first_turn(self):
        hand = [C(0, 3), C(3, 14), C(2, 13)]
        result = Finder.find_valid_plays(hand, None)
        self.assertEqual(result, [[C(0, 3)]])

    # 驗證：上家為單張時，只能回傳單張候選
    def test_with_last_single(self):
        hand = [C(0, 6), C(3, 14), C(2, 13)]
        last = [C(0, 5)]
        result = Finder.find_valid_plays(hand, last)
        self.assertTrue(all(len(x) == 1 for x in result))

    # 驗證：上家為對子時，只能回傳對子候選
    def test_with_last_pair(self):
        hand = [C(0, 6), C(1, 6), C(3, 14)]
        last = [C(0, 5), C(1, 5)]
        result = Finder.find_valid_plays(hand, last)
        self.assertTrue(all(len(x) == 2 for x in result))

    # 驗證：無法壓過上家時應回傳空清單
    def test_no_valid(self):
        hand = [C(0, 4), C(1, 4), C(2, 3)]
        last = [C(0, 5), C(1, 5)]
        result = Finder.find_valid_plays(hand, last)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
