import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_490.py 中
# 並且您的解答會提供一個 rotate_sentences(lines) 函式：
# 接收一個包含多行字串的 list，並回傳旋轉 90 度後的字串 list。
from solution_490 import rotate_sentences

class TestUVA490(unittest.TestCase):
    
    def test_sample_case(self):
        """
        測試題目基礎範例。
        長度相同的兩行字串旋轉：
        HELLO
        WORLD
        旋轉後，最後輸入的 WORLD 會在最左邊，最先輸入的 HELLO 會在最右邊。
        """
        input_lines = [
            "HELLO",
            "WORLD"
        ]
        expected = [
            "WH",
            "OE",
            "RL",
            "LL",
            "DO"
        ]
        self.assertEqual(rotate_sentences(input_lines), expected)

    def test_different_lengths(self):
        """
        測試長度不一的字串 (UVA 490 核心陷阱)。
        當上方字串較長、下方字串較短時，下方字串對應的空缺必須填補「空白 (Space)」。
        """
        input_lines = [
            "12345",
            "AB",
            "XYZ"
        ]
        # 最長為 5，有 3 行字串，輸出應該要是 5 行、每行 3 個字元。
        expected = [
            "XA1",
            "YB2",
            "Z 3", # 注意這裡：第二行的 "AB" 只有兩個字元，所以對應的位置要補上空白
            "  4", # 第三行、第二行都沒有第 4 個字元，都要補空白
            "  5"
        ]
        self.assertEqual(rotate_sentences(input_lines), expected)
        
    def test_single_line(self):
        """
        邊界測試：只有單行字串的旋轉。
        """
        self.assertEqual(rotate_sentences(["ABC"]), ["A", "B", "C"])

if __name__ == '__main__':
    unittest.main()