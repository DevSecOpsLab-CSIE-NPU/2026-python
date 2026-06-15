import sys

# 手打版本：組合數累加判斷法處理 64-bit 樓層丟水球問題
def solve():
    raw = sys.stdin.read().split()
    if not raw: return
    idx = 0
    while idx < len(raw):
        k = int(raw[idx]); idx += 1
        if k == 0: break
        n = int(raw[idx]); idx += 1

        if k == 1:
            if n > 63: print("More than 63 trials needed.")
            else: print(n)
            continue

        ans = -1
        for t in range(1, 64):
            f, comb = 0, 1
            for i in range(1, min(t, k) + 1):
                comb = comb * (t - i + 1) // i
                f += comb
                if f >= n:
                    ans = t
                    break
            if ans != -1: break

        if ans == -1: print("More than 63 trials needed.")
        else: print(ans)

if __name__ == "__main__": solve()
