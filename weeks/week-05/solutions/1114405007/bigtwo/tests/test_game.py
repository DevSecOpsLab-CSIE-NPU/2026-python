import unittest

from game.game import BigTwoGame
from game.models import Card


class TestGame(unittest.TestCase):
    def test_setup(self):
        game = BigTwoGame()
        game.setup()
        self.assertEqual(len(game.players), 4)
        self.assertEqual(sum(len(p.hand) for p in game.players), 52)
        self.assertTrue(any(p.hand.find_3_clubs() for p in game.players))

    def test_play_and_pass(self):
        game = BigTwoGame()
        game.setup()

        player = game.get_current_player()
        self.assertTrue(game.play(player, [Card(3, 0)]))

        game.next_turn()
        next_player = game.get_current_player()
        self.assertTrue(game.pass_(next_player))

    def test_winner_detect(self):
        game = BigTwoGame()
        game.setup()
        p0 = game.players[0]
        p0.hand.clear()
        self.assertEqual(game.check_winner(), p0)

    def test_opening_rule_only_first_trick(self):
        game = BigTwoGame()
        game.setup()

        opener = game.get_current_player()
        self.assertTrue(game.play(opener, [Card(3, 0)]))

        # Simulate new trick lead after the opening hand was already played.
        game.last_play = None
        game.opening_required = False
        game.next_turn()

        leader = game.get_current_player()
        self.assertTrue(game.play(leader, [leader.hand[0]]))


if __name__ == "__main__":
    unittest.main()
