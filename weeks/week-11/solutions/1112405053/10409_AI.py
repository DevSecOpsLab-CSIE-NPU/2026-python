def solve():
    """
    貪心演算法 + 雙指標解法
    
    思路：
    1. 將物品由小到大排序
    2. 使用双指標 (left, right)
    3. 嘗試配對最輕 (left) 和最重 (right) 的物品
    4. 如果總重 <= W，兩者一起搬；否則最重的單獨搬
    """
    n, W = map(int, input().split())
    weights = list(map(int, input().split()))
    
    # 按照重量排序
    weights.sort()
    
    trips = 0
    left = 0
    right = n - 1
    
    # 雙指標法
    while left <= right:
        if left == right:
            # 只剩一個物品，單獨搬
            trips += 1
            break
        
        # 嘗試配對最輕和最重的物品
        if weights[left] + weights[right] <= W:
            # 兩個一起搬
            left += 1
            right -= 1
            trips += 1
        else:
            # 最重的單獨搬（因為跟最輕的都配不了，其他更重的也不行）
            right -= 1
            trips += 1
    
    print(trips)


if __name__ == "__main__":
    solve()
