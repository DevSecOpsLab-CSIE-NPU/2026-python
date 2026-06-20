from classifier import HandClassifier, CardType


class AIStrategy:
    EMPTY_HAND_BONUS = 10000
    NEAR_EMPTY_BONUS = 500
    SPADE_BONUS = 5

    @staticmethod
    def score_play(cards, hand, is_first=False):
        result = HandClassifier.classify(cards)
        if result is None:
            return -1
        ctype, rank, suit = result
        score = HandClassifier.TYPE_SCORES[ctype] * 100 + rank * 10 + suit
        remaining = len(hand) - len(cards)
        if remaining == 0:
            score += AIStrategy.EMPTY_HAND_BONUS
        elif remaining <= 3:
            score += AIStrategy.NEAR_EMPTY_BONUS
        for c in cards:
            if c.suit == 3:
                score += AIStrategy.SPADE_BONUS
        return score

    @staticmethod
    def select_best(valid_plays, hand, is_first=False):
        if not valid_plays:
            return None
        if is_first:
            for p in valid_plays:
                if any(c.rank == 3 and c.suit == 0 for c in p):
                    return p
            return None
        best = max(valid_plays, key=lambda p: AIStrategy.score_play(p, hand))
        return best
