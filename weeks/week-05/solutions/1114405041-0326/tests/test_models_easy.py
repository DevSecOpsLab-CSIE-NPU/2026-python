"""Phase 1 -easy 版本模型測試。

此檔用動態載入方式測試 models-easy.py（檔名含連字號）。
"""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import unittest


def load_easy_module():
    root = Path(__file__).resolve().parents[1]
    target = root / "game" / "models-easy.py"
    spec = spec_from_file_location("models_easy_dash", target)
    if spec is None or spec.loader is None:
        raise RuntimeError("無法載入 models-easy.py")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M = load_easy_module()
Card = M.Card
Deck = M.Deck
Hand = M.Hand
Player = M.Player


class TestEasyModel(unittest.TestCase):
    def test_easy_card_repr(self):
        self.assertEqual(repr(Card(14, 3)), "♠A")

    def test_easy_deck_52(self):
        d = Deck()
        self.assertEqual(len(d.cards), 52)

    def test_easy_hand_sort(self):
        h = Hand([Card(3, 0), Card(14, 3), Card(3, 3), Card(13, 2)])
        h.sort_desc()
        self.assertEqual(h, [Card(14, 3), Card(13, 2), Card(3, 0), Card(3, 3)])

    def test_easy_player_play(self):
        p = Player("EASY")
        c1, c2 = Card(3, 0), Card(14, 3)
        p.take_cards([c1, c2])
        out = p.play_cards([c2])
        self.assertEqual(out, [c2])
        self.assertEqual(p.hand, [c1])


if __name__ == "__main__":
    unittest.main()
