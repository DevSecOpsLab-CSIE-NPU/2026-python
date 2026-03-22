"""
UVA 10035: Primary Arithmetic
題目: 計算兩個整數相加時的進位次數。

輸入:
每一行包含兩個正整數（皆小於 10^9）。
輸入以 0 0 作為結束。

輸出:
No carry operation. (0 次)
1 carry operation. (1 次)
X carry operations. (X > 1 次)
"""

import sys

def solve():
    for line in sys.stdin:
        # 去除頭尾空白
        line = line.strip()
        if not line:
            continue
            
        parts = line.split()
        if len(parts) != 2:
            continue
            
        try:
            a = int(parts[0])
            b = int(parts[1])
        except ValueError:
            continue
            
        # 結束條件
        if a == 0 and b == 0:
            break
            
        carry = 0
        carry_count = 0
        
        # 當還有數字或進位未處理時繼續迴圈
        while a > 0 or b > 0:
            digit_a = a % 10
            digit_b = b % 10
            
            # 計算當前位數的和 + 前一位的進位
            current_sum = digit_a + digit_b + carry
            
            if current_sum >= 10:
                carry = 1
                carry_count += 1
            else:
                carry = 0
            
            # 移至下一位
            a //= 10
            b //= 10
            
        # 根據題目要求格式輸出
        if carry_count == 0:
            print("No carry operation.")
        elif carry_count == 1:
            print("1 carry operation.")
        else:
            print(f"{carry_count} carry operations.")

if __name__ == '__main__':
    solve()
