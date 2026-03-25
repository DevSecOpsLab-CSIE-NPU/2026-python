import sys

# 增加遞迴深度以防萬一，但在 BIT 實作中非必要
sys.setrecursionlimit(200005)

def solve():
    # 使用快速讀取
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    N = int(input_data[idx])
    Q = int(input_data[idx+1])
    idx += 2
    
    # 建立現象樹 (Binary Indexed Tree)
    # bit[i] 儲存的是 XOR 和
    bit = [0] * (N + 1)
    
    # 目前每個函數的狀態 (0: 增, 1: 減)
    # 初始皆為 0
    current_state = [0] * (N + 1)

    def update(i, delta):
        while i <= N:
            bit[i] ^= delta
            i += i & (-i)

    def query(i):
        res = 0
        while i > 0:
            res ^= bit[i]
            i -= i & (-i)
        return res

    results = []
    for _ in range(Q):
        v = int(input_data[idx])
        if v == 1:
            pos = int(input_data[idx+1])
            # 反轉狀態：0->1, 1->0
            update(pos, 1)
            idx += 2
        else:
            L = int(input_data[idx+1])
            R = int(input_data[idx+2])
            # 區間 XOR 查詢
            ans = query(R) ^ query(L-1)
            results.append(str(ans))
            idx += 3
    
    # 一次性輸出減少 I/O 次數
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()