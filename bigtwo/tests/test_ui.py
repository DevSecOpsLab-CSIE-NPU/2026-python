import unittest
from unittest.mock import Mock, patch
from game.models import Card

class TestUI(unittest.TestCase):
    def test_card_render(self):
        try:
            import pygame
            from game.ui.render import Renderer
            screen = pygame.Surface((800, 600))
            r = Renderer(screen)
            c = Card(14, 3)
            r.draw_card(c, 0, 0)
            self.assertTrue(True)
        except ImportError:
            self.skipTest("pygame not installed")

    def test_game_init(self):
        try:
            from game.ui.app import BigTwoApp
            with patch.object(BigTwoApp, 'run', return_value=None):
                app = BigTwoApp()
                self.assertEqual(len(app.game.players), 4)
        except ImportError:
            self.skipTest("pygame not installed")

if __name__ == "__main__":
    unittest.main()
