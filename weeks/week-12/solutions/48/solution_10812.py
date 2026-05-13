"""
UVA 10812 — Beat the Spread! 解決方案
給定和S與差D，求兩隊各自得分（較大分數先輸出）

公式解析：
- 設兩隊得分為 a (較大) 和 b (較小)
- 則：a + b = S (和)
       a - b = D (差)
- 解得：a = (S + D) / 2
       b = (S - D) / 2
- 條件檢查：
  1. (S + D) 必須是偶數
  2. a 和 b 都必須是非負整數
"""


def get_scores(s, d):
    """
    計算兩隊得分
    
    參數：
        s (int): 兩隊分數之和
        d (int): 兩隊分數之差的絕對值
    
    返回：
        str: 較大分數和較小分數（用空格分隔），或 'impossible'
    """
    # 檢查 (S + D) 是否能被 2 整除
    if (s + d) % 2 != 0:
        return "impossible"
    
    # 計算較大分數和較小分數
    larger_score = (s + d) // 2
    smaller_score = (s - d) // 2
    
    # 檢查是否存在負數得分
    if smaller_score < 0:
        return "impossible"
    
    return f"{larger_score} {smaller_score}"


def main():
    """主程式：讀取輸入並輸出結果"""
    n = int(input())
    for _ in range(n):
        s, d = map(int, input().split())
        print(get_scores(s, d))


if __name__ == "__main__":
    main()
