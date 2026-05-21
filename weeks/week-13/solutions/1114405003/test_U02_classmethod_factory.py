# 測試檔：test_U02_classmethod_factory.py
# 目標：針對 U02-classmethod-factory.py 撰寫單元測試
# 說明：
# 1) 驗證 Point 的多重構造器（from_string / from_list / origin）。
# 2) 驗證 classmethod 在繼承下會回傳子類別實例（cls 指向呼叫類）。
# 3) 驗證 CostTable 的 uniform、from_flat_string 與 total_cost 行為。

import importlib.util
import os
import unittest


def load_u02_module():
    """動態載入 U02 教學檔案，回傳模組物件。"""
    module_path = os.path.normpath(
        os.path.join(os.path.dirname(__file__), "..", "..", "in-class", "U02-classmethod-factory.py")
    )
    spec = importlib.util.spec_from_file_location("u02_classmethod_factory", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


U02 = load_u02_module()


class TestPointFactories(unittest.TestCase):
    """測試 Point 以及子類別 ColoredPoint 的 classmethod 工廠方法。"""

    def test_point_from_string(self):
        # 字串格式 "x,y" 應正確解析成整數座標。
        p = U02.Point.from_string("3,4")
        self.assertEqual((p.x, p.y), (3, 4))
        self.assertEqual(repr(p), "Point(3, 4)")

    def test_point_from_list(self):
        # list 格式 [x, y] 應正確建立物件。
        p = U02.Point.from_list([5, 6])
        self.assertEqual((p.x, p.y), (5, 6))

    def test_point_origin(self):
        # origin() 應建立 (0, 0)。
        p = U02.Point.origin()
        self.assertEqual((p.x, p.y), (0, 0))

    def test_classmethod_respects_subclass(self):
        # 由子類呼叫父類繼承來的 from_string，應回傳 ColoredPoint。
        cp = U02.ColoredPoint.from_string("7,8")
        self.assertIsInstance(cp, U02.ColoredPoint)
        self.assertEqual((cp.x, cp.y), (7, 8))
        self.assertEqual(cp.color, "black")


class TestCostTable(unittest.TestCase):
    """測試 CostTable 工廠方法與成本計算。"""

    def test_uniform_factory(self):
        # uniform(2) 應建立長度 36，且每個成本皆為 2。
        table = U02.CostTable.uniform(2)
        self.assertEqual(len(table.costs), 36)
        self.assertTrue(all(c == 2 for c in table.costs))

    def test_from_flat_string_factory(self):
        # 用 0..35 產生一行字串，檢查解析結果與索引成本。
        raw = " ".join(str(i) for i in range(36))
        table = U02.CostTable.from_flat_string(raw)
        self.assertEqual(len(table.costs), 36)
        self.assertEqual(table.cost_of(0), 0)
        self.assertEqual(table.cost_of(10), 10)
        self.assertEqual(table.cost_of(35), 35)

    def test_total_cost_zero_case(self):
        # n=0 時，依題目邏輯直接回傳 costs[0]。
        table = U02.CostTable.uniform(7)
        self.assertEqual(table.total_cost(0, 10), 7)

    def test_total_cost_uniform_digits_count(self):
        # 當所有字元成本都為 1，總成本等於位數。
        table = U02.CostTable.uniform(1)
        self.assertEqual(table.total_cost(255, 2), 8)    # 11111111
        self.assertEqual(table.total_cost(255, 16), 2)   # FF
        self.assertEqual(table.total_cost(255, 10), 3)   # 255


if __name__ == "__main__":
    unittest.main(verbosity=2)
