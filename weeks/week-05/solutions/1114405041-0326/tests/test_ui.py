"""Phase 6：UI 測試（不依賴實際 pygame 視窗）。"""

from __future__ import annotations

import unittest

from ui.app import BigTwoApp
from ui.render import Renderer


class TestRenderer(unittest.TestCase):
    def test_card_render(self):
        r = Renderer()
        card_desc = r.draw_card(None, 10, 10)
        self.assertGreater(card_desc["w"], 0)
        self.assertGreater(card_desc["h"], 0)

    def test_hand_render(self):
        app = BigTwoApp()
        hand_desc = app.renderer.draw_hand(app.game.players[0].hand, 20, 300, [])
        self.assertIsInstance(hand_desc, list)


class TestAppIntegration(unittest.TestCase):
    def test_game_init(self):
        app = BigTwoApp()
        self.assertEqual(len(app.game.players), 4)

    def test_card_selection(self):
        app = BigTwoApp()
        ok = app.input_handler.handle_click((400, 300), app.game)
        self.assertTrue(ok)

    def test_button_click(self):
        app = BigTwoApp()
        # 點 play 按鈕區（20,20,100,40）
        ok = app.input_handler.handle_click((30, 30), app.game)
        self.assertIsInstance(ok, bool)

    def test_complete_flow(self):
        app = BigTwoApp()
        app.run(max_steps=5)
        state = app.render()
        self.assertIn("players", state)


if __name__ == "__main__":
    unittest.main(verbosity=2)
