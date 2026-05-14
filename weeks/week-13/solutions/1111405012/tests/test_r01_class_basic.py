"""R01-class-basic.py 的單元測試。"""

from __future__ import annotations

import unittest

from support import load_module


class TestR01ClassBasic(unittest.TestCase):
    """確認類別基礎範例已可穩定驗證。"""

    @classmethod
    def setUpClass(cls):
        cls.module = load_module("R01-class-basic.py")

    def setUp(self):
        self.original_school = self.module.Student.school

    def tearDown(self):
        self.module.Student.school = self.original_school

    def test_point_repr_str_and_distance(self):
        point_a = self.module.Point(0, 0)
        point_b = self.module.Point(3, 4)

        self.assertEqual("Point(0, 0)", repr(point_a))
        self.assertEqual("(3, 4)", str(point_b))
        self.assertEqual(5.0, point_a.distance_to(point_b))

    def test_point_distance_to_self_is_zero(self):
        point = self.module.Point(7, -2)

        self.assertEqual(0.0, point.distance_to(point))

    def test_student_greeting_uses_class_variable(self):
        student = self.module.Student("王小明", "11144050001")

        self.assertIn(self.module.Student.school, student.greeting())
        self.assertEqual("Student(11144050001, 王小明)", repr(student))

    def test_updating_school_affects_all_instances(self):
        student_a = self.module.Student("王小明", "11144050001")
        student_b = self.module.Student("李小華", "11144050002")

        self.module.Student.school = "NPU"

        self.assertEqual("NPU", student_a.school)
        self.assertEqual("NPU", student_b.school)
        self.assertEqual("我是 NPU 的 王小明", student_a.greeting())


if __name__ == "__main__":
    unittest.main()
