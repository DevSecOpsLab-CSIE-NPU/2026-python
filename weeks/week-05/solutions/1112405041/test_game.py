import unittest
from game import BigTwoGame
from models import Card

class TestBigTwoGame(unittest.TestCase):
    def test_game_has_4_players(self):
        g = BigTwoGame()
        g.setup()
        self.assertEqual(len(g.players), 4)

    def test_each_player_13_cards(self):
        g = BigTwoGame()
        g.setup()
        for p in g.players:
            self.assertEqual(len(p.hand), 13)

    def test_total_cards_distributed(self):
        g = BigTwoGame()
        g.setup()
        total = sum(len(p.hand) for p in g.players)
        self.assertEqual(total, 52)

    def test_first_player_has_3_clubs(self):
        g = BigTwoGame()
        g.setup()
        first = g.players[g.current_player]
        self.assertIsNotNone(first.hand.find_3_clubs())

    def test_one_human_three_ai(self):
        g = BigTwoGame()
        g.setup()
        ais = sum(1 for p in g.players if p.is_ai)
        self.assertEqual(ais, 3)

    def test_play_removes_cards(self):
        g = BigTwoGame()
        g.setup()
        p = g.players[g.current_player]
        c = p.hand.find_3_clubs()
        if c:
            g.play(p, [c])
            self.assertNotIn(c, p.hand)

    def test_play_sets_last_play(self):
        g = BigTwoGame()
        g.setup()
        p = g.players[g.current_player]
        c = p.hand.find_3_clubs()
        if c:
            g.play(p, [c])
            self.assertIsNotNone(g.last_play)

    def test_pass_increments(self):
        g = BigTwoGame()
        g.setup()
        p = g.get_current_player()
        g.pass_(p)
        self.assertEqual(g.pass_count, 1)

    def test_turn_rotates(self):
        g = BigTwoGame()
        g.setup()
        old = g.current_player
        g.next_turn()
        self.assertEqual(g.current_player, (old + 1) % 4)

    def test_no_winner_yet(self):
        g = BigTwoGame()
        g.setup()
        self.assertIsNone(g.check_winner())

    def test_game_ends(self):
        g = BigTwoGame()
        g.setup()
        self.assertFalse(g.is_game_over())

if __name__ == "__main__":
    unittest.main()
