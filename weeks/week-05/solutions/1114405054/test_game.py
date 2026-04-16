"""Phase 5 遊戲流程的單元測試。"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


def _prepare_import_path() -> None:
    current = Path(__file__).resolve().parent

    for candidate in [current, *current.parents]:
        if (candidate / "game").is_dir():
            sys.path.insert(0, str(candidate))
            return

        if (candidate / "bigtwo" / "game").is_dir():
            sys.path.insert(0, str(candidate / "bigtwo"))
            return


_prepare_import_path()

from game.game import BigTwoGame
from game.models import Card, Hand


def _find_absent_card(hand: Hand) -> Card:
    have = set(hand)
    for rank in range(3, 16):
        for suit in range(4):
            candidate = Card(rank, suit)
            if candidate not in have:
                return candidate
    return Card(3, 0)


class TestGameSetup(unittest.TestCase):
    def test_game_has_4_players(self) -> None:
        game = BigTwoGame()
        game.setup()
        self.assertEqual(len(game.players), 4)

    def test_each_player_13_cards(self) -> None:
        game = BigTwoGame()
        game.setup()
        self.assertTrue(all(len(player.hand) == 13 for player in game.players))

    def test_total_cards_distributed(self) -> None:
        game = BigTwoGame()
        game.setup()
        self.assertEqual(sum(len(player.hand) for player in game.players), 52)

    def test_first_player_has_3_clubs(self) -> None:
        game = BigTwoGame()
        game.setup()
        starter = game.players[game.current_player]
        self.assertIn(Card(3, 0), starter.hand)

    def test_one_human_three_ai(self) -> None:
        game = BigTwoGame()
        game.setup()
        ai_count = sum(1 for player in game.players if player.is_ai)
        human_count = sum(1 for player in game.players if not player.is_ai)
        self.assertEqual(ai_count, 3)
        self.assertEqual(human_count, 1)


class TestPlayFlow(unittest.TestCase):
    def test_play_removes_cards(self) -> None:
        game = BigTwoGame()
        game.setup()

        player = game.players[game.current_player]
        play_cards = [Card(3, 0)]
        before = len(player.hand)

        ok = game.play(player, play_cards)
        self.assertTrue(ok)
        self.assertEqual(len(player.hand), before - 1)

    def test_play_sets_last_play(self) -> None:
        game = BigTwoGame()
        game.setup()

        player = game.players[game.current_player]
        play_cards = [Card(3, 0)]
        ok = game.play(player, play_cards)

        self.assertTrue(ok)
        self.assertIsNotNone(game.last_play)
        if isinstance(game.last_play, tuple):
            self.assertEqual(game.last_play[0], play_cards)
        else:
            self.assertEqual(game.last_play, play_cards)

    def test_invalid_play(self) -> None:
        game = BigTwoGame()
        game.setup()

        player = game.players[game.current_player]
        invalid = _find_absent_card(player.hand)

        ok = game.play(player, [invalid])
        self.assertFalse(ok)

    def test_pass_increments(self) -> None:
        game = BigTwoGame()
        game.setup()

        player = game.players[game.current_player]
        game.last_play = ([Card(3, 0)], "P0")
        before = game.pass_count

        ok = game.pass_(player)
        self.assertTrue(ok)
        self.assertEqual(game.pass_count, before + 1)


class TestTurnRules(unittest.TestCase):
    def test_three_passes_resets(self) -> None:
        game = BigTwoGame()
        game.setup()

        game.last_play = ([Card(14, 3)], "P1")
        game.pass_count = 3
        game.check_round_reset()

        self.assertIsNone(game.last_play)
        self.assertEqual(game.pass_count, 0)

    def test_turn_rotates(self) -> None:
        game = BigTwoGame()
        game.setup()

        before = game.current_player
        game.next_turn()
        self.assertEqual(game.current_player, (before + 1) % 4)


class TestWinnerRules(unittest.TestCase):
    def test_detect_winner(self) -> None:
        game = BigTwoGame()
        game.setup()

        game.players[0].hand = Hand([])
        winner = game.check_winner()

        self.assertIsNotNone(winner)
        self.assertEqual(winner, game.players[0])

    def test_no_winner_yet(self) -> None:
        game = BigTwoGame()
        game.setup()
        self.assertIsNone(game.check_winner())

    def test_game_ends(self) -> None:
        game = BigTwoGame()
        game.setup()

        game.players[0].hand = Hand([])
        game.check_winner()

        self.assertTrue(game.is_game_over())


if __name__ == "__main__":
    unittest.main(verbosity=2)
