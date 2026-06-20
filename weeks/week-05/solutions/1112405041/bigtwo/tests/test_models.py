import unittest
from game.models import Card, Deck, Hand, Player

class TestCard(unittest.TestCase):
    def test_card_creation(self):
        c = Card(rank=14, suit=3)
        self.assertEqual(c.rank, 14)
        self.assertEqual(c.suit, 3)

    def test_card_repr_ace(self):
        c = Card(14, 3)
        self.assertIn("A", repr(c))

    def test_card_repr_three(self):
        c = Card(3, 0)
        self.assertIn("3", repr(c))

    def test_card_compare_suit(self):
        self.assertGreater(Card(14, 3), Card(14, 2))
        self.assertGreater(Card(14, 2), Card(14, 1))
        self.assertGreater(Card(14, 1), Card(14, 0))

    def test_card_compare_rank(self):
        self.assertGreater(Card(15, 0), Card(14, 3))
        self.assertGreater(Card(14, 0), Card(13, 3))

    def test_card_compare_equal(self):
        self.assertFalse(Card(14, 3) > Card(14, 3))

    def test_card_sort_key(self):
        self.assertEqual(Card(14, 3).to_sort_key(), (14, 3))

class TestDeck(unittest.TestCase):
    def test_deck_has_52_cards(self):
        self.assertEqual(len(Deck().cards), 52)

    def test_deck_all_unique(self):
        self.assertEqual(len(set(Deck().cards)), 52)

    def test_deck_shuffle(self):
        d = Deck()
        orig = list(d.cards)
        d.shuffle()
        self.assertNotEqual(d.cards, orig)

    def test_deal_5_cards(self):
        d = Deck()
        c = d.deal(5)
        self.assertEqual(len(c), 5)
        self.assertEqual(len(d.cards), 47)

    def test_deal_exceed(self):
        c = Deck().deal(60)
        self.assertEqual(len(c), 52)

class TestHand(unittest.TestCase):
    def test_hand_creation(self):
        h = Hand([Card(3, 0), Card(14, 3)])
        self.assertEqual(len(h), 2)

    def test_hand_sort_desc(self):
        h = Hand([Card(14, 3), Card(13, 2)])
        h.sort_desc()
        self.assertGreater(h[0].rank, h[1].rank)

    def test_hand_find_3_clubs(self):
        h = Hand([Card(14, 3), Card(3, 0)])
        self.assertIsNotNone(h.find_3_clubs())

    def test_hand_find_3_clubs_none(self):
        h = Hand([Card(14, 3), Card(3, 1)])
        self.assertIsNone(h.find_3_clubs())

    def test_hand_remove(self):
        c = Card(3, 0)
        h = Hand([c, Card(14, 3)])
        h.remove([c])
        self.assertEqual(len(h), 1)

class TestPlayer(unittest.TestCase):
    def test_player_human(self):
        p = Player("P1", is_ai=False)
        self.assertFalse(p.is_ai)

    def test_player_ai(self):
        p = Player("AI", is_ai=True)
        self.assertTrue(p.is_ai)

    def test_player_take(self):
        p = Player("P1")
        p.take_cards([Card(3, 0)])
        self.assertEqual(len(p.hand), 1)

    def test_player_play(self):
        c = Card(3, 0)
        p = Player("P1")
        p.take_cards([c])
        played = p.play_cards([c])
        self.assertEqual(len(played), 1)
        self.assertEqual(len(p.hand), 0)

if __name__ == "__main__":
    unittest.main()
