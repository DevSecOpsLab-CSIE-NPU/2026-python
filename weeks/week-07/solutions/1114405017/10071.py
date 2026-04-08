import sys

def solve():
    # 從標準輸入讀取所有資料，並以空白/換行分割
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # 第一個數字為 N，代表集合 S 的元素個數
    n = int(input_data[0])
    
    # 接下來的 N 個數字為集合 S 的元素內容
    s = [int(x) for x in input_data[1:n+1]]
    
    # 建立一個字典（Hash Map）來儲存左半部算式的結果
    # Key: 總和數值, Value: 該數值出現的次數
    sum_counts = {}
    
    # --- 階段一：處理左半部 (a + b + c) ---
    # 使用三層迴圈窮舉所有 a, b, c 的組合
    # 複雜度為 O(N^3)
    for a in s:
        for b in s:
            for c in s:
                lhs = a + b + c  # LHS = Left Hand Side
                # 將計算結果存入字典，若已存在則次數加 1
                if lhs in sum_counts:
                    sum_counts[lhs] += 1
                else:
                    sum_counts[lhs] = 1
                    
    ans = 0
    
    # --- 階段二：處理右半部 (f - e - d) ---
    # 根據公式變形：a + b + c = f - d - e
    # 我們同樣使用三層迴圈窮舉 f, d, e
    # 複雜度同樣為 O(N^3)
    for f in s:
        for d in s:
            for e in s:
                rhs = f - d - e  # RHS = Right Hand Side
                
                # 檢查右半部的結果是否存在於左半部的字典中
                # 如果存在，代表找到了一組 (a, b, c, d, e, f) 滿足等式
                if rhs in sum_counts:
                    # 累加該數值在左半部出現的所有組合次數
                    ans += sum_counts[rhs]
                    
    # --- 階段三：輸出結果 ---
    # 最終輸出的 ans 即為滿足 a + b + c + d + e = f 的六元組總數
    print(ans)

# 程式執行進入點
if __name__ == "__main__":
    solve()