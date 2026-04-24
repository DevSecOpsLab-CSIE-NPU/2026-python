# 檔名: q10050-easy.py
# 這是 UVA 10050 (Hartals) 的簡易好記版 (Easy Version)

import sys

# 1. 一次把所有輸入讀進來，並全部轉換成整數陣列
data = [int(x) for x in sys.stdin.read().split()]

if data:
    test_cases = data[0]
    idx = 1
    
    for _ in range(test_cases):
        N = data[idx]      # 模擬的總天數
        P = data[idx + 1]  # 政黨的數量
        idx += 2
        
        parties = data[idx : idx + P]  # 抓出這 P 個政黨的罷會參數
        idx += P
        
        # 2. 建立一個集合 (set)，用來記錄究竟有哪些天發生了罷會
        hartals = set()
        
        # 3. 走訪每個政黨的罷會參數
        for h in parties:
            for day in range(h, N + 1, h):
                # 星期五 (day % 7 == 6) 與 星期六 (day % 7 == 0) 是假日，不計算損失
                if day % 7 != 6 and day % 7 != 0:
                    hartals.add(day)  # 集合會自動忽略重複的日子，不用擔心同一天加兩次
                    
        # 4. 集合裡有幾個元素，就代表損失了幾天的工作天
        print(len(hartals))