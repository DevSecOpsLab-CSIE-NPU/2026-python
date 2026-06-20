class Card:
    RANK_NAMES = {3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8",
                  9: "9", 10: "10", 11: "J", 12: "Q", 13: "K", 14: "A", 15: "2"}
    SUIT_NAMES = ["♣", "♦", "♥", "♠"]

    def __init__(self, rank: int, suit: int):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.SUIT_NAMES[self.suit]}{self.RANK_NAMES[self.rank]}"

    def __eq__(self, other):
        return isinstance(other, Card) and self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.suit < other.suit

    def __hash__(self):
        return hash((self.rank, self.suit))

    def to_sort_key(self):
        return (self.rank, self.suit)


class Deck:
    def __init__(self):
        self.cards = self._create_cards()

    def _create_cards(self):
        return [Card(r, s) for r in range(3, 16) for s in range(4)]

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, n):
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt


class Hand(list):
    def __init__(self, cards=None):
        super().__init__(cards or [])

    def sort_desc(self):
        self.sort(key=lambda c: (c.rank, c.suit), reverse=True)

    def find_3_clubs(self):
        for c in self:
            if c.rank == 3 and c.suit == 0:
                return c
        return None

    def remove(self, cards):
        for c in cards:
            if c in self:
                super().remove(c)


class Player:
    def __init__(self, name: str, is_ai: bool = False):
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0

    def take_cards(self, cards):
        self.hand.extend(cards)

    def play_cards(self, cards):
        self.hand.remove(cards)
        return cards
