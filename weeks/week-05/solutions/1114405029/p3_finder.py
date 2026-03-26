# p3_finder.py
# Phase 3：牌型搜尋模組
#
# 功能：實作 HandFinder 類別，負責在手牌中找出所有可能的合法出牌組合。
# 依賴：p1_models.py（Card, Hand）、p2_classifier.py（HandClassifier, CardType）
#
# 執行測試：
#   python p3-finder-unit-test.py

from __future__ import annotations

from itertools import combinations
from typing import List, Optional

from p1_models import Card, Hand
from p2_classifier import CardType, HandClassifier


class HandFinder:
    """牌型搜尋器：找出手牌中所有可能的合法出牌組合。"""

    # -------------------------------------------------------
    # 基礎搜尋方法
    # -------------------------------------------------------

    @staticmethod
    def find_singles(hand: Hand) -> List[List[Card]]:
        """
        找出所有可能的單張出牌。

        做法：每張牌都包成一個長度 1 的 list。
        例：手牌 [♠A, ♥K, ♣3] → [[♠A], [♥K], [♣3]]

        :param hand: 玩家手牌
        :return: 每個元素為 [Card] 的清單
        """
        return [[card] for card in hand]

    @staticmethod
    def find_pairs(hand: Hand) -> List[List[Card]]:
        """
        找出所有可能的對子（相同點數的兩張牌）。

        做法：
          1. 先將手牌依點數（rank）分組
          2. 對每個點數的同組牌，用 combinations 取 2 張
          3. 每個組合即為一個對子出牌

        例：手牌 [♠A, ♥A, ♣3] → [[♠A, ♥A]]

        :param hand: 玩家手牌
        :return: 每個元素為 [Card, Card] 的清單
        """
        # 依點數分組：{rank: [cards with that rank]}
        rank_groups: dict[int, List[Card]] = {}
        for card in hand:
            rank_groups.setdefault(card.rank, []).append(card)

        result: List[List[Card]] = []
        for cards in rank_groups.values():
            if len(cards) >= 2:
                # 從相同點數的牌中取出所有 2 張組合
                for pair in combinations(cards, 2):
                    result.append(list(pair))
        return result

    @staticmethod
    def find_triples(hand: Hand) -> List[List[Card]]:
        """
        找出所有可能的三條（相同點數的三張牌）。

        做法：與 find_pairs 相同邏輯，改為取 3 張組合。
        例：手牌 [♠A, ♥A, ♦A, ♣3] → [[♠A, ♥A, ♦A]]

        :param hand: 玩家手牌
        :return: 每個元素為 [Card, Card, Card] 的清單
        """
        # 依點數分組
        rank_groups: dict[int, List[Card]] = {}
        for card in hand:
            rank_groups.setdefault(card.rank, []).append(card)

        result: List[List[Card]] = []
        for cards in rank_groups.values():
            if len(cards) >= 3:
                for triple in combinations(cards, 3):
                    result.append(list(triple))
        return result

    @staticmethod
    def find_fives(hand: Hand) -> List[List[Card]]:
        """
        找出所有合法的五張牌型：順子、同花、葫蘆、四條、同花順。

        做法：
          1. 用 combinations(hand, 5) 列舉手牌所有 5 張組合
          2. 對每個組合呼叫 HandClassifier.classify()
          3. 只保留以下牌型：
             STRAIGHT, FLUSH, FULL_HOUSE, FOUR_OF_A_KIND, STRAIGHT_FLUSH

        :param hand: 玩家手牌
        :return: 每個元素為長度 5 的 [Card] 清單
        """
        # 僅保留這五種五張牌型
        valid_five_types = {
            CardType.STRAIGHT,
            CardType.FLUSH,
            CardType.FULL_HOUSE,
            CardType.FOUR_OF_A_KIND,
            CardType.STRAIGHT_FLUSH,
        }

        result: List[List[Card]] = []
        for combo in combinations(hand, 5):
            play = list(combo)
            classified = HandClassifier.classify(play)
            # classify 回傳 None 代表不合法牌型，或點數不夠
            if classified and classified[0] in valid_five_types:
                result.append(play)
        return result

    # -------------------------------------------------------
    # 合法出牌搜尋
    # -------------------------------------------------------

    @staticmethod
    def get_all_valid_plays(
        hand: Hand,
        last_play: Optional[List[Card]],
    ) -> List[List[Card]]:
        """
        根據上家的出牌，找出手牌中所有合法的出牌組合。

        規則：
          (1) last_play is None（第一回合）
                            - 回傳手牌中可形成的合法牌型候選
                            - 相容策略：若手牌仍有 3♣，優先只回傳「包含 3♣」的候選
                                （維持舊測試與舊介面期望）
                            - 若手牌已無 3♣（常見於後續新回合），回傳一般化候選

          (2) last_play 有值（非第一回合）
              - 先 classify(last_play) 得到上家牌型
              - 依上家張數找同類型候選出牌：
                  1 張 → find_singles
                  2 張 → find_pairs
                  3 張 → find_triples
                  5 張 → find_fives
              - 只保留可以壓過上家（compare == 1）的出牌

          (3) 無法出牌時，回傳 []

        :param hand: 玩家手牌
        :param last_play: 上家出的牌（None = 第一回合）
        :return: 所有合法出牌組合的清單
        """
        # ── 情況 (1)：第一回合，手牌必須含有 ♣3 ──────────────
        if last_play is None:
            # 先收集一般化候選：單張 / 對子 / 三條 / 五張牌型。
            # 真正是否可出，仍由 game.play() 端依規則判定。
            candidates = (
                HandFinder.find_singles(hand)
                + HandFinder.find_pairs(hand)
                + HandFinder.find_triples(hand)
                + HandFinder.find_fives(hand)
            )

            three_clubs = Card(3, 0)
            # 相容舊規則：若手牌仍有 3♣，回傳時優先保留含 3♣ 的候選。
            if three_clubs in hand:
                return [play for play in candidates if three_clubs in play]

            # 若手牌沒有 3♣（例如後續新回合），則回傳一般化候選。
            return candidates

        # ── 情況 (2)：非第一回合，依張數找同類型候選 ──────────
        n = len(last_play)

        # 依張數取候選出牌清單
        if n == 1:
            candidates = HandFinder.find_singles(hand)
        elif n == 2:
            candidates = HandFinder.find_pairs(hand)
        elif n == 3:
            candidates = HandFinder.find_triples(hand)
        elif n == 5:
            candidates = HandFinder.find_fives(hand)
        else:
            # 不支援的張數，無法出牌
            return []

        # 只保留可以壓過上家的出牌（compare 回傳 1 代表 play 比 last_play 大）
        valid: List[List[Card]] = []
        for play in candidates:
            try:
                if HandClassifier.compare(play, last_play) == 1:
                    valid.append(play)
            except (TypeError, ValueError):
                # classify 失敗或牌型不合，跳過
                pass
        return valid
