# 測試檔：test_U01_number_theory.py
# 目的：為 `U01-number-theory.py` 中的函式撰寫單元測試
# 使用內建的 unittest，並以繁體中文註解說明測試案例意圖

import os
import importlib.util
import unittest

# 動態載入同目錄下的模組（檔名包含連字號，無法以直接 import）
MODULE_PATH = os.path.join(os.path.dirname(__file__), 'U01-number-theory.py')
spec = importlib.util.spec_from_file_location('u01_nt', MODULE_PATH)
u01 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(u01)


class TestBeatTheSpread(unittest.TestCase):
    """測試 Beat the Spread 的各種情況（有解 / 無解 / 邊界）"""

    def test_normal_cases(self):
        # 典型可解情況
        self.assertEqual(u01.beat_the_spread(40, 20), (30, 10))
        self.assertEqual(u01.beat_the_spread(10, 10), (10, 0))

    def test_impossible_cases(self):
        # 差值大於總和或奇偶性不符，應無解
        self.assertIsNone(u01.beat_the_spread(20, 40))
        self.assertIsNone(u01.beat_the_spread(10, 11))

    def test_negative_low(self):
        # 當低分為負（例如 s < d）應回傳 None
        self.assertIsNone(u01.beat_the_spread(5, 7))


class TestNineDegree(unittest.TestCase):
    """測試 nine_degree 對大數字字串的處理與深度計算"""

    def test_single_digit_nine(self):
        # "9" 應為 9 的倍數，9-degree = 1
        self.assertEqual(u01.nine_degree("9"), (True, 1))

    def test_multi_digit_cases(self):
        # 18 -> 9 (深度 1)，999 -> 27 -> 9 (深度 2)
        self.assertEqual(u01.nine_degree("18"), (True, 1))
        self.assertEqual(u01.nine_degree("999"), (True, 2))

    def test_not_multiple_of_nine(self):
        # 100 的數位和為 1，不是 9 的倍數
        self.assertEqual(u01.nine_degree("100"), (False, -1))

    def test_large_case(self):
        # 729 -> 18 -> 9（深度 2）
        self.assertEqual(u01.nine_degree("729"), (True, 2))


class TestPositionAndSteps(unittest.TestCase):
    """測試螺旋座標 position 與 steps 的正確性"""

    def test_position_examples(self):
        # 使用檔案內範例檢查 position
        self.assertEqual(u01.position(0, 3), 9)
        self.assertEqual(u01.position(3, 0), 12)
        self.assertEqual(u01.position(2, 2), 6)

    def test_steps_examples(self):
        # 檔案中提供的步數範例
        self.assertEqual(u01.steps(0, 3, 3, 0), abs(u01.position(3,0) - u01.position(0,3)))
        self.assertEqual(u01.steps(0, 0, 2, 2), abs(u01.position(2,2) - u01.position(0,0)))
        self.assertEqual(u01.steps(1, 1, 2, 3), abs(u01.position(2,3) - u01.position(1,1)))


if __name__ == '__main__':
    unittest.main()
