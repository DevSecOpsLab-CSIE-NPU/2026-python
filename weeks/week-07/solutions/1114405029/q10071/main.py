import sys
from collections import Counter

# 進階實作版：使用 collections.Counter 優化計數過程
# 核心演算法：折半搜尋 (Meet-in-the-middle)
# 將 a + b + c + d + e = f 轉換為 a + b + c = f - d - e
def solve():
    # 從標準輸入讀取所有資料並以空白分割
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # 第一個數字為集合大小 N
    n = int(input_data[0])
    # 接下來的 N 個數字為集合 S 的元素
    s = [int(x) for x in input_data[1:1+n]]
    
    # 建立一個 Counter 物件來儲存左半邊 (a + b + c) 的所有可能組合及其出現次數
    # Counter 本質上是一個高效的字典 (dict)，專門用於計數
    left_side_counts = Counter()
    
    # 三層迴圈枚舉 a, b, c 的所有組合，時間複雜度 O(N^3)
    for a in s:
        for b in s:
            for c in s:
                left_side_counts[a + b + c] += 1
                
    total_solutions = 0
    
    # 三層迴圈枚舉 f, d, e 的所有組合，尋找符合 f - d - e 的結果
    # 這樣做的總時間複雜度為 O(N^3) + O(N^3)，遠快於直接六層迴圈的 O(N^6)
    for f in s:
        for d in s:
            for e in s:
                # 計算右半邊移項後的目標值
                target_value = f - d - e
                # 如果目標值存在於左半邊的計數字典中，累加其出現次數
                if target_value in left_side_counts:
                    total_solutions += left_side_counts[target_value]
    
    # 輸出最終符合條件的六元組總數
    print(total_solutions)

if __name__ == "__main__":
    solve()