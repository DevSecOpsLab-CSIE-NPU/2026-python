"""
================================================================================
UVA 10929 - 判斷 11 的倍數（簡化版）

題目核心：
  判斷一個數（最多 1000 位）是否為 11 的倍數
  
判斷技巧：
  從右往左計算：奇數位數字和 - 偶數位數字和 = 11 的倍數？
  
  例：121 → 1 (奇) + 1 (奇) = 2，2 (偶) = 2，差 = 0 ✓
  例：123 → 3 (奇) + 1 (奇) = 4，2 (偶) = 2，差 = 2 ✗

輸入：逐行輸入正整數，以 0 結束
輸出：是/否為 11 的倍數
================================================================================
"""


def is_multiple_of_11(n_str):
    """
    判斷數字是否為 11 的倍數。
    
    方法：
      - 從右往左遍歷每一位
      - 奇數位（第 1, 3, 5, ...）的數字相加
      - 偶數位（第 2, 4, 6, ...）的數字相加
      - 兩者的差 % 11 == 0 則是 11 的倍數
    """
    odd_sum = 0   # 奇數位和
    even_sum = 0  # 偶數位和
    
    # 從右往左遍歷數字（位數從 1 開始）
    for idx, digit_char in enumerate(reversed(n_str)):
        digit = int(digit_char)
        
        # 判斷是奇數位還是偶數位
        if (idx + 1) % 2 == 1:
            odd_sum += digit
        else:
            even_sum += digit
    
    # 檢查差是否為 11 的倍數
    diff = odd_sum - even_sum
    return diff % 11 == 0


def main():
    """
    主程式：讀取輸入直到 0
    """
    while True:
        line = input().strip()
        
        # 遇到 0 停止
        if line == "0":
            break
        
        # 判斷並輸出
        if is_multiple_of_11(line):
            print(f"{line} is a multiple of 11.")
        else:
            print(f"{line} is not a multiple of 11.")


if __name__ == "__main__":
    main()
