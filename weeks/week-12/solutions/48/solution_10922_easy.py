"""
UVA 10922 — 2 the 9s 簡單版本
更簡單易記的寫法

核心思想：
- 只需要記住：重複將數字加起來，直到得到9或判斷不是9的倍數
- 計數每次加總的次數就是深度
"""


def nine_degree_simple(num_str):
    """
    最簡單的解法
    
    簡化概念：
    - 只需要一個 while 迴圈
    - 每次計算所有數字之和
    - 計算次數就是深度
    """
    # 一直將數字加起來
    current = num_str
    depth = 0
    
    while True:
        # 計算各位數字之和
        digit_sum = sum(int(d) for d in current)
        depth += 1
        current = str(digit_sum)
        
        # 如果得到一位數
        if len(current) == 1:
            if current == "9":
                return f"{num_str} is a multiple of 9.", depth
            else:
                return f"{num_str} is not a multiple of 9.", 0


# 測試
if __name__ == "__main__":
    result, depth = nine_degree_simple("9")
    print(f"{result} 深度={depth}")  # 深度=1
    
    result, depth = nine_degree_simple("18")
    print(f"{result} 深度={depth}")  # 深度=1
    
    result, depth = nine_degree_simple("999")
    print(f"{result} 深度={depth}")  # 深度=2
