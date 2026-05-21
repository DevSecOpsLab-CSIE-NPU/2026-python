# 測試檔：test_R03_property.py
# 目的：針對 R03-property.py 的 @property 教學內容撰寫單元測試
#
# 重點說明：
# 1) 驗證 @property 的 getter / setter 是否正確運作。
# 2) 驗證 setter 的資料驗證（合法值通過、非法值拋出 ValueError）。
# 3) 驗證唯讀屬性（例如 Circle.area）不可直接指定。
# 4) 驗證子類別覆寫 setter 後，驗證範圍是否正確改變。
#
# 註：原始教學檔在匯入時會直接執行示範 print，屬於預期行為，不影響測試。

import importlib.util
import os
import unittest


def load_r03_module():
    """動態載入 R03-property.py，回傳模組物件。"""
    module_path = os.path.normpath(
        os.path.join(os.path.dirname(__file__), "..", "..", "in-class", "R03-property.py")
    )
    spec = importlib.util.spec_from_file_location("r03_property", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


R03 = load_r03_module()


class TestStudentProperty(unittest.TestCase):
    """測試 Student 的成績屬性（含 getter/setter 與資料驗證）。"""

    def test_student_init_calls_setter(self):
        # 建構子內 self.grade = grade 會觸發 setter。
        # 因此合法成績應該可正常建立，並存進內部欄位 _grade。
        s = R03.Student("李大華", 90)
        self.assertEqual(s.grade, 90)
        self.assertEqual(s._grade, 90)

    def test_student_set_valid_grade(self):
        # 合法範圍 0~100 的值應可成功設定。
        s = R03.Student("王小明", 80)
        s.grade = 100
        self.assertEqual(s.grade, 100)

        s.grade = 0
        self.assertEqual(s.grade, 0)

    def test_student_set_invalid_grade_raises(self):
        # 非法值（小於 0 或大於 100）應拋出 ValueError。
        s = R03.Student("王小明", 80)

        with self.assertRaises(ValueError):
            s.grade = -1

        with self.assertRaises(ValueError):
            s.grade = 101

    def test_student_init_invalid_grade_raises(self):
        # 建構子傳入非法成績，因為會走 setter，應直接失敗。
        with self.assertRaises(ValueError):
            R03.Student("小美", -10)


class TestCircleReadOnlyProperty(unittest.TestCase):
    """測試 Circle 的計算型唯讀屬性（area、diameter）。"""

    def test_circle_area_and_diameter(self):
        # 使用 assertAlmostEqual 驗證浮點數，避免小數誤差造成誤判。
        c = R03.Circle(5)
        self.assertEqual(c.diameter, 10)
        self.assertAlmostEqual(c.area, 78.53981633974483, places=10)

    def test_circle_area_updates_when_radius_changes(self):
        # area 與 diameter 是由 radius 即時計算，不是固定儲存值。
        c = R03.Circle(5)
        c.radius = 10
        self.assertEqual(c.diameter, 20)
        self.assertAlmostEqual(c.area, 314.1592653589793, places=10)

    def test_circle_area_is_read_only(self):
        # Circle.area 沒有 setter，直接指定應拋出 AttributeError。
        c = R03.Circle(3)
        with self.assertRaises(AttributeError):
            c.area = 100


class TestGradStudentOverrideSetter(unittest.TestCase):
    """測試 GradStudent 覆寫後的成績驗證範圍（0~150）。"""

    def test_gradstudent_allows_extended_range(self):
        # 研究生允許超過 100 分，只要不超過 150。
        g = R03.GradStudent("張教授", 120)
        self.assertEqual(g.grade, 120)

        g.grade = 150
        self.assertEqual(g.grade, 150)

    def test_gradstudent_rejects_out_of_range(self):
        # 研究生若小於 0 或大於 150，一樣應拋出 ValueError。
        g = R03.GradStudent("研究生", 100)

        with self.assertRaises(ValueError):
            g.grade = -5

        with self.assertRaises(ValueError):
            g.grade = 151


if __name__ == "__main__":
    unittest.main(verbosity=2)
