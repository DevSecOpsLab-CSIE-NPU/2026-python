"""
================================================================================
UVA 10931 - Parity（奇偶性） - 簡化版

題目核心：
  計算一個整數的二進位表示中 1 的個數
  
方法：
  1. 使用 bin() 轉換為二進位字串（去掉 "0b" 前綴）
  2. 計算字串中 '1' 的個數
  3. 按格式輸出：「The parity of B is P (mod 2).」

例：1 → "1" → 1 個 1 → 輸出「The parity of 1 is 1 (mod 2).」
例：10 → "1010" → 2 個 1 → 輸出「The parity of 1010 is 2 (mod 2).」
================================================================================
"""


def count_ones_in_binary(n):
    """
    計算二進位中 1 的個數。
    
    參數：n (int) - 正整數
    返回：(二進位字串, 1 的個數)
    """
    binary = bin(n)[2:]           # 轉換為二進位，去掉 "0b" 前綴
    ones = binary.count('1')      # 計算 '1' 的個數
    return binary, ones


def main():
    """
    主程式：讀取輸入、計算、輸出
    """
    while True:
        n = int(input().strip())
        
        # 遇到 0 停止
        if n == 0:
            break
        
        # 計算並輸出
        binary, ones = count_ones_in_binary(n)
        print(f"The parity of {binary} is {ones} (mod 2).")


if __name__ == "__main__":
    main()
