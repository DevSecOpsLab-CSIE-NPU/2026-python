"""
題目 490：矩陣順時針旋轉 Easy 版本
檔名：question_490_easy.py

最簡單、最容易記憶的解法
適合臨場編寫

核心思想：
1. 讀取所有行
2. 找最長的行並用空白填充其他行
3. 順時針旋轉 = 從右往左遍歷列，每列從上到下輸出
"""


def rotate_text(lines):
    """
    將文字矩陣順時針旋轉 90 度
    
    Args:
        lines: 文字行的列表
        
    Returns:
        旋轉後的文字行列表
    """
    # 邊界條件處理
    if not lines:
        return []
    
    if len(lines) == 1:
        return list(lines[0])
    
    # 找最長行的長度
    max_len = max(len(line) for line in lines)
    
    # 用空白補充所有行到相同長度
    padded = [line.ljust(max_len) for line in lines]
    
    # 旋轉：從右往左遍歷列
    # 每列的所有字符形成一行輸出
    result = []
    for col in range(max_len - 1, -1, -1):
        new_line = ''.join(padded[row][col] for row in range(len(padded)))
        result.append(new_line)
    
    return result


def solve(text):
    """
    求解旋轉問題
    
    Args:
        text: 輸入的文字（多行，以換行符分隔）
        
    Returns:
        旋轉後的文字
    """
    # 分割成多行
    lines = text.strip().split('\n')
    
    # 進行旋轉
    result_lines = rotate_text(lines)
    
    # 合併並返回
    return '\n'.join(result_lines)


# 主程式
if __name__ == '__main__':
    import sys
    
    # 讀取所有輸入
    text = sys.stdin.read()
    
    # 解答
    output = solve(text)
    
    # 輸出結果
    print(output)
