from __future__ import annotations

from classifier import CardType, HandClassifier
from models import Card, Hand


class AIStrategy:
    """AI 出牌策略：以貪心法挑選當下分數最高的合法出牌。"""

    TYPE_SCORES = {
        CardType.SINGLE: 1,
        CardType.PAIR: 2,
        CardType.TRIPLE: 3,
        CardType.STRAIGHT: 4,
        CardType.FLUSH: 5,
        CardType.FULL_HOUSE: 6,
        CardType.FOUR_OF_A_KIND: 7,
        CardType.STRAIGHT_FLUSH: 8,
    }

    EMPTY_HAND_BONUS = 10000
    NEAR_EMPTY_BONUS = 500
    SPADE_BONUS = 5

    @staticmethod
    def score_play(cards: list[Card], hand: Hand, is_first: bool = False) -> float:
        """評分公式：牌型*100 + 點數*10 + 收尾加分 + 黑桃加分。"""
        classified = HandClassifier.classify(cards)
        if classified is None:
            return float("-inf")

        ctype, rank_value, _ = classified

        # 基礎分數：牌型層級優先，其次看點數。
        score = AIStrategy.TYPE_SCORES[ctype] * 100 + rank_value * 10

        # 出完後剩餘牌數，用於鼓勵快出完手牌。
        remaining = len(hand.cards) - len(cards)
        if remaining <= 1:
            score += AIStrategy.EMPTY_HAND_BONUS
        elif remaining <= 3:
            score += AIStrategy.NEAR_EMPTY_BONUS

        # 黑桃獎勵：每張黑桃 +5。
        spades = sum(1 for card in cards if card.suit == 3)
        score += spades * AIStrategy.SPADE_BONUS

        # 第一回合可額外鼓勵含 3♣ 的合法開局牌。
        if is_first and Card(3, 0) in cards:
            score += 1

        return float(score)

    @staticmethod
    def select_best(valid_plays: list[list[Card]], hand: Hand, is_first: bool = False):
        """從合法出牌中挑分數最高者；無牌可出則回傳 None。"""
        if not valid_plays:
            return None

        if is_first:
            # 規則：第一回合只能從包含 3♣ 的候選中選。
            first_candidates = [play for play in valid_plays if Card(3, 0) in play]
            if first_candidates:
                valid_plays = first_candidates

        best_play = None
        best_score = float("-inf")

        for play in valid_plays:
            score = AIStrategy.score_play(play, hand, is_first=is_first)
            if score > best_score:
                best_score = score
                best_play = play

        return best_play
