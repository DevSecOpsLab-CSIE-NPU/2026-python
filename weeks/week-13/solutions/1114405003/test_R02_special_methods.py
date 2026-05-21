# 測試檔：test_R02_special_methods.py
# 目的：針對 R02-special-methods.py 的特殊方法主題撰寫單元測試
#
# 涵蓋重點：
# - __repr__ 與 __str__ 的輸出語意
# - __eq__ 自訂相等條件
# - @total_ordering 補齊比較運算子的行為
# - __slots__ 對動態屬性的限制

import importlib.util
import os
import unittest


def load_r02_module():
    """動態載入 R02 教學檔，回傳模組物件。"""
    module_path = os.path.join(os.path.dirname(__file__), "R02-special-methods.py")
    spec = importlib.util.spec_from_file_location("r02_special_methods", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


R02 = load_r02_module()


class TestR02SpecialMethods(unittest.TestCase):
    """測試 R02 的特殊方法實作是否符合預期。"""

    def test_student_repr_and_str(self):
        # __repr__：偏向開發者除錯資訊；__str__：偏向使用者閱讀格式。
        s = R02.Student("王小明", 85)
        self.assertEqual(repr(s), "Student(name='王小明', grade=85)")
        self.assertEqual(str(s), "王小明：85 分")

    def test_point_equality(self):
        # Point 物件以座標值作為相等判定依據。
        p1 = R02.Point(1, 2)
        p2 = R02.Point(1, 2)
        p3 = R02.Point(3, 4)
        self.assertTrue(p1 == p2)
        self.assertFalse(p1 == p3)

    def test_point_comparing_with_other_type(self):
        # __eq__ 對非 Point 會回傳 NotImplemented，
        # 實際使用 == 運算時通常得到 False。
        p = R02.Point(1, 2)
        self.assertFalse(p == (1, 2))

    def test_score_ordering_and_sort(self):
        # Score 使用 @total_ordering，只實作 __eq__ 與 __lt__，
        # 其餘比較應可自動運作。
        a = R02.Score(80)
        b = R02.Score(90)
        self.assertTrue(a < b)
        self.assertTrue(a <= b)
        self.assertFalse(a > b)

        # sorted() 應依 value 升冪排序。
        scores = [R02.Score(70), R02.Score(95), R02.Score(60)]
        sorted_values = [s.value for s in sorted(scores)]
        self.assertEqual(sorted_values, [60, 70, 95])

    def test_pointlite_slots_blocks_new_attributes(self):
        # PointLite 限制只能有 x、y；新增 z 應觸發 AttributeError。
        p = R02.PointLite(3, 4)
        self.assertEqual((p.x, p.y), (3, 4))
        with self.assertRaises(AttributeError):
            p.z = 5


if __name__ == "__main__":
    unittest.main(verbosity=2)
