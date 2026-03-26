# -*- coding: utf-8 -*-
"""
R05. 數字基礎 - 單元測試程式

【學習目標】
本程式針對 Python 數字運算的各種操作進行單元測試，包括：
1. 四捨五入與銀行家捨入
2. 精確浮點數運算（Decimal）
3. 數字格式化輸出
4. 二進制、八進制、十六進制轉換

【重要概念】
- round() 使用銀行家捨入（banker's rounding）
- 浮點數有精度問題，需用 Decimal 做精確運算
- format() 可控制數字輸出格式
- bin()、oct()、hex() 進行進制轉換
"""

import unittest
from decimal import Decimal, localcontext
import math


class TestRoundingOperations(unittest.TestCase):
    """測試四捨五入相關操作"""

    def test_round_basic(self):
        """
        【測試1】基本四捨五入

        說明：round(數字, 小數位數) 用來做四捨五入。
        - round(1.27, 1) → 1.3（對小數點後第1位四捨五入）
        - round(1.25361, 3) → 1.254（對小數點後第3位四捨五入）
        """
        # 基本四捨五入
        self.assertEqual(round(1.27, 1), 1.3)
        self.assertEqual(round(1.25361, 3), 1.254)
        # 整數四捨五入
        self.assertEqual(round(1.5), 2)
        self.assertEqual(round(2.5), 2)

    def test_round_bankers_rounding(self):
        """
        【測試2】銀行家捨入（Banker's Rounding）

        重要：Python 的 round() 使用「銀行家捨入」！

        什麼是銀行家捨入？
        - 傳統四捨五入：0.5 → 1
        - 銀行家捨入：0.5 → 取「最近的偶數」
          - round(0.5) → 0（因為 0 是偶數）
          - round(1.5) → 2（因為 2 是偶數）
          - round(2.5) → 2（因為 2 是偶數）
          - round(3.5) → 4（因為 4 是偶數）

        這種方式在統計上更公平，避免 systematic bias。
        """
        # 銀行家捨入：0.5 取最近的偶數
        self.assertEqual(round(0.5), 0)  # 0.5 → 0
        self.assertEqual(round(2.5), 2)  # 2.5 → 2
        self.assertEqual(round(1.5), 2)  # 1.5 → 2
        self.assertEqual(round(3.5), 4)  # 3.5 → 4

    def test_round_negative(self):
        """
        【測試3】負數的四捨五入

        負數的四捨五入要注意：
        - round(-1.5) → -2（向遠離零的方向捨入）
        """
        self.assertEqual(round(-1.5), -2)
        self.assertEqual(round(-0.5), 0)

    def test_round_to_digit(self):
        """
        【測試4】對整數位做四捨五入

        語法：round(數字, -n) 表示對第 n 位數做四捨五入

        範例：
        - round(1627731, -2) → 1627700（對百位四捨五入）
        - round(1627731, -3) → 1628000（對千位四捨五入）
        - round(1627731, -4) → 1630000（對萬位四捨五入）
        """
        # 對百位四捨五入
        self.assertEqual(round(1627731, -2), 1627700)
        # 對千位四捨五入
        self.assertEqual(round(1627731, -3), 1628000)
        # 對萬位四捨五入
        self.assertEqual(round(1234567, -4), 1230000)


