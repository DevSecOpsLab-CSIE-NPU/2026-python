import unittest
from unittest.mock import MagicMock, patch
import pygame
from game.models import Card, Player
from ui.render import Renderer

class TestUI(unittest.TestCase):
    @patch('pygame.font.SysFont')
    @patch('pygame.font.Font')
    def setUp(self, mock_font, mock_sysfont):
        pygame.init()
        
        fake_text_surface = pygame.Surface((50, 20))
        
        mock_font_instance = MagicMock()
        mock_font_instance.render.return_value = fake_text_surface
        
        mock_sysfont.return_value = mock_font_instance
        mock_font.return_value = mock_font_instance
        
        self.mock_surface = pygame.Surface((1000, 700))
        self.renderer = Renderer()

    def test_ui_proportions(self):
        self.assertEqual(self.renderer.SCREEN_SIZE, (1000, 700))
        self.assertTrue(self.renderer.CARD_W > 50)
        self.assertTrue(self.renderer.CARD_H > 80)

    def test_draw_single_card_no_crash(self):
        card = Card(14, 3)
        try:
            self.renderer._draw_card_entity(self.mock_surface, card, 100, 100, is_selected=True)
            success = True
        except Exception as e:
            print(f"Error: {e}")
            success = False
        self.assertTrue(success)

    def test_draw_hud_ai_gold_hidden(self):
        human = Player("You")
        human.hand = [Card(3, 0)] * 13
        ai = Player("Alice", is_ai=True)
        ai.hand = [Card(3, 0)] * 5 
        
        try:
            # [修正] 補上缺少的 player_avatar_indices 參數 (傳入模擬的頭像編號 [0, 1])
            self.renderer.draw_hud(self.mock_surface, [human, ai], 0, [0, 1])
            success = True
        except Exception as e:
            print(f"Error: {e}")
            success = False
        self.assertTrue(success)

    def test_draw_scene_table_center(self):
        try:
            self.renderer.draw_scene(self.mock_surface)
            last_play = [Card(3,0), Card(4,1), Card(5,2), Card(6,3), Card(7,0)]
            self.renderer.draw_table_cards(self.mock_surface, last_play)
            success = True
        except Exception as e:
            print(f"Error: {e}")
            success = False
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()