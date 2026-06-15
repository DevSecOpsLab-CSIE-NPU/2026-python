import sys

def solve():
    """
    UVA 10268 魔改版：丟水球 (經典 Egg Dropping 問題)
    解法：
    給定 K 個水球與 N 層樓，求最糟情況下的最少測試次數 T。
    轉換問題：給定 T 次測試機會與 K 個水球，最大能測量的樓層數 F(T, K) 是多少？
    公式為：F(T, K) = sum_{i=1 to K} C(T, i)
    若 F(T, K) >= N，則 T 次測試足夠。
    因為 N 很大 (64-bit)，我們直接尋找最小的 T 使得 F(T, K) >= N。
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    ptr = 0
    while ptr < len(input_data):
        K = int(input_data[ptr])
        if K == 0:
            break
        N = int(input_data[ptr+1])
        ptr += 2

        # 特殊情況：只有 1 個水球，必須逐層丟，需要 N 次
        if K == 1:
            if N > 63:
                print("More than 63 trials needed.")
            else:
                print(N)
            continue

        # 尋找 T
        found = False
        for t in range(1, 64):
            # 計算 F(t, K) = C(t, 1) + C(t, 2) + ... + C(t, K)
            f_val = 0
            comb = 1
            for i in range(1, min(t, K) + 1):
                comb = comb * (t - i + 1) // i
                f_val += comb
                if f_val >= N:
                    print(t)
                    found = True
                    break
            if found:
                break

        if not found:
            print("More than 63 trials needed.")

if __name__ == "__main__":
    solve()