class TestExactFloatingPoint(unittest.TestCase):
    """測試精確浮點數運算"""

    def test_float_precision_problem(self):
        """
        【測試5】浮點數精度問題

        為什麼 4.2 + 2.1 不是 6.3？

        原因：電腦用二進制儲存小數，但有些小數在二進制是無窮小数：
        - 0.1 在二進制 = 0.0001100110011001100...（無限循環）
        - 所以 0.1 + 0.2 實際是 0.30000000000000004

        這不是 Python 的 bug，是 IEEE 754 浮點數標準的限制。
        """
        # 浮點數運算有誤差
        result = 4.2 + 2.1
        # 不能直接用 == 比較浮點數
        self.assertNotEqual(result, 6.3)
        # 應該用近似比較
        self.assertAlmostEqual(result, 6.3, places=10)

    def test_decimal_exact_calculation(self):
        """
        【測試6】使用 Decimal 進行精確計算

        解決方案：使用 decimal.Decimal 類別！

        重要：
        - 建立 Decimal 時，傳入字串而非數字！
        - Decimal("4.2") 是精確的 4.2
        - Decimal(4.2) 會繼承浮點數的誤差！

        範例：
        - Decimal("4.2") + Decimal("2.1") → Decimal("6.3")
        """
        # 建立精確的 Decimal（傳入字串！）
        da = Decimal("4.2")
        db = Decimal("2.1")
        # 加法結果是精確的 6.3
        self.assertEqual(da + db, Decimal("6.3"))

    def test_decimal_from_string_not_float(self):
        """
        【測試7】Decimal 傳入字串 vs 傳入浮點數

        重要差異：
        - Decimal("0.1") → Decimal("0.1")（精確）
        - Decimal(0.1) → Decimal('0.1000000000000000055511151231257827021181583404541015625')
        """
        # 傳入字串：精確值
        d_str = Decimal("0.1")
        self.assertEqual(d_str, Decimal("0.1"))

        # 傳入浮點數：繼承誤差
        d_float = Decimal(0.1)
        # 這是一個很長的小數
        self.assertGreater(len(str(d_float)), 10)

    def test_decimal_precision_control(self):
        """
        【測試8】控制 Decimal 精度

        使用 localcontext() 暫時改變精度：
        - ctx.prec = 3 表示有效數字為 3 位
        - Decimal("1.3") / Decimal("1.7") → Decimal('0.764705...')
          設定精度 3 後 → Decimal('0.765')
        """
        with localcontext() as ctx:
            ctx.prec = 3  # 設定有效數字為 3 位
            result = Decimal("1.3") / Decimal("1.7")
            self.assertEqual(result, Decimal("0.765"))

    def test_math_fsum(self):
        """
        【測試9】math.fsum 修正大數加小數的精度問題

        問題：1.23e18 + 1 - 1.23e18 用普通加法可能得到錯誤結果

        原因：當數字差距太大時，浮點數無法準確表示小數

        解決：使用 math.fsum()，它使用更精確的演算法

        範例：
        - 1.23e18 + 1 - 1.23e18 → 應該 = 1.0
        """
        result = math.fsum([1.23e18, 1, -1.23e18])
        self.assertEqual(result, 1.0)


class TestNumberFormatting(unittest.TestCase):
    """測試數字格式化輸出"""

    def test_format_decimal_places(self):
        """
        【測試10】格式化小數位數

        語法：format(數字, "小數位數f")
        - "0.2f" → 保留 2 位小數，四捨五入
        - "0.3f" → 保留 3 位小數

        範例：
        - format(1234.56789, "0.2f") → '1234.57'
        - format(1234.56789, "0.3f") → '1234.568'
        """
        x = 1234.56789
        self.assertEqual(format(x, "0.2f"), "1234.57")
        self.assertEqual(format(x, "0.3f"), "1234.568")

    def test_format_alignment(self):
        """
        【測試11】格式化對齊

        語法：format(數字, "寬度.小數位數f")
        - ">" → 右對齊（預設）
        - "<" → 左對齊
        - "^" → 置中

        範例：
        - format(1234.6, ">10.1f") → '    1234.6'（右對齊，總寬10）
        - format(1234.6, "<10.1f") → '1234.6    '（左對齊）
        """
        x = 1234.56789
        # 右對齊
        result = format(x, ">10.1f")
        self.assertEqual(result, "    1234.6")
        self.assertEqual(len(result), 10)

        # 左對齊
        result_left = format(x, "<10.1f")
        self.assertEqual(result_left, "1234.6    ")

    def test_format_thousands_separator(self):
        """
        【測試12】千分位分隔符號

        使用 "," 在數字中插入千分位逗號

        範例：
        - format(1234.56789, ",") → '1,234.56789'
        """
        x = 1234.56789
        result = format(x, ",")
        self.assertEqual(result, "1,234.56789")

    def test_format_with_decimal_and_thousands(self):
        """
        【測試13】同時設定千分位和小數位

        語法：format(數字, "0,小數位數f")

        範例：
        - format(1234.56789, "0,.2f") → '1,234.57'
        """
        x = 1234.56789
        result = format(x, "0,.2f")
        self.assertEqual(result, "1,234.57")

    def test_format_scientific_notation(self):
        """
        【測試14】科學記號表示法

        使用 "e" 或 "E" 轉換為科學記號

        範例：
        - format(1234.56789, "e") → '1.234568e+03'
        - format(1234.56789, "E") → '1.234568E+03'
        """
        x = 1234.56789
        result = format(x, "e")
        self.assertTrue(result.startswith("1.234568e+03"))

        result_upper = format(x, "E")
        self.assertTrue(result_upper.startswith("1.234568E+03"))


