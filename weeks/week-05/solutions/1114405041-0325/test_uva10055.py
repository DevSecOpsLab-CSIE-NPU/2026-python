from __future__ import annotations

import importlib.util
import pathlib
import unittest

from uva10055 import absolute_difference, solve_io as solve_main


def _load_easy():
    path = pathlib.Path(__file__).parent / "uva10055-easy.py"
    spec = importlib.util.spec_from_file_location("uva10055_easy_dynamic", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load easy module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


EASY = _load_easy()
solve_easy = EASY.solve_io


class TestUVA10055(unittest.TestCase):
    def test_abs_diff(self):
        self.assertEqual(absolute_difference(10, 12), 2)
        self.assertEqual(absolute_difference(100, 30), 70)

    def test_full_io(self):
        data = "10 12\n100 30\n0 0\n"
        expected = "2\n70\n0"
        self.assertEqual(solve_main(data), expected)
        self.assertEqual(solve_easy(data), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
