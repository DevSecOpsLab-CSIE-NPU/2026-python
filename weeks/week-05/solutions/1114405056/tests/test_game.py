import unittest
from game.models import Card, Hand
from game.game import BigTwoGame


def C(rank, suit):
    return Card(rank, suit)


class TestGameInit(unittest.TestCase):

    def setUp(self):
        self.game = BigTwoGame()
        self.game.setup()

    def test_game_has_4_players(self):
        self.assertEqual(len(self.game.players), 4)

    def test_each_player_13_cards(self):
        for player in self.game.players:
            self.assertEqual(len(player.hand), 13)

    def test_total_cards_distributed(self):
        total = sum(len(p.hand) for p in self.game.players)
        self.assertEqual(total, 52)

    def test_first_player_has_3_clubs(self):
        first = self.game.get_current_player()
        self.assertIsNotNone(first.hand.find_3_clubs())

    def test_one_human_three_ai(self):
        human_count = sum(1 for p in self.game.players if not p.is_ai)
        ai_count = sum(1 for p in self.game.players if p.is_ai)
        self.assertEqual(human_count, 1)
        self.assertEqual(ai_count, 3)


class TestPlayFlow(unittest.TestCase):

    def setUp(self):
        self.game = BigTwoGame()
        self.game.setup()

    def test_play_removes_cards(self):
        first = self.game.get_current_player()
        before = len(first.hand)
        three_clubs = first.hand.find_3_clubs()
        self.game.play(first, [three_clubs])
        self.assertEqual(len(first.hand), before - 1)

    def test_play_sets_last_play(self):
        first = self.game.get_current_player()
        three_clubs = first.hand.find_3_clubs()
        self.game.play(first, [three_clubs])
        self.assertIsNotNone(self.game.last_play)

    def test_invalid_play(self):
        first = self.game.get_current_player()
        # Try to play a card that is not 3??on first turn
        other_card = next(c for c in first.hand
                          if not (c.rank == 3 and c.suit == 0))
        result = self.game.play(first, [other_card])
        self.assertFalse(result)

    def test_pass_increments(self):
        # First make a valid first play
        first = self.game.get_current_player()
        three_clubs = first.hand.find_3_clubs()
        self.game.play(first, [three_clubs])
        self.game.next_turn()

        second = self.game.get_current_player()
        before = self.game.pass_count
        self.game.pass_(second)
        self.assertEqual(self.game.pass_count, before + 1)


class TestRoundLogic(unittest.TestCase):

    def setUp(self):
        self.game = BigTwoGame()
        self.game.setup()

    def test_three_passes_resets(self):
        first = self.game.get_current_player()
        three_clubs = first.hand.find_3_clubs()
        self.game.play(first, [three_clubs])

        for _ in range(3):
            self.game.next_turn()
            self.game.pass_(self.game.get_current_player())

        self.assertIsNone(self.game.last_play)

    def test_turn_rotates(self):
        before = self.game.current_player
        self.game.next_turn()
        self.assertEqual(self.game.current_player, (before + 1) % 4)


class TestWinner(unittest.TestCase):

    def setUp(self):
        self.game = BigTwoGame()
        self.game.setup()

    def test_no_winner_yet(self):
        self.assertIsNone(self.game.check_winner())

    def test_detect_winner(self):
        player = self.game.players[0]
        player.hand.clear()
        self.assertIsNotNone(self.game.check_winner())

    def test_game_ends(self):
        player = self.game.players[0]
        player.hand.clear()
        self.game.check_winner()
        self.assertTrue(self.game.is_game_over())


if __name__ == '__main__':
    unittest.main()
