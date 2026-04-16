import unittest
from unittest.mock import MagicMock, patch
from game.models import Card, Hand
from game.game import BigTwoGame


def C(rank, suit):
    return Card(rank, suit)


class TestRendererBasic(unittest.TestCase):
    """Test Renderer without requiring pygame to be installed."""

    def test_card_render_no_crash(self):
        from ui.render import Renderer
        r = Renderer(screen=None)
        # Should not raise even without pygame screen
        r.draw_card(C(14, 3), 0, 0)

    def test_hand_render_no_crash(self):
        from ui.render import Renderer
        r = Renderer(screen=None)
        h = Hand([C(14, 3), C(13, 2), C(3, 0)])
        r.draw_hand(h, 0, 0, [])


class TestAppInit(unittest.TestCase):

    @patch('ui.app.PYGAME_AVAILABLE', False)
    def test_game_init(self):
        from ui.app import BigTwoApp
        app = BigTwoApp()
        self.assertEqual(len(app.game.players), 4)

    @patch('ui.app.PYGAME_AVAILABLE', False)
    def test_card_selection_skipped_without_pygame(self):
        from ui.app import BigTwoApp
        app = BigTwoApp()
        # No crash when pygame is not available
        self.assertIsNone(app.input_handler)

    @patch('ui.app.PYGAME_AVAILABLE', False)
    def test_run_without_pygame(self):
        from ui.app import BigTwoApp
        app = BigTwoApp()
        # run() should print message and return without crashing
        app.run()


if __name__ == '__main__':
    unittest.main()
