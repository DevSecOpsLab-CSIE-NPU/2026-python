# UVA 10038 - Jolly Jumpers (簡單好記版)
# 學生：1114405035 賴彥廷

import sys

def solve():
    for line in sys.stdin:
        nums = list(map(int, line.split()))
        if not nums: continue
        
        n = nums[0]
        if n == 1:
            print("Jolly")
            continue
            
        # 計算相鄰差值的絕對值
        diffs = set()
        for i in range(1, n):
            d = abs(nums[i] - nums[i+1])
            if 1 <= d <= n - 1:
                diffs.add(d)
        
        # 如果集合大小等於 n-1，表示 1 到 n-1 都出現過
        if len(diffs) == n - 1:
            print("Jolly")
        else:
            print("Not jolly")

if __name__ == "__main__":
    solve()
