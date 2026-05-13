"""
題目 10812 - Beat the Spread!

問題：給定兩隊分數之和 S 和差 D，求各隊得分

解法：
- 較高分 = (S + D) / 2
- 較低分 = (S - D) / 2
"""


def find_scores(s, d):
    """
    根據分數之和和之差，計算兩隊得分。
    
    參數：
        s (int): 分數之和
        d (int): 分數之差（絕對值）
    
    返回：
        tuple: (較高分, 較低分) 或 None（若無解）
    """
    # 檢查 S + D 是否為偶數
    if (s + d) % 2 != 0:
        return None
    
    # 計算兩隊得分
    higher = (s + d) // 2
    lower = (s - d) // 2
    
    # 檢查較低分是否為非負
    if lower < 0:
        return None
    
    return (higher, lower)


def main():
    """
    主程式：讀取輸入，處理多組測試資料。
    """
    # 讀取測試組數
    n = int(input())
    
    # 處理每組測試資料
    for _ in range(n):
        # 讀取分數之和和之差
        s, d = map(int, input().split())
        
        # 計算兩隊得分
        result = find_scores(s, d)
        
        # 輸出結果
        if result is None:
            print("impossible")
        else:
            higher, lower = result
            print(f"{higher} {lower}")


if __name__ == "__main__":
    main()
