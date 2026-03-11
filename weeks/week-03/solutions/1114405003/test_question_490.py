"""
題目 490：矩陣順時針旋轉 90 度的單元測試程式

問題描述：
  將輸入的文字矩陣順時針旋轉 90 度
  - 原本由左到右、由上到下的輸入
  - 變成由上到下、由右到左的輸出
  - 最後一行變成最左列
  - 第一行變成最右列

旋轉原理：
  1. 讀取所有行
  2. 找到最長行的長度
  3. 用空白填充所有行到相同長度
  4. 順時針旋轉（轉置 + 反向行順序）
"""

import unittest
from typing import List


# ============================================================================
# 矩陣旋轉類別
# ============================================================================

class MatrixRotator:
    """
    用於旋轉矩陣的類別
    
    實現順時針 90 度旋轉
    """
    
    def rotate_clockwise_90(self, lines: List[str]) -> List[str]:
        """
        將輸入的文字矩陣順時針旋轉 90 度
        
        演算法流程：
        1. 如果輸入為空或只有一行，特殊處理
        2. 找到最長行的長度
        3. 用空白填充所有行到同一長度
        4. 進行順時針旋轉：
           - 對於每一列（從右往左）
           - 輸出該列的所有字符（從上到下）
        
        Args:
            lines: 輸入的文字行列表
            
        Returns:
            旋轉後的文字行列表
        """
        # 邊界條件處理
        if not lines:
            return []
        
        if len(lines) == 1:
            # 單行輸入：每個字符變成一行
            return list(lines[0])
        
        # 找到最長行的長度
        max_length = max(len(line) for line in lines)
        
        # 將所有行補充至相同長度（用空白填充）
        padded_lines = []
        for line in lines:
            padded_lines.append(line.ljust(max_length))
        
        # 進行順時針旋轉
        # 原理：最後一列變成第一行，第一列變成最後一行
        # 通過反向迭代列索引，然後逐行讀取
        result = []
        
        # 從右往左遍歷列
        for col_idx in range(max_length - 1, -1, -1):
            # 構建該列的所有字符（從上到下）
            new_line = ''.join(padded_lines[row_idx][col_idx] for row_idx in range(len(padded_lines)))
            result.append(new_line)
        
        return result
    
    def solve(self, text: str) -> str:
        """
        求解矩陣旋轉問題
        
        Args:
            text: 輸入的文字（多行，以換行符分隔）
            
        Returns:
            旋轉後的文字
        """
        # 分割輸入為多行
        lines = text.split('\n')
        
        # 移除最後的空行（如果存在）
        if lines and lines[-1] == '':
            lines = lines[:-1]
        
        # 進行旋轉
        result_lines = self.rotate_clockwise_90(lines)
        
        # 合併結果
        return '\n'.join(result_lines)


# ============================================================================
# 單元測試類別
# ============================================================================

class TestBasicRotation(unittest.TestCase):
    """測試基本的旋轉功能"""
    
    def setUp(self):
        """每個測試前的準備工作"""
        self.rotator = MatrixRotator()
    
    def test_single_character(self):
        """測試單一字符"""
        input_lines = ['A']
        result = self.rotator.rotate_clockwise_90(input_lines)
        self.assertEqual(result, ['A'])
    
    def test_single_line(self):
        """測試單一行輸入"""
        input_lines = ['ABC']
        expected = ['C', 'B', 'A']
        result = self.rotator.rotate_clockwise_90(input_lines)
        self.assertEqual(result, expected)
    
    def test_single_column(self):
        """測試單一列輸入"""
        input_lines = ['A', 'B', 'C']
        expected = ['CBA']
        result = self.rotator.rotate_clockwise_90(input_lines)
        self.assertEqual(result, expected)
    
    def test_two_by_two_square(self):
        """測試 2x2 正方形矩陣"""
        input_lines = ['AB', 'CD']
        expected = ['CA', 'DB']
        result = self.rotator.rotate_clockwise_90(input_lines)
        self.assertEqual(result, expected)
    
    def test_three_by_three_square(self):
        """測試 3x3 正方形矩陣"""
        input_lines = ['ABC', 'DEF', 'GHI']
        expected = ['GDA', 'HEB', 'IFC']
        result = self.rotator.rotate_clockwise_90(input_lines)
        self.assertEqual(result, expected)


class TestPadding(unittest.TestCase):
    """測試行補充功能"""
    
    def setUp(self):
        self.rotator = MatrixRotator()
    
    def test_unequal_length_lines(self):
        """測試長度不等的行"""
        input_lines = ['A', 'BB', 'CCC']
        # 補充後：['A  ', 'BB ', 'CCC']
        # 旋轉後應該按最長列處理
        result = self.rotator.rotate_clockwise_90(input_lines)
        # 應該產生 3 行輸出
        self.assertEqual(len(result), 3)
    
    def test_with_spaces(self):
        """測試包含空白的行"""
        input_lines = ['A B', 'CD']
        # 補充後：['A B', 'CD ']
        result = self.rotator.rotate_clockwise_90(input_lines)
        self.assertEqual(len(result), 3)
    
    def test_rectangular_matrix(self):
        """測試矩形（非正方形）矩陣"""
        input_lines = ['HELLO', 'WORLD']
        # 補充後都是 5 個字符
        result = self.rotator.rotate_clockwise_90(input_lines)
        # 應該產生 5 行輸出
        self.assertEqual(len(result), 5)
        # 第一行應該是「WH」（最後一列，從上到下）
        self.assertEqual(result[0], 'WH')


