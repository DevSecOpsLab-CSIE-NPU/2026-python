from itertools import combinations
from game.models import Card, Hand
from game.classifier import HandClassifier


class HandFinder:
    @staticmethod
    def find_singles(hand):
        return [[c] for c in hand]

    @staticmethod
    def find_pairs(hand):
        pairs = []
        from collections import defaultdict
        by_rank = defaultdict(list)
        for c in hand:
            by_rank[c.rank].append(c)
        for rank, cards in by_rank.items():
            if len(cards) >= 2:
                for combo in combinations(cards, 2):
                    pairs.append(list(combo))
        return pairs

    @staticmethod
    def find_triples(hand):
        triples = []
        from collections import defaultdict
        by_rank = defaultdict(list)
        for c in hand:
            by_rank[c.rank].append(c)
        for rank, cards in by_rank.items():
            if len(cards) >= 3:
                for combo in combinations(cards, 3):
                    triples.append(list(combo))
        return triples

    @staticmethod
    def find_fives(hand):
        fives = []
        for combo in combinations(hand, 5):
            result = HandClassifier.classify(list(combo))
            if result is not None:
                fives.append(list(combo))
        return fives

    @staticmethod
    def get_all_valid_plays(hand, last_play):
        if last_play is None:
            three_clubs = [c for c in hand if c.rank == 3 and c.suit == 0]
            if not three_clubs:
                return []
            return [[three_clubs[0]]]

        n = len(last_play)
        candidates = []
        if n == 1:
            candidates = HandFinder.find_singles(hand)
        elif n == 2:
            candidates = HandFinder.find_pairs(hand)
        elif n == 3:
            candidates = HandFinder.find_triples(hand)
        elif n == 5:
            candidates = HandFinder.find_fives(hand)
        else:
            return []

        result = []
        for play in candidates:
            if HandClassifier.compare(play, last_play) == 1:
                result.append(play)
        return result
