"""
可用出牌搜尋工具。
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations

from game.classifier import HandClassifier
from game.models import Card, Hand


class HandFinder:
    """從手牌中找出所有可出的組合。"""

    @staticmethod
    def _sort_play(cards: list[Card]) -> list[Card]:
        return sorted(cards, key=lambda card: card.to_sort_key(), reverse=True)

    @classmethod
    def find_singles(cls, hand: Hand) -> list[list[Card]]:
        return [[card] for card in cls._sort_play(list(hand.cards))]

    @classmethod
    def find_pairs(cls, hand: Hand) -> list[list[Card]]:
        groups: dict[int, list[Card]] = defaultdict(list)
        for card in hand.cards:
            groups[card.rank].append(card)

        pairs: list[list[Card]] = []
        for rank in sorted(groups, reverse=True):
            cards = sorted(groups[rank], key=lambda card: card.suit, reverse=True)
            for combo in combinations(cards, 2):
                pairs.append(cls._sort_play(list(combo)))
        return pairs

    @classmethod
    def find_triples(cls, hand: Hand) -> list[list[Card]]:
        groups: dict[int, list[Card]] = defaultdict(list)
        for card in hand.cards:
            groups[card.rank].append(card)

        triples: list[list[Card]] = []
        for rank in sorted(groups, reverse=True):
            cards = sorted(groups[rank], key=lambda card: card.suit, reverse=True)
            for combo in combinations(cards, 3):
                triples.append(cls._sort_play(list(combo)))
        return triples

    @classmethod
    def find_fives(cls, hand: Hand) -> list[list[Card]]:
        fives: list[list[Card]] = []
        for combo in combinations(hand.cards, 5):
            play = cls._sort_play(list(combo))
            if HandClassifier.classify(play) is not None:
                fives.append(play)
        fives.sort(
            key=lambda play: HandClassifier.classify(play) or (0, 0, 0),
            reverse=True,
        )
        return fives

    @classmethod
    def get_all_valid_plays(
        cls,
        hand: Hand,
        last_play: list[Card] | None,
        is_first_turn: bool = False,
    ) -> list[list[Card]]:
        all_plays = (
            cls.find_singles(hand)
            + cls.find_pairs(hand)
            + cls.find_triples(hand)
            + cls.find_fives(hand)
        )

        valid = [
            play
            for play in all_plays
            if HandClassifier.can_play(last_play, play, is_first_turn=is_first_turn)
        ]
        valid.sort(
            key=lambda play: (len(play), HandClassifier.classify(play) or (0, 0, 0)),
            reverse=True,
        )
        return valid
