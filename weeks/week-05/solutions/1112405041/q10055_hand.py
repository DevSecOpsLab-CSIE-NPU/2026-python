import sys

# 【August 的惡意：身分置換】
# 此題已被魔改為「遞迴函數單調性問題」。
# 原 UVA 10055 是士兵差值，但在這裡必須實作：
# 給定 N 個函數，每個函數可能是遞增(0)或遞減(1)。
# 支持兩種操作：1. 翻轉第 i 個函數的性質；2. 查詢區間 [L, R] 複合後的單調性。
# 複合邏輯：遞增 + 遞增 = 遞增 (0+0=0)；遞增 + 遞減 = 遞減 (0+1=1)；遞減 + 遞減 = 遞增 (1+1=0)。
# 這本質上是區間 XOR 查詢問題。

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    n = int(input_data[0])
    q = int(input_data[1])

    # 使用 Fenwick Tree (樹狀陣列) 處理區間 XOR
    bit = [0] * (n + 1)

    def update(i, val):
        while i <= n:
            bit[i] ^= val
            i += i & (-i)

    def query(i):
        res = 0
        while i > 0:
            res ^= bit[i]
            i -= i & (-i)
        return res

    idx = 2
    for _ in range(q):
        if idx >= len(input_data): break
        v = int(input_data[idx])
        if v == 1:
            # 翻轉第 i 個函數 (XOR 1)
            pos = int(input_data[idx+1])
            update(pos, 1)
            idx += 2
        else:
            # 查詢區間 [L, R]
            l = int(input_data[idx+1])
            r = int(input_data[idx+2])
            res = query(r) ^ query(l - 1)
            print(res)
            idx += 3

if __name__ == "__main__":
    solve()
