import math
import sys

def solve():
    # 使用 sys.stdin 讀取輸入，以應對可能的連續輸入或大檔案
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            a = int(line)
        except ValueError:
            continue

        # --- 數學推導簡述 ---
        # 根據公式推導可得：(b - a)(c - a) = a^2 + 1
        # 令 X = b - a, Y = c - a
        # 則 X * Y = a^2 + 1
        # 我們要求的 b + c = (X + a) + (Y + a) = X + Y + 2a
        # 
        # 為了讓 b + c 最小，且 2a 是固定值，我們必須讓 X + Y 最小。
        # 根據算術幾何平均不等式原理，當兩數乘積固定時，
        # 兩數越「接近」，其和就越小。
        
        target = a * a + 1
        
        # 從 sqrt(target) 開始向下尋找第一個能整除 target 的整數
        # 這樣找到的 X 會是最接近 sqrt(target) 的因數，
        # 從而保證 X 與 Y 的差距最小，進而使 X + Y 最小。
        
        # 使用整數開根號作為搜尋起點
        x = int(math.isqrt(target))
        
        # 遞減搜尋因數
        while x > 0:
            if target % x == 0:
                # 找到因數 X，則另一個因數 Y = target / X
                y = target // x
                
                # 計算最終結果 b + c = X + Y + 2a
                result = x + y + 2 * a
                print(result)
                break
            x -= 1

if __name__ == "__main__":
    solve()