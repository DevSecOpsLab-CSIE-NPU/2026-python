"""
10041 - 最小距離問題【簡單版本 - AI教學版】

【核心概念】
給定 N 個親戚的位置，找一個位置 A 讓他們的距離和最小
答案是中位數

【步驟】
1️⃣ 排序所有位置
2️⃣ 找中位數位置
3️⃣ 計算到中位數的距離和
"""

def solve(relatives):
    """
    求解最小距離問題
    
    參數：relatives 親戚的位置列表
    返回：最小距離和
    """
    # 排序位置
    relatives.sort()
    
    # 找中位數（最優位置）
    median_index = (len(relatives) - 1) // 2
    median_position = relatives[median_index]
    
    # 計算距離和
    total_distance = sum(abs(position - median_position) for position in relatives)
    
    return total_distance


# ═══════════════════════════════════════════════════════════════════
# 測試
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # 測試用例
    print(solve([1, 2, 3]))        # 2
    print(solve([1, 2, 3, 4]))     # 4
    print(solve([10]))             # 0
    print(solve([1, 5]))           # 4
