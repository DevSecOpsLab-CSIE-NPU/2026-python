# UVA 10812 - Beat the Spread!
# 解題思路：
# 已知兩隊分數之和 S 和最大分差 D
# 設較高分為 H，較低分為 L
# H + L = S  (分數之和)
# H - L = D  (分數之差)
# 解得：H = (S + D) / 2, L = (S - D) / 2
# 條件：H、L 都必須是非負整數

def solve_beat_the_spread():
    """
    求解 Beat the Spread 問題
    """
    n = int(input())
    for _ in range(n):
        S, D = map(int, input().split())
        
        # 檢查 (S + D) 和 (S - D) 是否都能整除 2
        if (S + D) % 2 != 0 or (S - D) % 2 != 0:
            print("impossible")
            continue
        
        # 計算假設的高分和低分
        high = (S + D) // 2
        low = (S - D) // 2
        
        # 檢查低分是否為負數
        if low < 0:
            print("impossible")
        else:
            print(high, low)

if __name__ == "__main__":
    solve_beat_the_spread()
