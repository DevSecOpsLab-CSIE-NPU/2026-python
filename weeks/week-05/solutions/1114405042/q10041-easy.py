def solve_vito_easy(data: list[int]) -> int:
    """
    這是一個更容易記憶且簡潔的版本（Pythonic）。
    核心原理一樣：找出中位數，計算所有點到中位數的距離和。
    """
    # 如果沒資料，直接回傳 0
    if len(data) <= 1:
        return 0
        
    # 第一個元素是數量，後面才是門牌。
    # 用切片 data[1:] 略過第一個元素。
    houses = data[1:]
    
    # 步驟 1: 排序 (找中位數必須先排序)
    houses.sort()
    
    # 步驟 2: 取得中位數 (長度除以 2 取商，代表中間的索引)
    median = houses[len(houses) // 2]
    
    # 步驟 3: 利用 sum() 函數搭配生成器，一行計算出總距離
    # 意思為「對每一個房子 h，計算 abs(h - median) 並將結果加總」
    return sum(abs(h - median) for h in houses)
