# 測試檔：test_U01_closures_traps.py
# 目標：針對 U01-closures-traps.py 撰寫單元測試
# 說明：
# 1) 驗證「可變預設值」陷阱是否如題目描述會共用同一個 list。
# 2) 驗證 add_to_cart_safe 使用 None 預設值後，每次呼叫都有獨立容器。
# 3) 驗證閉包延遲綁定（funcs）與修正版（funcs_ok）的差異。
# 4) 驗證 nonlocal 閉包狀態是否正確累加與彼此獨立。
# 5) 驗證 visit tracker 是否可記住已拜訪節點。

import importlib.util
import os
import unittest


def load_u01_module():
    """動態載入 U01 教學檔案，回傳模組物件。"""
    module_path = os.path.normpath(
        os.path.join(os.path.dirname(__file__), "..", "..", "in-class", "U01-closures-traps.py")
    )
    spec = importlib.util.spec_from_file_location("u01_closures_traps", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


U01 = load_u01_module()


class TestMutableDefaultArgumentTrap(unittest.TestCase):
    """測試可變預設值 cart=[] 的共享陷阱。"""

    def test_add_to_cart_shares_default_list(self):
        # 先重置函式預設值，避免受其他測試或匯入時呼叫污染。
        U01.add_to_cart.__defaults__ = ([],)

        first = U01.add_to_cart("蘋果")
        second = U01.add_to_cart("香蕉")
        third = U01.add_to_cart("葡萄")

        # 三次呼叫會累積在同一個 list 上，這正是題目示範的陷阱。
        self.assertEqual(first, ["蘋果", "香蕉", "葡萄"])
        self.assertIs(first, second)
        self.assertIs(second, third)

    def test_add_to_cart_safe_creates_new_list_each_call(self):
        # safe 版本使用 None 當預設值，應該每次都建立新 list。
        a = U01.add_to_cart_safe("蘋果")
        b = U01.add_to_cart_safe("香蕉")

        self.assertEqual(a, ["蘋果"])
        self.assertEqual(b, ["香蕉"])
        self.assertIsNot(a, b)

    def test_add_to_cart_safe_can_use_external_list(self):
        # 若外部傳入既有 list，函式會在該 list 上 append。
        external = ["原本"]
        result = U01.add_to_cart_safe("新項目", external)
        self.assertIs(result, external)
        self.assertEqual(result, ["原本", "新項目"])


class TestClosureBindingAndNonlocal(unittest.TestCase):
    """測試閉包延遲綁定與 nonlocal 狀態更新。"""

    def test_late_binding_funcs_all_use_final_i(self):
        # funcs 內 lambda 都引用同一個 i 名稱，迴圈結束後 i=4。
        values = [f() for f in U01.funcs]
        self.assertEqual(values, [4, 4, 4, 4, 4])

    def test_funcs_ok_capture_values_correctly(self):
        # funcs_ok 透過 lambda i=i 固定當下值，結果應為 0..4。
        values = [f() for f in U01.funcs_ok]
        self.assertEqual(values, [0, 1, 2, 3, 4])

    def test_make_counter_independent_states(self):
        # 兩個 counter 彼此狀態獨立。
        c1 = U01.make_counter()
        c2 = U01.make_counter(10)

        self.assertEqual(c1(), 1)
        self.assertEqual(c1(), 2)
        self.assertEqual(c2(), 11)
        self.assertEqual(c2(), 12)
        self.assertEqual(c1(), 3)

    def test_visit_tracker_records_seen_nodes(self):
        # visit tracker 第一次看到節點回傳 True，再次看到同節點回傳 False。
        visit = U01.make_visit_tracker()
        result = [visit(n) for n in [1, 2, 1, 3, 2, 4]]
        self.assertEqual(result, [True, True, False, True, False, True])


if __name__ == "__main__":
    unittest.main(verbosity=2)
