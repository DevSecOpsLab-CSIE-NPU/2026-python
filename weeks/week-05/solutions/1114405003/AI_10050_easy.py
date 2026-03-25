"""
10050 - 罷會損失工作天【簡單版本 - AI教學版】

【核心概念】
N 個政黨輪流罷會，政黨 h 每隔 h 天罷會一次
計算工作天（星期一到四）因罷會損失的天數

【步驟】
1️⃣ 遍歷每一天
2️⃣ 判斷是否工作天（星期一到四）
3️⃣ 檢查是否有政黨罷會
4️⃣ 如果是工作天且有罷會，損失 +1
"""

def solve(n, hartal_params):
    """
    計算罷會損失的工作天數
    
    參數：
    - n: 天數
    - hartal_params: 各政黨的罷會週期
    
    返回：損失的工作天數
    """
    loss = 0
    
    # 每一天
    for day in range(1, n + 1):
        # 星期（0=日, 1=一, 2=二, 3=三, 4=四, 5=五, 6=六）
        day_of_week = (day - 1) % 7
        
        # 是否工作天（星期一到四）
        if day_of_week not in [1, 2, 3, 4]:
            continue
        
        # 是否有政黨罷會
        if any(day % h == 0 for h in hartal_params):
            loss += 1
    
    return loss


if __name__ == "__main__":
    print(solve(7, [3]))       # 1
    print(solve(10, [2, 3]))   # 5
