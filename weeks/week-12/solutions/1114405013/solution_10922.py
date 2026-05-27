'''
UVA 10922 — 2 the 9s
判斷超大整數是否為 9 的倍數，若是則計算其 9-degree。
9-degree = 需要做幾次「把各位數字加總」才能得到 9。
完整繁體中文註解，適合學習與單元測試。
'''

def solve(in_stream, out_stream):
    """
    參數：
      in_stream  — 輸入串流，每行一個正整數，0 結束
      out_stream — 輸出串流，輸出判斷結果與 degree
    """
    while True:
        # 讀取一整行並去除前後空白
        numstr = in_stream.readline().strip()
        if numstr == '0':          # 遇到 0 結束輸入
            break

        ori = numstr               # 保留原始字串以供輸出

        degree = 0                 # degree 初始設為 0
        while len(numstr) > 1:     # 當數字超過一位就繼續加總
            # 把每一位字元轉成整數後加總，再轉回字串
            numstr = str(sum(int(c) for c in numstr))
            degree += 1            # 每做一次加總，degree 就 +1

        # 如果原數本身就是 '9'（沒進過 while），degree 要從 0 修正為 1
        if numstr == '9':
            deg = degree if degree > 0 else 1
            out_stream.write(f"9-degree of {ori} is {deg}.\n")
        else:
            out_stream.write(f"{ori} is not a multiple of 9.\n")


if __name__ == '__main__':
    import sys
    solve(sys.stdin, sys.stdout)
