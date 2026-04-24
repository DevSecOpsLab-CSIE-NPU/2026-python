# 檔名: q10071-easy.py
# 這是 UVA 10071 (六元組問題) 的簡易好記版 (Easy Version)

import sys

# 1. 萬用讀取法：把所有輸入切成一維整數陣列
data = [int(x) for x in sys.stdin.read().split()]

idx = 0
while idx < len(data):
    n = data[idx]
    idx += 1
    
    s_set = data[idx : idx + n]  # 抓出這組測資的 n 個數字
    idx += n
    
    # 2. 建立一個普通字典，用來儲存 a+b+c 的和以及它們出現的次數
    left_sums = {}
    
    # 3. 窮舉所有 a, b, c 的組合，計算它們的和
    for a in s_set:
        for b in s_set:
            for c in s_set:
                current_sum = a + b + c
                # 如果和已經存在字典中，次數就加 1；否則初始化為 1
                left_sums[current_sum] = left_sums.get(current_sum, 0) + 1
                
    # 4. 初始化總解數
    total_solutions = 0
    
    # 5. 窮舉所有 f, d, e 的組合，計算 f-d-e 的差
    for f in s_set:
        for d in s_set:
            for e in s_set:
                right_diff = f - d - e
                # 如果這個差值存在於 left_sums 字典中，就將其出現的次數加到總解數中
                if right_diff in left_sums:
                    total_solutions += left_sums[right_diff]
                    
    # 6. 印出結果
    print(total_solutions)