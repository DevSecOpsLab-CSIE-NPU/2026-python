'''
UVA 10922 — 2 the 9s
======================================
最簡單易記寫法，附詳細繁體中文逐行說明。

核心規則（題目定義）：
  ① 一個整數若能被 9 整除，則稱「9 的倍數」。
  ② 判斷方式：重複將各位數字加總，直到只剩一位數。
  ③ 若最終那位數為 9，即為 9 的倍數。
  ④「9-degree」= 總共做了幾次「各位數加總」才得到 9。

計算 degree 的邏輯口訣：
  「每加總一次 degree 就加一；若本身已是 9，degree 就是一。」
'''

def solve(in_stream, out_stream):
    """
    參數說明：
      in_stream  — 輸入串流（類似 sys.stdin），
                   每行一個正整數，遇到 '0' 停止。
      out_stream — 輸出串流（類似 sys.stdout），
                   印出判斷結果與 9-degree。
    """

    # ===== 主迴圈：持續讀取直到遇到 '0' =====
    while True:
        # 讀取一行，去除換行與前後空白字元
        s = in_stream.readline().strip()

        # 題目規定：輸入為 "0" 時結束程式
        if s == '0':
            break

        # 保留原始的輸入字串，printf 時會需要用到
        orig = s

        # ===== 初始化 degree 計數器 =====
        # deg 用來記錄「總共執行了幾次各位數字加總」
        # 初始為 0，每做一次加總就 +1
        deg = 0

        # ===== 反覆進行「各位數字加總」直到剩一位數 =====
        # 條件：只要 s 的長度大於 1（即超過一位數）就要繼續加總
        while len(s) > 1:
            # 將字串 s 中的每個字元轉成整數後全部加起來
            # 再把結果轉回字串，以判斷是否仍為多位數
            s = str(sum(int(x) for x in s))

            # 完成一次「各位數加總」，deg 加一
            deg += 1

        # ===== 處理「本身就是 9」的特殊情況 =====
        # 如果輸入是 "9"：
        #   → 長度為 1，完全不會進入上面的 while 迴圈
        #   → deg 會維持 0
        #   → 但根據題意，本身的 degree 應為 1
        # 因此如果 deg 還是 0，就手動設成 1
        deg = deg if deg > 0 else 1

        # ===== 判斷是否為 9 的倍數並輸出結果 =====
        if s == '9':
            # 是 9 的倍數，輸出 degree
            out_stream.write(f"9-degree of {orig} is {deg}.\n")
        else:
            # 不是 9 的倍數
            out_stream.write(f"{orig} is not a multiple of 9.\n")


# ===== 程式進入點：直接用 sys.stdin / sys.stdout 執行 =====
if __name__ == '__main__':
    import sys
    solve(sys.stdin, sys.stdout)
