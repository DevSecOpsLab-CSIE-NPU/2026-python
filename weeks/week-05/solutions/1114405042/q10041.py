def solve_vito(data: list[int]) -> int:
    """
    計算 Vito 到所有親戚家最短的總距離。
    :param data: 一個整數列表，第一個元素是親戚的數量，後面跟著親戚家的門牌號碼
    :return: 最短的總距離
    """
    # 如果沒有親戚資料或只有數量，則總距離為 0
    if len(data) <= 1:
        return 0
        
    # 第一個數字是親戚的數量，這題的計算中可以忽略它
    r = data[0] 
    
    # 從第二個數字開始是所有親戚的門牌號碼
    houses = data[1:] 
    
    # 步驟 1：將門牌號碼從小到大排序。
    # 為什麼要排序？因為在數線上，到所有點距離總和最小的位置，就是「中位數」。
    houses.sort()
    
    # 步驟 2：找出中位數所在的索引位置
    # 如果有 3 個元素 (索引 0, 1, 2)，3 // 2 = 1 (正好是中間)
    # 如果有 4 個元素 (索引 0, 1, 2, 3)，4 // 2 = 2 (中間偏右，在數學上選中間任一點總距離都一樣小)
    mid_index = len(houses) // 2
    median = houses[mid_index]
    
    # 步驟 3：計算所有親戚家到中位數（新家）的距離總和
    total_distance = 0
    for house in houses:
        # 使用 abs() 取絕對值，因為距離不會是負數
        total_distance += abs(house - median)
        
    return total_distance
