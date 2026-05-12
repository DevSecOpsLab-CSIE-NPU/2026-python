def can_transport(weights, m, W):
    """
    檢查是否能用 m 輛車在載重限制為 W 的情況下完成1輪搬運
    
    :param weights: 物品重量列表
    :param m: 車數
    :param W: 載重限制
    :return: 能否搬完所有物品
    """
    trucks_used = 1
    current_load = 0
    
    for weight in weights:
        if current_load + weight <= W:
            # 當前車還能裝
            current_load += weight
        else:
            # 當前車裝不下，需要用下一輛車
            trucks_used += 1
            current_load = weight
            
            # 如果超過了車的數量，無法完成
            if trucks_used > m:
                return False
    
    return True


def solve():
    """
    用二分搜索找最小的載重限制 W
    
    思路：
    - 左界：最重的單個物品（必須能裝下最重物品）
    - 右界：所有物品的總和（最多情況下1輛車搬所有）
    - 二分搜索過程中，如果 can_transport(weights, m, W) 返回 True，
      就嘗試更小的 W；否則增加 W
    """
    n, m = map(int, input().split())
    weights = list(map(int, input().split()))
    
    # 二分搜索邊界
    left = max(weights)  # 最小值至少是最重物品
    right = sum(weights)  # 最大值是所有物品的和
    
    result = right
    
    # 二分搜索
    while left <= right:
        mid = (left + right) // 2
        
        if can_transport(weights, m, mid):
            # 能搬完，嘗試更小的 W
            result = mid
            right = mid - 1
        else:
            # 無法搬完，需要更大的 W
            left = mid + 1
    
    print(result)


if __name__ == "__main__":
    solve()
