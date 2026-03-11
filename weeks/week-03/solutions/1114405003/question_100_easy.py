"""
題目 100：Collatz序列 簡單版本（AI教學版）
檔名：question_100_easy.py

這是最簡單、最容易記憶的Collatz序列解法
適合在CPE考試當場臨時寫出來

特點：
- 程式邏輯簡單明瞭，容易理解
- 注重代碼簡潔性，不過度優化
- 使用全域記憶化字典加速計算
- 容易在考試時手打
"""

# 全域記憶化字典，避免重複計算
memo = {1: 1}


def cycle_length(n):
    """
    計算n的cycle-length（序列長度）
    
    關鍵邏輯：
    - 如果是1，長度為1
    - 如果是偶數，除以2，長度加1
    - 如果是奇數，乘以3加1，長度加1
    
    Args:
        n: 輸入正整數
        
    Returns:
        該數字的cycle-length
    """
    if n in memo:
        return memo[n]
    
    # 根據奇偶性計算下一個數字
    if n % 2 == 0:
        next_n = n // 2
    else:
        next_n = 3 * n + 1
    
    # 遞迴計算，並記錄結果
    result = cycle_length(next_n) + 1
    memo[n] = result
    return result


def solve(i, j):
    """
    找出[i,j]區間內的最大cycle-length
    
    Args:
        i, j: 區間的兩端點
        
    Returns:
        該區間內所有數字的最大cycle-length
    """
    # 確保i <= j
    start = min(i, j)
    end = max(i, j)
    
    # 找出區間內的最大值
    max_len = 0
    for num in range(start, end + 1):
        max_len = max(max_len, cycle_length(num))
    
    return max_len


# 主程式：讀取輸入並輸出結果
if __name__ == '__main__':
    try:
        while True:
            line = input()
            i, j = map(int, line.split())
            result = solve(i, j)
            print(f"{i} {j} {result}")
    except EOFError:
        # 讀到檔案末尾時結束
        pass
