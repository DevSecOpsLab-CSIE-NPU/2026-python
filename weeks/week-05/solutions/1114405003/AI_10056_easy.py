"""
10056 - 骰子遊戲獲勝機率【簡單版本 - AI教學版】

【核心概念】
N 個玩家輪流擲骰子，成功機率 p
求玩家 i 的獲勝機率

【公式】
P(i) = (1-p)^(i-1) × p / (1 - (1-p)^N)

分子：前 i-1 個玩家都失敗 × 玩家 i 成功
分母：排除全部失敗的情況
"""

def win_prob(n, p, i):
    """計算玩家 i 的獲勝機率"""
    if p == 1.0:
        return 1.0 if i == 1 else 0.0
    
    fail = 1 - p
    numerator = (fail ** (i - 1)) * p
    denominator = 1 - (fail ** n)
    
    return numerator / denominator


if __name__ == "__main__":
    print(f"{win_prob(1, 0.5, 1):.4f}")      # 1.0000
    print(f"{win_prob(2, 0.5, 1):.4f}")      # 0.6667
    print(f"{win_prob(2, 0.5, 2):.4f}")      # 0.3333
    print(f"{win_prob(3, 1/6, 1):.4f}")      # 0.3956
