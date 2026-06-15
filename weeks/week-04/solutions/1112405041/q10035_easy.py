# 10035-easy.py
# UVA 10035：Primary Arithmetic (簡單版)
# 核心邏輯：模擬國小加法進位，用 carry 變數紀錄是否進位

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    it = iter(input_data)
    while True:
        try:
            a_str = next(it)
            b_str = next(it)
        except StopIteration:
            break

        if a_str == "0" and b_str == "0":
            break

        # 為了方便從個位數開始加，我們把字串反轉
        a = list(map(int, reversed(a_str)))
        b = list(map(int, reversed(b_str)))

        carries = 0
        current_carry = 0
        # 跑比較長的那個數字的長度
        for i in range(max(len(a), len(b))):
            val_a = a[i] if i < len(a) else 0
            val_b = b[i] if i < len(b) else 0

            if val_a + val_b + current_carry >= 10:
                carries += 1
                current_carry = 1
            else:
                current_carry = 0

        # 格式化輸出
        if carries == 0:
            print("No carry operation.")
        elif carries == 1:
            print("1 carry operation.")
        else:
            print(f"{carries} carry operations.")

if __name__ == "__main__":
    solve()
