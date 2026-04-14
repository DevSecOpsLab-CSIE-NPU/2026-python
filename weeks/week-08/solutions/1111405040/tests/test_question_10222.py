"""
UVA 10222 測試。
"""

from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import question_10222


class TestQuestion10222(unittest.TestCase):
    """測試 Decode the Mad man。"""

    def test_decode_known_phrase(self) -> None:
        self.assertEqual(question_10222.decode_text("k[r dyt I[o"), "how are you")

    def test_spaces_and_newlines_are_preserved(self) -> None:
        self.assertEqual(question_10222.solve("k[r\n"), "how\n")

    def test_punctuation_is_decoded_by_keyboard_position(self) -> None:
        self.assertEqual(question_10222.decode_text("]"), "p")


if __name__ == "__main__":
    unittest.main()