class TestBaseConversion(unittest.TestCase):
    """測試進制轉換"""

    def test_bin_oct_hex(self):
        """
        【測試15】轉換為二進制、八進制、十六進制

        函數：
        - bin(數字) → '0b...'（二進制，前綴 0b）
        - oct(數字) → '0o...'（八進制，前綴 0o）
        - hex(數字) → '0x...'（十六進制，前綴 0x）

        範例：1234
        - bin(1234) → '0b10011010010'
        - oct(1234) → '0o2322'
        - hex(1234) → '0x4d2'
        """
        n = 1234
        self.assertEqual(bin(n), "0b10011010010")
        self.assertEqual(oct(n), "0o2322")
        self.assertEqual(hex(n), "0x4d2")

    def test_format_base(self):
        """
        【測試16】format 函數控制進制（不含前綴）

        語法：format(數字, "進制符號")
        - "b" → 二進制（不含 0b）
        - "o" → 八進制（不含 0o）
        - "x" → 十六進制（不含 0x）

        範例：
        - format(1234, "b") → '10011010010'
        - format(1234, "x") → '4d2'
        """
        n = 1234
        self.assertEqual(format(n, "b"), "10011010010")
        self.assertEqual(format(n, "o"), "2322")
        self.assertEqual(format(n, "x"), "4d2")

    def test_int_from_string(self):
        """
        【測試17】將字串轉換為整數（指定進制）

        語法：int("數字字串", base=進制)

        重要：第二個參數是原始進制！
        - int("10011010010", 2) → 1234（二進制轉十進制）
        - int("2322", 8) → 1234（八進制轉十進制）
        - int("4d2", 16) → 1234（十六進制轉十進制）
        """
        n = 1234
        # 二進制字串轉十進制
        self.assertEqual(int("10011010010", 2), 1234)
        # 八進制字串轉十進制
        self.assertEqual(int("2322", 8), 1234)
        # 十六進制字串轉十進制（可大小寫混合）
        self.assertEqual(int("4d2", 16), 1234)
        self.assertEqual(int("4D2", 16), 1234)
        self.assertEqual(int("4D2", 16), 0x4D2)

    def test_int_from_hex_string(self):
        """
        【測試18】十六進制字串解析

        十六進制使用 0-9 和 a-f（或 A-F）
        - 0-9: 數字 0-9
        - a-f: 數字 10-15
        """
        # 十六進制 a = 10
        self.assertEqual(int("a", 16), 10)
        # 十六進制 f = 15
        self.assertEqual(int("f", 16), 15)
        # 十六進制 ff = 255
        self.assertEqual(int("ff", 16), 255)
        # 顏色值範例：#FF0000 = 紅色
        self.assertEqual(int("ff0000", 16), 16711680)


if __name__ == "__main__":
    # 執行所有測試
    unittest.main(verbosity=2)
