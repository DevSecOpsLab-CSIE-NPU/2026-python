"""
UVA 10812 — Beat the Spread! 簡單版本
更簡單易記的寫法

核心思想：
- 較大分數 = (和 + 差) / 2
- 較小分數 = (和 - 差) / 2
- 檢查是否為整數且非負
"""


def solve_simple(s, d):
    """
    最簡單的解法
    
    只需要記住三個檢查條件：
    1. (S + D) 能被 2 整除嗎？ → (s + d) % 2 == 0
    2. 較小分數是否為負數？ → (s - d) // 2 < 0
    3. 否則輸出兩個分數
    """
    # 檢查 (S + D) 是否為偶數
    if (s + d) % 2 != 0:
        return "impossible"
    
    # 計算分數
    big = (s + d) // 2
    small = (s - d) // 2
    
    # 檢查是否有負數
    if small < 0:
        return "impossible"
    
    return f"{big} {small}"


# 測試
if __name__ == "__main__":
    print(solve_simple(40, 20))  # 30 10
    print(solve_simple(20, 40))  # impossible
    print(solve_simple(10, 2))   # 6 4
