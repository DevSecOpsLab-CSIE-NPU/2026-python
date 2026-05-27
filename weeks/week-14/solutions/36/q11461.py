# Square Numbers 解答程式
# 題目 11461: UVA — Square Numbers
# 計算區間 [a, b] 中完全平方數的個數

import math

def count_squares(a, b):
    """
    計算閉區間 [a, b] 中完全平方數的個數
    
    思路:
    - 找出 sqrt(a) 向上取整的值 (最小的完全平方數底數)
    - 找出 sqrt(b) 向下取整的值 (最大的完全平方數底數)
    - 計算兩者之間的整數個數
    
    參數:
        a: 區間左端點
        b: 區間右端點
    
    返回:
        完全平方數的個數
    """
    # 計算最小的 i，使得 i^2 >= a
    min_i = math.ceil(math.sqrt(a))
    
    # 計算最大的 i，使得 i^2 <= b
    max_i = math.floor(math.sqrt(b))
    
    # 如果 min_i > max_i，表示沒有完全平方數
    if min_i > max_i:
        return 0
    
    # 完全平方數的個數 = max_i - min_i + 1
    return max_i - min_i + 1

def main():
    """
    主程式：讀取輸入並輸出結果
    """
    while True:
        a, b = map(int, input().split())
        
        # 輸入 0 0 表示結束
        if a == 0 and b == 0:
            break
        
        result = count_squares(a, b)
        print(result)

if __name__ == '__main__':
    main()
