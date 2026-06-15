import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from bigtwo_models import Card, Deck, Hand, Player

class TestBigTwoModels(unittest.TestCase):
    """
    å°é? game_design/p1-test.md ?„å–®?ƒæ¸¬è©?
    """

    def test_card_creation(self):
        # æ¸¬è©¦?¡ç?å»ºç?
        c = Card(14, 3) # é»‘æ? A
        self.assertEqual(c.rank, 14)
        self.assertEqual(c.suit, 3)

    def test_card_repr(self):
        # æ¸¬è©¦?¡ç??‡å?é¡¯ç¤º
        self.assertEqual(repr(Card(14, 3)), "? A")
        self.assertEqual(repr(Card(3, 0)), "??")
        self.assertEqual(repr(Card(10, 2)), "?¥T")

    def test_card_comparison(self):
        # æ¸¬è©¦?¡ç?å¤§å?æ¯”è? (é»‘æ? > ç´…å? > ?¹å? > æ¢…èŠ±)
        self.assertTrue(Card(14, 3) > Card(14, 2)) # ? A > ?¥A
        self.assertTrue(Card(15, 0) > Card(14, 3)) # ?? > ? A (2 ?€å¤?
        self.assertTrue(Card(14, 0) > Card(13, 3)) # ?£A > ? K
        self.assertFalse(Card(14, 3) < Card(14, 3)) # ?¸å??‡ä?å°æ–¼

    def test_deck_initialization(self):
        # æ¸¬è©¦?Œç??å???
        d = Deck()
        self.assertEqual(len(d.cards), 52)
        # æ¸¬è©¦?¯ä???(ä¸é?è¤?
        self.assertEqual(len(set(d.cards)), 52)

    def test_deck_deal(self):
        # æ¸¬è©¦?¼ç??è¼¯
        d = Deck()
        dealt = d.deal(13)
        self.assertEqual(len(dealt), 13)
        self.assertEqual(len(d.cards), 39)

    def test_hand_sorting(self):
        # æ¸¬è©¦?‹ç??’å?
        h = Hand([Card(3, 0), Card(14, 3), Card(3, 3), Card(13, 2)])
        h.sort_desc()
        # ?æ?ï¼šâ?A, ?¥K, ??, ??
        self.assertEqual(repr(h[0]), "? A")
        self.assertEqual(repr(h[-1]), "??")

    def test_hand_find_3_clubs(self):
        # æ¸¬è©¦å°‹æ‰¾æ¢…èŠ± 3
        h1 = Hand([Card(14, 3), Card(3, 0)])
        self.assertIsNotNone(h1.find_3_clubs())

        h2 = Hand([Card(14, 3), Card(3, 1)])
        self.assertIsNone(h2.find_3_clubs())

    def test_player_initialization(self):
        # æ¸¬è©¦?©å®¶å»ºç?
        p = Player("CSIE_Student")
        self.assertEqual(p.name, "CSIE_Student")
        self.assertEqual(len(p.hand), 0)

if __name__ == "__main__":
    unittest.main()

