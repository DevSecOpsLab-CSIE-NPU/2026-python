def solve():
    """
    搬運問題 - 考慮物品類別限制
    
    思路：
    1. 按物品類別分組
    2. 對每個類別中的物品進行排序
    3. 使用雙指標法：配對最輕和最重的物品
    4. 如果無法配對，最重的單獨搬
    5. 累計所有類別的搬運次數
    
    關鍵：不同類別的物品不能一起搬，所以要分別處理
    """
    n, W = map(int, input().split())
    
    # 按類別分組物品
    categories = {}
    for _ in range(n):
        w, c = map(int, input().split())
        if c not in categories:
            categories[c] = []
        categories[c].append(w)
    
    total_trips = 0
    
    # 對每個類別分別進行配對
    for category, weights in categories.items():
        # 排序該類別的物品
        weights.sort()
        
        left = 0
        right = len(weights) - 1
        
        # 雙指標法配對該類別的物品
        while left <= right:
            if left == right:
                # 只剩一個物品，單獨搬
                total_trips += 1
                break
            
            # 嘗試配對最輕和最重的物品
            if weights[left] + weights[right] <= W:
                # 兩個一起搬
                left += 1
                right -= 1
                total_trips += 1
            else:
                # 最重的無法與最輕的配對，所以單獨搬
                # (因為同類別中其他物品都比最輕的重)
                right -= 1
                total_trips += 1
    
    print(total_trips)


if __name__ == "__main__":
    solve()
