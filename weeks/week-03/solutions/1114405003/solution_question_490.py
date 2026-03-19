"""
題目 490 - 矩陣順時針旋轉 (Rotating Sentence)

這題要求將輸入的文本矩陣順時針旋轉 90 度。
輸入是多行文本（每行長度可能不同），輸出是旋轉後的矩陣。

核心算法：
1. 讀取所有輸入行直到 EOF
2. 找出最長行的長度（用空白補充較短行）
3. 將矩陣按照規則旋轉：最後一行變成最左列（由下到上），第一行變成最右列（由上到下）
4. 保持輸出矩形的完整性（右邊界用空白填充）

應用場景：矩陣變換、文本旋轉、圖像處理基礎
"""


class SentenceRotator:
    """
    文本矩陣旋轉類。
    
    特點：
    - 支援不等長輸入行
    - 自動補充空白使成為矩形
    - 支援順時針 90 度旋轉
    - 保持輸出矩形的完整性
    """
    
    def __init__(self):
        """初始化 SentenceRotator 實例。"""
        pass
    
    def rotate_text(self, lines):
        """
        將輸入文本順時針旋轉 90 度。
        
        參數：
            lines (list): 輸入行的列表，每個元素是一個字符串
        
        返回：
            list: 旋轉後的行列表
        
        算法說明：
        原始矩陣：
            row 0: A B C
            row 1: D E F
            row 2: G H I
        
        順時針旋轉 90 度後：
            row 0: G D A  (原第 0 列，從下到上)
            row 1: H E B  (原第 1 列，從下到上)
            row 2: I F C  (原第 2 列，從下到上)
        
        時間複雜度：O(rows * max_cols)
        空間複雜度：O(rows * max_cols)
        """
        if not lines:
            return []
        
        # 處理空輸入
        if all(not line for line in lines):
            return []
        
        # 找最長行長度
        max_length = max(len(line) for line in lines) if lines else 0
        
        if max_length == 0:
            return []
        
        # 補充空白使所有行等長（變成矩形）
        matrix = []
        for line in lines:
            padded_line = line.ljust(max_length)
            matrix.append(padded_line)
        
        rows = len(matrix)
        cols = max_length
        
        # 旋轉矩陣
        result = []
        
        # 新矩陣的列數 = 原矩陣的行數
        for col in range(cols):
            # 從下到上讀取原矩陣的第 col 列
            new_row = []
            for row in range(rows - 1, -1, -1):
                new_row.append(matrix[row][col])
            result.append(''.join(new_row))
        
        # 移除末尾的空白行（但保留中間的空白以保持矩形）
        # 不移除：題目要求輸出應使用與輸入中最寬的行等長的空格填充
        
        return result
    
    def process_input(self, input_text):
        """
        處理輸入文本並進行旋轉。
        
        參數：
            input_text (str): 完整的輸入文本
        
        返回：
            str: 旋轉後的文本
        """
        # 按行分割輸入
        lines = input_text.rstrip('\n').split('\n')
        
        # 執行旋轉
        rotated = self.rotate_text(lines)
        
        return '\n'.join(rotated)


def solve_rotating_sentence(input_text):
    """
    求解矩陣旋轉問題的主函式。
    
    參數：
        input_text (str): 完整的輸入文本
    
    返回：
        str: 旋轉後的文本
    """
    rotator = SentenceRotator()
    return rotator.process_input(input_text)


if __name__ == "__main__":
    # 測試範例 1
    test_input_1 = """HELLO
WORLD"""
    
    print("測試範例 1:\n輸入:")
    print(test_input_1)
    print("\n輸出:")
    output_1 = solve_rotating_sentence(test_input_1)
    print(output_1)
    
    # 測試範例 2
    test_input_2 = """ABC
DE"""
    
    print("\n\n測試範例 2:\n輸入:")
    print(test_input_2)
    print("\n輸出:")
    output_2 = solve_rotating_sentence(test_input_2)
    print(output_2)
