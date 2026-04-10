import sys

# 進階版：使用樹狀數組 (BIT) 達到 O(N log^2 N) 效能
def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    n = int(input_data[0])
    # 題目給的是從第 2 頭到第 N 頭的資訊
    a = [int(x) for x in input_data[1:]]
    
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

    # 初始化所有編號皆可用（設為 1）
    for i in range(1, n + 1):
        update(i, 1)
        
    ans = [0] * n
    # 由後往前推
    for i in range(n - 1, 0, -1):
        k = a[i-1] + 1
        low, high = 1, n
        pos = n
        while low <= high:
            mid = (low + high) // 2
            if query(mid) >= k:
                pos = mid
                high = mid - 1
            else:
                low = mid + 1
        ans[i] = pos
        update(pos, -1) # 移除已使用的編號
        
    # 最後剩下的就是第一頭牛
    for i in range(1, n + 1):
        if query(i) == 1:
            ans[0] = i
            break
            
    print('\n'.join(map(str, ans)))

if __name__ == "__main__":
    solve()