"""
題目 10929 - Divisibility by 11

問題：判斷超大數字（最多 1000 位）是否為 11 的倍數

解法：
- 使用「奇偶位檢驗法」
- 奇數位數字之和 - 偶數位數字之和 ≡ 0 (mod 11) 
- 則該數是 11 的倍數
"""


def is_multiple_of_11(num_str):
    """
    判斷一個數字字符串是否為 11 的倍數。
    
    使用奇偶位檢驗法：
    - 奇數位：第 1, 3, 5, ... 位（從右往左數）
    - 偶數位：第 2, 4, 6, ... 位（從右往左數）
    - 若 (奇數位和 - 偶數位和) % 11 == 0，則是 11 的倍數
    
    參數：
        num_str (str): 數字的字符串表示
    
    返回：
        bool: 是否為 11 的倍數
    """
    # 計算奇偶位數字和
    odd_sum = 0   # 奇數位的和
    even_sum = 0  # 偶數位的和
    
    # 從右往左遍歷數字
    for idx, digit in enumerate(reversed(num_str)):
        # idx 是從 0 開始的索引
        # 實際位置（從右往左）是 idx + 1
        # 位置為 1, 3, 5... 的是奇數位
        # 位置為 2, 4, 6... 的是偶數位
        
        if (idx + 1) % 2 == 1:  # 奇數位
            odd_sum += int(digit)
        else:  # 偶數位
            even_sum += int(digit)
    
    # 計算差值
    diff = odd_sum - even_sum
    
    # 判斷是否為 11 的倍數
    return diff % 11 == 0


def main():
    """
    主程式：讀取輸入，判斷是否為 11 的倍數。
    """
    # 讀取輸入，直到遇到 0
    while True:
        # 讀取一個數字（可能很長）
        num_str = input().strip()
        
        # 當輸入為 '0' 時停止
        if num_str == '0':
            break
        
        # 判斷是否為 11 的倍數
        if is_multiple_of_11(num_str):
            print(f"{num_str} is a multiple of 11.")
        else:
            print(f"{num_str} is not a multiple of 11.")


if __name__ == "__main__":
    main()
