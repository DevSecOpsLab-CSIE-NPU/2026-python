"""R02-property.py 的單元測試。"""

from __future__ import annotations

import math
import unittest

from support import load_module


class TestR02Property(unittest.TestCase):
    """確認 property 封裝範例的行為。"""

    @classmethod
    def setUpClass(cls):
        cls.module = load_module("R02-property.py")

    def test_circle_area_and_diameter_follow_radius(self):
        circle = self.module.Circle(5)

        self.assertEqual(5, circle.radius)
        self.assertAlmostEqual(math.pi * 25, circle.area)
        self.assertEqual(10, circle.diameter)

    def test_circle_radius_update_recomputes_area(self):
        circle = self.module.Circle(5)
        circle.radius = 10

        self.assertEqual(10, circle.radius)
        self.assertAlmostEqual(math.pi * 100, circle.area)

    def test_circle_rejects_negative_radius_in_init_and_setter(self):
        with self.assertRaises(ValueError):
            self.module.Circle(-1)

        circle = self.module.Circle(3)
        with self.assertRaises(ValueError):
            circle.radius = -2

    def test_circle_area_is_read_only(self):
        circle = self.module.Circle(4)

        with self.assertRaises(AttributeError):
            circle.area = 100

    def test_rectangle_area_and_perimeter_update_automatically(self):
        rectangle = self.module.Rectangle(4, 6)
        self.assertEqual(24, rectangle.area)
        self.assertEqual(20, rectangle.perimeter)

        rectangle.width = 8
        self.assertEqual(48, rectangle.area)
        self.assertEqual(28, rectangle.perimeter)


if __name__ == "__main__":
    unittest.main()
