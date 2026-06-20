import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

import unittest
from unittest.mock import Mock, patch
from models import Card

class TestUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import pygame
        pygame.init()
        pygame.font.init()

    def test_card_render(self):
        import pygame
        from render import Renderer
        screen = pygame.Surface((800, 600))
        r = Renderer(screen)
        c = Card(14, 3)
        r.draw_card(c, 0, 0)

    def test_game_init(self):
        from app import BigTwoApp
        app = BigTwoApp()
        self.assertEqual(len(app.game.players), 4)

    def test_hand_y_coords_match(self):
        from render import HAND_Y
        from input import InputHandler
        from render import Renderer as R
        self.assertEqual(HAND_Y, 380, "HAND_Y 撣豢? 380")

if __name__ == "__main__":
    unittest.main()