class TestOfficialExamples(unittest.TestCase):
    """測試官方範例"""
    
    def setUp(self):
        self.rotator = MatrixRotator()
    
    def test_hello_world(self):
        """測試 HELLO 和 WORLD 範例"""
        input_lines = ['HELLO', 'WORLD']
        result = self.rotator.rotate_clockwise_90(input_lines)
        
        # 預期輸出（顺時針旋轉後）
        expected = ['WH', 'OE', 'RL', 'LL', 'DO']
        self.assertEqual(result, expected)
    
    def test_simple_example(self):
        """測試簡單範例"""
        input_lines = ['AB', 'CD', 'EF']
        result = self.rotator.rotate_clockwise_90(input_lines)
        
        # 補充後：['AB', 'CD', 'EF']（已是相同長度）
        # 旋轉後：
        # 最後列（右列）→ 第一行：ECA
        # 第一列（左列）→ 最後行：FDB
        expected = ['ECA', 'FDB']
        self.assertEqual(result, expected)


class TestEdgeCases(unittest.TestCase):
    """測試邊界情況"""
    
    def setUp(self):
        self.rotator = MatrixRotator()
    
    def test_empty_input(self):
        """測試空輸入"""
        input_lines = []
        result = self.rotator.rotate_clockwise_90(input_lines)
        self.assertEqual(result, [])
    
    def test_empty_line(self):
        """測試包含空行"""
        input_lines = ['', 'A']
        result = self.rotator.rotate_clockwise_90(input_lines)
        # 應該補充空格
        self.assertEqual(len(result), 1)
    
    def test_all_spaces(self):
        """測試全空白行"""
        input_lines = ['   ', '   ']
        result = self.rotator.rotate_clockwise_90(input_lines)
        self.assertEqual(len(result), 3)
    
    def test_special_characters(self):
        """測試特殊字符"""
        input_lines = ['!@#', '$%^']
        result = self.rotator.rotate_clockwise_90(input_lines)
        expected = ['$!', '%@', '^#']
        self.assertEqual(result, expected)
    
    def test_numbers_and_mixed(self):
        """測試數字和混合內容"""
        input_lines = ['12', '34']
        result = self.rotator.rotate_clockwise_90(input_lines)
        expected = ['31', '42']
        self.assertEqual(result, expected)


class TestRotationProperties(unittest.TestCase):
    """測試旋轉的數學性質"""
    
    def setUp(self):
        self.rotator = MatrixRotator()
    
    def test_rotation_four_times_returns_original(self):
        """測試旋轉 4 次應回到原始狀態（對正方形）"""
        input_lines = ['ABC', 'DEF', 'GHI']
        
        # 第 1 次旋轉
        result1 = self.rotator.rotate_clockwise_90(input_lines)
        
        # 第 2 次旋轉
        result2 = self.rotator.rotate_clockwise_90(result1)
        
        # 第 3 次旋轉
        result3 = self.rotator.rotate_clockwise_90(result2)
        
        # 第 4 次旋轉
        result4 = self.rotator.rotate_clockwise_90(result3)
        
        # 應該回到原始狀態
        self.assertEqual(result4, input_lines)
    
    def test_rotation_dimensions_swap(self):
        """測試旋轉後行列互換"""
        input_lines = ['ABC', 'DEF']  # 2x3 矩陣
        result = self.rotator.rotate_clockwise_90(input_lines)
        
        # 旋轉後應該變成 3x2 矩陣
        self.assertEqual(len(result), 3)  # 3 行
        self.assertEqual(len(result[0]), 2)  # 每行 2 列


class TestTextInput(unittest.TestCase):
    """測試文字輸入處理"""
    
    def setUp(self):
        self.rotator = MatrixRotator()
    
    def test_text_with_newlines(self):
        """測試帶換行符的文字"""
        text = "HELLO\nWORLD"
        result_text = self.rotator.solve(text)
        
        expected_lines = ['WH', 'OE', 'RL', 'LL', 'DO']
        expected_text = '\n'.join(expected_lines)
        
        self.assertEqual(result_text, expected_text)
    
    def test_text_with_trailing_newline(self):
        """測試帶尾部換行符的文字"""
        text = "AB\nCD\n"
        result_text = self.rotator.solve(text)
        
        expected_lines = ['CA', 'DB']
        expected_text = '\n'.join(expected_lines)
        
        self.assertEqual(result_text, expected_text)


class TestLongerMatrices(unittest.TestCase):
    """測試較大的矩陣"""
    
    def setUp(self):
        self.rotator = MatrixRotator()
    
    def test_five_by_five(self):
        """測試 5x5 矩陣旋轉"""
        input_lines = [
            'ABCDE',
            'FGHIJ',
            'KLMNO',
            'PQRST',
            'UVWXY'
        ]
        result = self.rotator.rotate_clockwise_90(input_lines)
        
        # 驗證輸出的行數和列數
        self.assertEqual(len(result), 5)
        self.assertEqual(len(result[0]), 5)
        
        # 驗證第一行（最後一列，從上到下）
        self.assertEqual(result[0], 'UFPKA')
        
        # 驗證最後一行（第一列，從上到下）
        self.assertEqual(result[4], 'YOJEF')
    
    def test_wide_rectangle(self):
        """測試寬矩形 2x6"""
        input_lines = ['ABCDEF', 'GHIJKL']
        result = self.rotator.rotate_clockwise_90(input_lines)
        
        self.assertEqual(len(result), 6)  # 6 行輸出
        self.assertEqual(result[0], 'GA')  # 最後一列


# ============================================================================
# 主程式入口
# ============================================================================

if __name__ == '__main__':
    # 執行所有單元測試
    unittest.main(verbosity=2)
