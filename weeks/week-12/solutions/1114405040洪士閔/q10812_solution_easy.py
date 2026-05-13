"""
題目 10812 - Beat the Spread! (簡易版)

核心公式：
- 高分 = (S + D) / 2
- 低分 = (S - D) / 2
- 需要檢查：(S+D) 為偶數 且 低分 >= 0
"""


def find_scores(s, d):
    """計算兩隊得分，若無解返回 None"""
    if (s + d) % 2 != 0 or s < d:
        return None
    return ((s + d) // 2, (s - d) // 2)


# 讀取測試組數
n = int(input())

# 每組測試
for _ in range(n):
    s, d = map(int, input().split())
    result = find_scores(s, d)
    
    if result is None:
        print("impossible")
    else:
        print(f"{result[0]} {result[1]}")
