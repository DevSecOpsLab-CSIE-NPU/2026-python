"""
UVA 10929 — You can say 11
======================================
判斷一個超大正整數（最多 1000 位）是否為 11 的倍數。

判斷規則（11 的倍數特徵）：
  將數字從左到右，奇數位（第 1, 3, 5, … 位）總和 減去
  偶數位（第 2, 4, 6, … 位）總和，
  若差值能被 11 整除，則原數為 11 的倍數。
"""

def solve(in_stream, out_stream):
    """
    參數：
      in_stream  — 輸入串流，每行一個正整數，0 結束
      out_stream — 輸出串流，輸出判斷結果
    """
    while True:
        line = in_stream.readline()
        if not line:               # EOF 保護
            break
        s = line.strip()
        if s == '0':               # 結束條件
            break

        # 奇數位總和（odd_sum）與偶數位總和（even_sum）
        odd_sum = 0
        even_sum = 0

        # 逐一取出每個字元，i 從 0 開始
        # i = 0 → 第 1 位（奇數位）
        # i = 1 → 第 2 位（偶數位）
        for i, ch in enumerate(s):
            digit = ord(ch) - ord('0')   # 字元轉整數
            if i % 2 == 0:
                odd_sum += digit
            else:
                even_sum += digit

        # 計算差值，取絕對值判斷是否為 11 的倍數
        diff = odd_sum - even_sum
        if diff % 11 == 0:
            out_stream.write(f"{s} is a multiple of 11.\n")
        else:
            out_stream.write(f"{s} is not a multiple of 11.\n")


if __name__ == '__main__':
    import sys
    solve(sys.stdin, sys.stdout)
