def solve():
    """
    搬移物品 3 - 順序搬運 + 多車並行
    
    思路：
    1. 物品的順序不能改變，必須依序搬運
    2. 每一輪，m 輛車同時出發
    3. 每輛車在出發前盡可能地按順序裝物品，直到無法再裝
    4. 如果還有物品未搬，進行下一輪
    
    關鍵：
    - 用一個全局的物品索引 item_idx 追蹤下一個要搬的物品
    - 每一輪都讓 m 輛車依序裝物品
    - 直到所有物品都被搬走
    """
    n, m, W = map(int, input().split())
    weights = list(map(int, input().split()))
    
    rounds = 0
    item_idx = 0  # 指向下一個要搬的物品
    
    # 模擬多輪搬運
    while item_idx < n:
        rounds += 1
        
        # 這一輪，m 輛車同時出發
        for truck in range(m):
            if item_idx >= n:
                # 所有物品都搬完了
                break
            
            # 當前車能裝的總重量
            current_load = 0
            
            # 當前車盡可能地裝物品（按順序）
            while item_idx < n and current_load + weights[item_idx] <= W:
                current_load += weights[item_idx]
                item_idx += 1
    
    print(rounds)


if __name__ == "__main__":
    solve()
