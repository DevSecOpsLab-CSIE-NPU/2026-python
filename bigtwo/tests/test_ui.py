import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

import unittest
from unittest.mock import Mock, patch
from game.models import Card

class TestUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import pygame
        pygame.init()
        pygame.font.init()

    def test_card_render(self):
        import pygame
        from game.ui.render import Renderer
        screen = pygame.Surface((800, 600))
        r = Renderer(screen)
        c = Card(14, 3)
        r.draw_card(c, 0, 0)

    def test_game_init(self):
        from game.ui.app import BigTwoApp
        app = BigTwoApp()
        self.assertEqual(len(app.game.players), 4)

if __name__ == "__main__":
    unittest.main()
