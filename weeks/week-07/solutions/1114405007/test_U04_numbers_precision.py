"""
U04. 數字精度的陷阱與選擇 - 單元測試
====================================
測試重點：
1. 銀行家捨入（四捨六入五取偶）
2. NaN 無法用 == 比較
3. float vs Decimal 的精度差異
"""

import unittest
import math
from decimal import Decimal, ROUND_HALF_UP


class TestNumbersPrecision(unittest.TestCase):
    """數字精度的陷阱與選擇的單元測試"""

    def test_banker_rounding_python_round(self):
        """測試：Python 的 round() 使用銀行家捨入（四捨六入五取偶）"""
        # 五時取偶：0.5 → 0（最近的偶數），2.5 → 2（最近的偶數）
        self.assertEqual(round(0.5), 0)
        self.assertEqual(round(2.5), 2)
        self.assertEqual(round(3.5), 4)  # 往上取到偶數
        
        # 小數位數時也適用
        self.assertEqual(round(1.15, 1), 1.1)  # 往下到偶數位
        self.assertEqual(round(1.25, 1), 1.2)  # 往下到偶數位

    def test_traditional_rounding_with_decimal(self):
        """測試：傳統四捨五入（用 Decimal + ROUND_HALF_UP）"""
        def trad_round(x: float, n: int = 0) -> Decimal:
            d = Decimal(str(x))
            fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)
            return d.quantize(fmt, rounding=ROUND_HALF_UP)
        
        # 傳統四捨五入：0.5 → 1，2.5 → 3
        self.assertEqual(trad_round(0.5), Decimal("1"))
        self.assertEqual(trad_round(2.5), Decimal("3"))

    def test_nan_comparison_fails(self):
        """測試：NaN 無法用 == 比較（自己不等於自己）"""
        c = float("nan")
        
        # 嚴格來說，NaN != NaN
        self.assertFalse(c == c)
        self.assertFalse(float("nan") == float("nan"))

    def test_nan_detection_with_isnan(self):
        """測試：檢測 NaN 必須用 math.isnan()"""
        c = float("nan")
        
        # 唯一正確的檢測方式
        self.assertTrue(math.isnan(c))
        
        # 正常數字不是 NaN
        self.assertFalse(math.isnan(1.0))
        self.assertFalse(math.isnan(0.0))

    def test_filter_nan_from_list(self):
        """測試：從列表中過濾 NaN"""
        data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
        clean = [x for x in data if not math.isnan(x)]
        
        self.assertEqual(clean, [1.0, 3.0, 5.0])

    def test_float_precision_issue(self):
        """測試：float 的精度問題"""
        # 0.1 + 0.2 != 0.3（浮點誤差）
        result = 0.1 + 0.2
        self.assertNotEqual(result, 0.3)
        self.assertAlmostEqual(result, 0.3, places=15)

    def test_decimal_precision_exact(self):
        """測試：Decimal 的精確計算"""
        # Decimal 計算精確
        result = Decimal("0.1") + Decimal("0.2")
        self.assertEqual(result, Decimal("0.3"))

    def test_float_vs_decimal_choice(self):
        """測試：float vs Decimal 的選擇"""
        # float：快但有誤差（科學/工程適用）
        x = 0.1
        y = 0.2
        # 需要考慮誤差
        self.assertAlmostEqual(x + y, 0.3, places=15)
        
        # Decimal：精確但慢（金融/會計適用）
        x_d = Decimal("0.1")
        y_d = Decimal("0.2")
        self.assertEqual(x_d + y_d, Decimal("0.3"))


if __name__ == "__main__":
    unittest.main()
