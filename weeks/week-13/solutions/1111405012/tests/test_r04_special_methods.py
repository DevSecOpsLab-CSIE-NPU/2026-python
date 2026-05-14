"""R04-special-methods.py 的單元測試。"""

from __future__ import annotations

import contextlib
import io
import unittest

from support import load_module


class TestR04SpecialMethods(unittest.TestCase):
    """確認特殊方法範例已整理成可測試的模組。"""

    @classmethod
    def setUpClass(cls):
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            cls.module = load_module("R04-special-methods.py")
        cls.import_output = stream.getvalue()

    def test_import_has_no_side_effect_output(self):
        self.assertEqual("", self.import_output)

    def test_score_supports_ordering_and_repr(self):
        score_a = self.module.Score("Alice", 90)
        score_b = self.module.Score("Bob", 75)
        score_c = self.module.Score("Carol", 90)

        self.assertTrue(score_a > score_b)
        self.assertTrue(score_a == score_c)
        self.assertEqual("Score('Alice', 90)", repr(score_a))
        self.assertEqual(
            ["Bob", "Alice", "Carol"],
            [score.name for score in sorted([score_a, score_b, score_c])],
        )

    def test_score_comparison_with_other_type_is_safe(self):
        score = self.module.Score("Alice", 90)

        self.assertFalse(score == 90)
        with self.assertRaises(TypeError):
            score < 90

    def test_classroom_supports_len_contains_iter_and_repr(self):
        classroom = self.module.Classroom("資工一甲")
        classroom.add("Alice")
        classroom.add("Bob")
        classroom.add("Carol")

        self.assertEqual(3, len(classroom))
        self.assertIn("Alice", classroom)
        self.assertNotIn("Dave", classroom)
        self.assertEqual(["Alice", "Bob", "Carol"], list(classroom))
        self.assertEqual("Classroom('資工一甲', 3 人)", repr(classroom))


if __name__ == "__main__":
    unittest.main()
