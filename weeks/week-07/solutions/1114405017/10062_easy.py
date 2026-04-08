import sys

def solve():
    # 快速讀取所有輸入
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    # 補上第一頭牛的 0，其餘為輸入數據
    pre_smaller = [0] + [int(x) for x in input_data[1:]]
    
    # bit[i] 儲存該位置是否還有可用編號 (1 代表可用, 0 代表已用)
    bit = [0] * (n + 1)
    
    def update(i, delta):
        while i <= n:
            bit[i] += delta
            i += i & (-i)

    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s

    # 初始化 BIT：所有編號一開始都是 1 (可用)
    for i in range(1, n + 1):
        update(i, 1)

    ans = [0] * n
    # 逆向還原：從最後一頭牛往前找
    for i in range(n - 1, -1, -1):
        target_rank = pre_smaller[i] + 1
        
        # 二分搜尋：在 BIT 中尋找第 target_rank 小的編號
        low, high = 1, n
        pos = n
        while low <= high:
            mid = (low + high) // 2
            if query(mid) >= target_rank:
                pos = mid
                high = mid - 1
            else:
                low = mid + 1
        
        ans[i] = pos
        update(pos, -1)  # 標記該編號已使用

    # 輸出結果
    sys.stdout.write('\n'.join(map(str, ans)) + '\n')

if __name__ == '__main__':
    solve()