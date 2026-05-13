"""
UVA 10812 — Beat the Spread! 解題程式
題目說明：根據兩隊的分數之和 S 和分數之差 D，
求出兩隊各自的得分（較大的先輸出）。
"""


def solve_beat_the_spread(S, D):
    """
    根據分數之和和分數之差計算兩隊的得分。
    
    參數:
        S (int): 兩隊分數之和
        D (int): 兩隊分數之差的絕對值
    
    返回:
        tuple: 若有解，返回 (較高分, 較低分)；若無解，返回 None
    
    條件檢查:
        - 高分 = (S + D) / 2
        - 低分 = (S - D) / 2
        - S + D 必須為偶數
        - 低分必須非負（S >= D）
    """
    
    # 檢查 S + D 是否為偶數
    if (S + D) % 2 != 0:
        return None
    
    # 計算較高分和較低分
    higher_score = (S + D) // 2
    lower_score = (S - D) // 2
    
    # 檢查較低分是否為非負整數
    if lower_score < 0:
        return None
    
    # 返回結果（較大分數在前）
    return (higher_score, lower_score)


def main():
    """
    主程式：讀取輸入並輸出結果
    """
    n = int(input())  # 讀取測試資料組數
    
    for _ in range(n):
        S, D = map(int, input().split())  # 讀取每組測試資料
        result = solve_beat_the_spread(S, D)
        
        if result is None:
            # 無解情況
            print("impossible")
        else:
            # 有解情況，輸出兩隊分數（較大的先輸出）
            higher, lower = result
            print(f"{higher} {lower}")


if __name__ == "__main__":
    main()
