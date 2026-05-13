"""
================================================================================
UVA 10922 - 2 the 9s (簡化版)

題目核心：
  - 判斷一個數是否為 9 的倍數
  - 若是，計算「9 的深度」= 需要多少次數字相加才能得到 9
  
  例如：99 → 9+9=18 → 1+8=9（深度=2）
  
輸入：正整數，以 0 結束
輸出：
  - 是 9 的倍數：「9-degree of X is Y.」
  - 否則：「X is not a multiple of 9.」
================================================================================
"""


def digit_sum(n):
    """
    計算數字各位相加的和。
    例：digit_sum(123) = 1+2+3 = 6
    """
    total = 0
    # 逐位將每個數字加起來
    for ch in str(n):
        total += int(ch)
    return total


def nine_degree(n):
    """
    計算「9 的深度」。
    
    步驟：
    1. 重複計算各位數字之和
    2. 計數每一次的加總
    3. 當結果為個位數時停止
    4. 若最終為 9，則返回深度；否則返回 None
    """
    degree = 0
    
    # 重複相加各位數字，直到得到個位數
    while True:
        n = digit_sum(n)           # 計算各位數字和
        degree += 1                 # 深度 +1
        
        if n == 9:                  # 得到 9，說明是 9 的倍數
            return degree
        elif n < 10:                # 得到其他個位數，不是 9 的倍數
            return None


def main():
    """
    主程式：不斷讀取輸入直到遇到 0
    """
    while True:
        line = input().strip()
        
        # 遇到 0 停止程式
        if line == "0":
            break
        
        # 計算 9 的深度
        degree = nine_degree(int(line))
        
        # 輸出結果
        if degree is None:
            print(f"{line} is not a multiple of 9.")
        else:
            print(f"9-degree of {line} is {degree}.")


if __name__ == "__main__":
    main()
