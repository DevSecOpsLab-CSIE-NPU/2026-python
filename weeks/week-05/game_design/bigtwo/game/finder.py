"""Big Two Card Game - Hand Finding"""

from typing import List, Optional
from itertools import combinations
from .models import Card, Hand
from .classifier import HandClassifier, CardType


class HandFinder:
    @staticmethod
    def find_singles(hand: Hand) -> List[List[Card]]:
        return [[card] for card in hand]

    @staticmethod
    def find_pairs(hand: Hand) -> List[List[Card]]:
        result = []
        rank_groups = {}
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)

        for cards in rank_groups.values():
            if len(cards) >= 2:
                for pair in combinations(cards, 2):
                    result.append(list(pair))
        return result

    @staticmethod
    def find_triples(hand: Hand) -> List[List[Card]]:
        result = []
        rank_groups = {}
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)

        for cards in rank_groups.values():
            if len(cards) >= 3:
                for triple in combinations(cards, 3):
                    result.append(list(triple))
        return result

    @classmethod
    def find_fives(cls, hand: Hand) -> List[List[Card]]:
        result = []
        hand_ranks = sorted(set(c.rank for c in hand))

        for i in range(len(hand_ranks) - 4):
            straight_ranks = hand_ranks[i : i + 5]
            straight = cls._find_straight(hand, straight_ranks)
            if straight:
                is_flush = cls._is_flush_straight(straight)
                if is_flush:
                    result.append(straight)
                else:
                    result.append(straight)

        if (
            [3, 4, 5, 6, 14] == sorted(hand_ranks[:5])
            if len(hand_ranks) >= 5
            else False
        ):
            a2345 = cls._find_straight(hand, [3, 4, 5, 6, 14])
            if a2345 and a2345 not in result:
                result.append(a2345)

        result.extend(cls._find_flush(hand))
        result.extend(cls._find_full_house(hand))
        result.extend(cls._find_four_of_a_kind(hand))

        seen = set()
        unique_result = []
        for play in result:
            key = tuple(sorted(c.rank for c in play))
            if key not in seen:
                seen.add(key)
                unique_result.append(play)
        return unique_result

    @staticmethod
    def _find_straight(hand: Hand, ranks: List[int]) -> Optional[List[Card]]:
        if len(ranks) != 5:
            return None

        result = []
        for r in ranks:
            found = False
            for card in hand:
                if card.rank == r and card not in result:
                    result.append(card)
                    found = True
                    break
            if not found:
                return None

        return result if len(result) == 5 else None

    @staticmethod
    def _is_flush_straight(cards: List[Card]) -> bool:
        if len(cards) != 5:
            return False
        suits = [c.suit for c in cards]
        return len(set(suits)) == 1

    @staticmethod
    def _find_flush(hand: Hand) -> List[List[Card]]:
        result = []
        suit_groups = {s: [] for s in range(4)}
        for card in hand:
            suit_groups[card.suit].append(card)

        for suit, cards in suit_groups.items():
            if len(cards) >= 5:
                for combo in combinations(cards, 5):
                    combo_list = list(combo)
                    combo_list.sort(key=lambda c: c.rank, reverse=True)
                    ranks = [c.rank for c in combo_list]
                    if not HandClassifier._is_straight(ranks):
                        result.append(combo_list)
        return result

    @staticmethod
    def _find_full_house(hand: Hand) -> List[List[Card]]:
        result = []
        rank_groups = {}
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)

        triples = [(r, cards) for r, cards in rank_groups.items() if len(cards) >= 3]
        pairs = [(r, cards) for r, cards in rank_groups.items() if len(cards) >= 2]

        for triple_rank, triple_cards in triples:
            for triple_combo in combinations(triple_cards, 3):
                for pair_rank, pair_cards in pairs:
                    if pair_rank == triple_rank and len(pair_cards) < 4:
                        continue
                    for pair_combo in combinations(pair_cards, 2):
                        full_house = list(triple_combo) + list(pair_combo)
                        result.append(full_house)
        return result

    @staticmethod
    def _find_four_of_a_kind(hand: Hand) -> List[List[Card]]:
        result = []
        rank_groups = {}
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)

        for rank, cards in rank_groups.items():
            if len(cards) >= 4:
                for four in combinations(cards, 4):
                    four_list = list(four)
                    for extra in hand:
                        if extra not in four_list:
                            four_list.append(extra)
                            result.append(four_list)
                            break
        return result

    @classmethod
    def get_all_valid_plays(
        cls, hand: Hand, last_play: Optional[List[Card]]
    ) -> List[List[Card]]:
        if last_play is None:
            club_3 = hand.find_3_clubs()
            if club_3:
                return [[club_3]]
            return []

        n = len(last_play)
        valid = []

        if n == 1:
            valid.extend(cls.find_singles(hand))
        elif n == 2:
            valid.extend(cls.find_pairs(hand))
        elif n == 3:
            valid.extend(cls.find_triples(hand))
        elif n == 5:
            valid.extend(cls.find_fives(hand))

        return [play for play in valid if HandClassifier.compare(play, last_play) > 0]
