# 檔名: q10019-easy.py
# 這是 UVA 10019 (實為 UVA 10055) 的簡易好記版 (Easy Version)

import sys

# 1. 大絕招：一次讀取所有輸入，並過濾掉所有換行與空白，切成一個一維的字串陣列
data = sys.stdin.read().split()

# 2. 利用 range(起點, 終點, 步長) 的特性，每次跳 2 格 (因為一組測資有 2 個數字)
for i in range(0, len(data), 2):
    a = int(data[i])
    b = int(data[i+1])
    
    # 3. 直接相減並使用 abs() 取得絕對值印出
    print(abs(a - b))