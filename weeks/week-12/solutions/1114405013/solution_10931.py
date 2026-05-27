"""
UVA 10931 — Parity
======================================
給一個整數 I，求出其二進位表示與其中 1 的個數 P，
並以指定格式輸出。

解題步驟：
  ① 用 bin(I) 取得二進位字串（格式 "0b..."）
  ② 去掉 "0b" 前綴
  ③ 用 count("1") 數有幾個 1
  ④ 按照題目格式輸出
"""

def solve(in_stream, out_stream):
    """
    參數：
      in_stream  — 輸入串流，每行一個整數 I，0 結束
      out_stream — 輸出串流
    """
    while True:
        line = in_stream.readline()
        if not line:
            break
        line = line.strip()
        if line == '0':
            break

        # 輸入為整數（在此範圍內 Python int 完全容納）
        n = int(line)

        # bin(n) 回傳 "0b1010" 格式，去掉前兩個字元
        binary = bin(n)[2:]

        # 計算 1 的個數
        p = binary.count('1')

        # 按照題目格式輸出
        out_stream.write(f"The parity of {binary} is {p} (mod 2).\n")


if __name__ == '__main__':
    import sys
    solve(sys.stdin, sys.stdout)
