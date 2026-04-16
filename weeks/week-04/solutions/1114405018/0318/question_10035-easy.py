"""UVA 10035 - easy 版本

題目重點：
1. 每行輸入兩個整數。
2. 計算這兩個數做直式加法時，總共發生幾次進位（carry）。
3. 遇到輸入 0 0 時結束，不再輸出結果。

輸出規則：
- 0 次進位：No carry operation.
- 1 次進位：1 carry operation.
- 2 次以上：n carry operations.
"""

import sys

# 逐行讀取測資，直到 EOF
for line in sys.stdin:
    # 去除前後空白（包含換行）
    line = line.strip()

    # 若是空行就略過
    if not line:
        continue

    # 解析兩個整數
    a, b = map(int, line.split())

    # 題目規定：0 0 代表輸入結束
    if a == 0 and b == 0:
        break

    # carry: 目前這一位加總後，是否要進位到下一位（0 或 1）
    # count: 累積總進位次數
    carry = 0
    count = 0

    # 只要任一數字還有位數，就持續逐位計算
    while a > 0 or b > 0:
        # 取出個位數相加，再加上前一位帶來的進位
        s = (a % 10) + (b % 10) + carry

        # 若 >= 10，代表本位發生一次進位
        if s >= 10:
            count += 1
            carry = 1
        else:
            carry = 0

        # 去掉已處理的個位數，往下一位前進
        a //= 10
        b //= 10

    # 依進位次數輸出題目指定字串
    if count == 0:
        print("No carry operation.")
    elif count == 1:
        print("1 carry operation.")
    else:
        print(f"{count} carry operations.")
