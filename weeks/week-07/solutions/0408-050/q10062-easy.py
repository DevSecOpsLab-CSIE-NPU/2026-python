# 檔名: q10062-easy.py
# 這是 UVA 10062 (Lost Cows) 的簡易好記版 (Easy Version)

import sys

# 讀取所有輸入並過濾掉換行與空白
input_data = sys.stdin.read().split()
idx = 0

# UVA 測資通常包含多組測試資料直到 EOF
while idx < len(input_data):
    n = int(input_data[idx])
    idx += 1
    
    # 讀取這組測資接下來的 N-1 個數字
    smaller_counts = [int(x) for x in input_data[idx : idx + n - 1]]
    idx += n - 1
    
    # 1. 建立一個包含所有可用數字的列表 (1 到 n)
    available = list(range(1, n + 1))
    
    # 2. 準備一個陣列來存放還原後的結果
    result = [0] * n
    
    # 題目沒有給第一頭牛的 smaller 數量 (因為必定為 0)，所以在前面補 0
    counts = [0] + smaller_counts
    
    # 3. 從最後一頭牛開始「由後往前」反推
    for i in range(n - 1, -1, -1):
        # 這頭牛前面有 counts[i] 頭比牠小，代表牠是剩下數字中的「第 counts[i] + 1 小」
        # 在 Python 陣列中，索引剛好就是 counts[i]
        rank_index = counts[i]
        
        # 4. 從可用數字列表中，利用索引直接找出這頭牛的編號，並將它從列表中移除
        cow_number = available.pop(rank_index)
        
        # 5. 將還原出的編號放到結果陣列的正確位置
        result[i] = cow_number
        
    # 計算並輸出正確排列
    for cow in result:
        print(cow)