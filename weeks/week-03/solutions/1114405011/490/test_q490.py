"""
test_q490.py — UVA 490 Rotating Text 單元測試
==============================================
測試對象：q490.py 中的 rotate_cw() 與 solve()
執行方式：pytest test_q490.py -v
"""

import importlib.util
import pathlib
import unittest

# ── 動態載入 q490.py（路徑固定在同一目錄）──────────────────────────────────
_path = pathlib.Path(__file__).parent / "q490.py"
_spec = importlib.util.spec_from_file_location("q490", _path)
_mod  = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

rotate_cw = _mod.rotate_cw   # 取得旋轉函式
solve     = _mod.solve        # 取得主解題函式


# ══════════════════════════════════════════════════════════════════════════════
class TestRotateCw(unittest.TestCase):
    """測試 rotate_cw(lines) 的核心旋轉邏輯"""

    def test_basic_hello_world(self):
        """題目基本範例：HELLO / WORLD 旋轉後應得 WH OE RL LL DO"""
        result = rotate_cw(["HELLO", "WORLD"])
        self.assertEqual(result, ["WH", "OE", "RL", "LL", "DO"])

    def test_single_row(self):
        """單一行：旋轉後每個字元各自成一行，垂直排列"""
        result = rotate_cw(["ABC"])
        # A 在最右，C 在最左：結果由下到上 → [C, B, A]
        self.assertEqual(result, ["A", "B", "C"])

    def test_single_column(self):
        """單一欄（每行只有一字元）：旋轉後合成一行，由下往上讀"""
        result = rotate_cw(["A", "B", "C"])
        self.assertEqual(result, ["CBA"])

    def test_square_3x3(self):
        """3×3 正方形矩陣旋轉"""
        # 原矩陣:  ABC
        #           DEF
        #           GHI
        # col 0 由下到上: G D A → "GDA"
        # col 1 由下到上: H E B → "HEB"
        # col 2 由下到上: I F C → "IFC"
        result = rotate_cw(["ABC", "DEF", "GHI"])
        self.assertEqual(result, ["GDA", "HEB", "IFC"])

    def test_unequal_row_lengths_padding(self):
        """行長不一時，短行應補空格再旋轉"""
        # 'AB' 補成 'AB '，'CDE' 不變，'F' 補成 'F  '
        # reversed: F__, CDE, AB_
        # col0: F,C,A → "FCA"
        # col1: _,D,B → " DB"
        # col2: _,E,_ → " E "
        result = rotate_cw(["AB", "CDE", "F"])
        self.assertEqual(result, ["FCA", " DB", " E "])

    def test_with_spaces_in_content(self):
        """行內含空格，旋轉後空格應保留在正確位置"""
        # "A B" = A, space, B
        # "C D" = C, space, D
        # reversed: [C D, A B]
        # col0: C,A → "CA"
        # col1: ' ',' ' → "  "
        # col2: D,B → "DB"
        result = rotate_cw(["A B", "C D"])
        self.assertEqual(result, ["CA", "  ", "DB"])

    def test_single_character(self):
        """單一字元輸入，旋轉後仍是該字元"""
        result = rotate_cw(["X"])
        self.assertEqual(result, ["X"])

    def test_empty_list(self):
        """空列表輸入，應回傳空列表"""
        result = rotate_cw([])
        self.assertEqual(result, [])

    def test_two_rows_two_cols(self):
        """2×2 矩陣旋轉"""
        # AB  →  col0: C,A → CA
        # CD     col1: D,B → DB
        result = rotate_cw(["AB", "CD"])
        self.assertEqual(result, ["CA", "DB"])

    def test_numbers(self):
        """數字字元旋轉"""
        result = rotate_cw(["123", "456"])
        # col0: 4,1 → "41"
        # col1: 5,2 → "52"
        # col2: 6,3 → "63"
        self.assertEqual(result, ["41", "52", "63"])

    def test_output_row_count_equals_max_width(self):
        """輸出列數應等於輸入中最寬行的長度"""
        lines = ["HELLO", "HI", "PYTHON"]   # max_w = 6
        result = rotate_cw(lines)
        self.assertEqual(len(result), 6)

    def test_output_col_count_equals_row_count(self):
        """每列輸出的字元數應等於原始行數"""
        lines = ["HELLO", "WORLD", "AGAIN"]  # 3 行
        result = rotate_cw(lines)
        for row in result:
            self.assertEqual(len(row), 3)


# ══════════════════════════════════════════════════════════════════════════════
class TestSolve(unittest.TestCase):
    """測試 solve(input_text) 的完整輸入輸出流程"""

    def test_basic_hello_world(self):
        """題目基本範例：換行分隔輸入"""
        result = solve("HELLO\nWORLD")
        self.assertEqual(result, "WH\nOE\nRL\nLL\nDO")

    def test_single_row(self):
        """單行輸入：每個字元各自一行輸出"""
        result = solve("ABC")
        self.assertEqual(result, "A\nB\nC")

    def test_single_column(self):
        """單欄輸入（每行一字元）：合成一行輸出"""
        result = solve("A\nB\nC")
        self.assertEqual(result, "CBA")

    def test_empty_input(self):
        """完全空白輸入，應回傳空字串"""
        result = solve("")
        self.assertEqual(result, "")

    def test_single_char(self):
        """單一字元，旋轉後仍是該字元"""
        result = solve("Z")
        self.assertEqual(result, "Z")

    def test_with_trailing_newline(self):
        """尾端含換行符，結果應相同（splitlines 會自動處理）"""
        result = solve("HELLO\nWORLD\n")
        self.assertEqual(result, "WH\nOE\nRL\nLL\nDO")

    def test_unequal_rows(self):
        """行長不一，短行補空格後旋轉"""
        result = solve("AB\nCDE\nF")
        self.assertEqual(result, "FCA\n DB\n E ")

    def test_numbers_only(self):
        """純數字輸入旋轉"""
        result = solve("123\n456")
        self.assertEqual(result, "41\n52\n63")

    def test_punctuation(self):
        """包含標點符號的輸入"""
        result = solve("A!\nB.")
        # col0: B,A → "BA"
        # col1: .,! → ".!"
        self.assertEqual(result, "BA\n.!")

    def test_output_line_count(self):
        """輸出列數 = 輸入中最長行的字元數"""
        result = solve("HELLO\nWORLD\nPY")
        lines = result.splitlines()
        self.assertEqual(len(lines), 5)  # max_w = 5

    def test_spaces_preserved(self):
        """行內空格旋轉後應保留在正確位置"""
        result = solve("A B\nC D")
        self.assertEqual(result, "CA\n  \nDB")


if __name__ == "__main__":
    unittest.main()
