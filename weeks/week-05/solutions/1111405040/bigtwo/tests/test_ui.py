"""
ui 模組測試。
"""

from __future__ import annotations

import unittest

from game.game import BigTwoGame
from game.models import Card, Hand, Player
from ui.app import BigTwoApp
from ui.input import InputHandler
from ui.render import Renderer


class TestUI(unittest.TestCase):
    """UI 與互動層測試。"""

    def test_card_render_returns_surface_like_object(self) -> None:
        renderer = Renderer()
        surface = renderer.draw_card(Card(14, 3), 0, 0)
        self.assertGreater(surface.get_width(), 0)
        self.assertGreater(surface.get_height(), 0)

    def test_hand_render_returns_surface_like_object(self) -> None:
        renderer = Renderer()
        hand = Hand([Card(14, 3), Card(3, 0)])
        surface = renderer.draw_hand(hand, 0, 0, selected_indices={0})
        self.assertGreater(surface.get_width(), 0)
        self.assertGreater(surface.get_height(), 0)

    def test_try_play_selected_cards(self) -> None:
        game = BigTwoGame(seed=7)
        player = Player("Player")
        player.hand = Hand([Card(3, 0), Card(9, 1)])
        game.players = [player, Player("AI1", True), Player("AI2", True), Player("AI3", True)]
        game.current_player_index = 0
        game.first_turn = True
        handler = InputHandler()
        handler.selected_indices = {player.hand.cards.index(Card(3, 0))}
        self.assertTrue(handler.try_play(game))
        self.assertEqual(game.last_play, [Card(3, 0)])

    def test_button_lookup(self) -> None:
        handler = InputHandler()
        self.assertEqual(handler.button_at((25, 25)), "play")

    def test_app_init(self) -> None:
        app = BigTwoApp(seed=7, use_gui=False)
        self.assertEqual(len(app.game.players), 4)


if __name__ == "__main__":
    unittest.main()
