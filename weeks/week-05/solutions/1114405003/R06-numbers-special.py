# -*- coding: utf-8 -*-
"""
R06. 特殊數值 - 單元測試程式

【學習目標】
本程式針對 Python 特殊數值運算進行單元測試，包括：
1. 無窮大（inf）與 NaN（非數值）
2. 分數運算（Fraction）
3. 隨機數產生（random）

【重要概念】
- float("inf") 與 float("-inf") 表示無窮大
- float("nan") 表示 Not a Number
- NaN 不等於自己（NaN != NaN 永遠為 True）
- Fraction 進行精確分數運算
- random 模組產生隨機數
"""

import unittest
import math
import random
from fractions import Fraction


class TestInfinityAndNaN(unittest.TestCase):
    """測試無窮大與 NaN"""

    def test_infinity_basic(self):
        """
        【測試1】建立無窮大

        float("inf") → 正無窮大
        float("-inf") → 負無窮大

        注意：是字串 "inf"，不是 inf 變數！
        """
        pos_inf = float("inf")
        neg_inf = float("-inf")

        self.assertTrue(math.isinf(pos_inf))
        self.assertTrue(math.isinf(neg_inf))
        self.assertGreater(pos_inf, 0)
        self.assertLess(neg_inf, 0)

    def test_nan_basic(self):
        """
        【測試2】建立 NaN（非數值）

        float("nan") → NaN（Not a Number）

        常見產生 NaN 的情況：
        - 0 / 0
        - inf - inf
        - sqrt(-1)
        """
        nan = float("nan")
        self.assertTrue(math.isnan(nan))

    def test_nan_not_equal_to_itself(self):
        """
        【測試3】NaN 不等於自己（重要特性！）

        NaN 是唯一一個不等於自己的值！

        這是 IEEE 754 浮點數標準的規定。
        用來判斷是否為 NaN：使用 math.isnan()，不要用 ==
        """
        nan = float("nan")
        # NaN != NaN 永遠為 True
        self.assertNotEqual(nan, nan)
        # 正確的判斷方式
        self.assertTrue(math.isnan(nan))

    def test_infinity_operations(self):
        """
        【測試4】無窮大的運算

        inf + 任意數 = inf
        inf + inf = inf
        inf - inf = nan
        inf / inf = nan
        """
        pos_inf = float("inf")
        neg_inf = float("-inf")

        # inf + 正數 = inf
        self.assertEqual(pos_inf + 45, float("inf"))
        # 任意正數 / inf = 0
        self.assertEqual(10 / pos_inf, 0.0)
        # inf / inf = nan
        self.assertTrue(math.isnan(pos_inf / pos_inf))
        # inf + (-inf) = nan
        self.assertTrue(math.isnan(pos_inf + neg_inf))

    def test_isinf_isnan_functions(self):
        """
        【測試5】math.isinf() 和 math.isnan() 函數
        """
        pos_inf = float("inf")
        nan = float("nan")

        self.assertTrue(math.isinf(pos_inf))
        self.assertFalse(math.isinf(nan))
        self.assertTrue(math.isnan(nan))
        self.assertFalse(math.isnan(pos_inf))


class TestFractionOperations(unittest.TestCase):
    """測試分數運算"""

    def test_fraction_creation(self):
        """
        【測試6】建立分數

        Fraction(分子, 分母)

        範例：
        Fraction(5, 4) → 5/4 = 1.25
        """
        p = Fraction(5, 4)
        self.assertEqual(p.numerator, 5)
        self.assertEqual(p.denominator, 4)

    def test_fraction_arithmetic(self):
        """
        【測試7】分數運算

        分數支援 +、-、*、/ 運算，結果自動約分
        """
        p = Fraction(5, 4)
        q = Fraction(7, 16)

        # 加法：5/4 + 7/16 = 20/16 + 7/16 = 27/16
        self.assertEqual(p + q, Fraction(27, 16))

        # 乘法：5/4 * 7/16 = 35/64
        r = p * q
        self.assertEqual(r.numerator, 35)
        self.assertEqual(r.denominator, 64)

    def test_fraction_to_float(self):
        """
        【測試8】分數轉浮點數
        """
        r = Fraction(35, 64)
        self.assertAlmostEqual(float(r), 0.546875)

    def test_fraction_limit_denominator(self):
        """
        【測試9】限制分母大小

        limit_denominator(最大分母)

        找到最接近的分數，且分母不大於指定值

        範例：
        Fraction('3.1415926535').limit_denominator(1000)
        → Fraction(355, 113)
        """
        pi_approx = Fraction("3.1415926535")
        result = pi_approx.limit_denominator(10)
        self.assertEqual(result, Fraction(22, 7))

        # 另一個例子：0.546875 ≈ 4/7（分母≤8）
        r = Fraction(35, 64)
        limited = r.limit_denominator(8)
        self.assertEqual(limited, Fraction(4, 7))

    def test_fraction_from_float(self):
        """
        【測試10】從浮點數建立分數

        Fraction(*(3.75).as_integer_ratio())

        as_integer_ratio() 回傳 (分子, 分母) 的 tuple
        """
        f = 3.75
        frac = Fraction(*f.as_integer_ratio())
        self.assertEqual(frac, Fraction(15, 4))


class TestRandomOperations(unittest.TestCase):
    """測試隨機數產生"""

    def test_random_choice(self):
        """
        【測試11】隨機選擇一個元素

        random.choice(序列)

        從序列中隨機選擇一個元素
        """
        values = [1, 2, 3, 4, 5, 6]
        result = random.choice(values)
        self.assertIn(result, values)

    def test_random_sample(self):
        """
        【測試12】隨機不重複取樣

        random.sample(序列, 數量)

        隨機取出不重複的 n 個元素
        """
        values = [1, 2, 3, 4, 5, 6]
        result = random.sample(values, 3)

        # 確保取到 3 個
        self.assertEqual(len(result), 3)
        # 確保不重複
        self.assertEqual(len(set(result)), 3)
        # 確保都在原始序列中
        for v in result:
            self.assertIn(v, values)

    def test_random_shuffle(self):
        """
        【測試13】隨機洗牌

        random.shuffle(序列)

        原地打亂序列順序
        """
        values = [1, 2, 3, 4, 5, 6]
        original = values.copy()
        random.shuffle(values)

        # 確保元素相同
        self.assertEqual(sorted(values), sorted(original))

    def test_random_randint(self):
        """
        【測試14】隨機整數

        random.randint(a, b)

        產生 [a, b] 區間的隨機整數（包含兩端）
        """
        result = random.randint(0, 10)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 10)

    def test_random_seed(self):
        """
        【測試15】固定隨機種子

        random.seed(數值)

        設定種子後，隨機數會變得可重現
        """
        # 設定相同種子
        random.seed(42)
        result1 = random.random()

        random.seed(42)
        result2 = random.random()

        # 結果相同
        self.assertEqual(result1, result2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
