# 檔名: q490-easy.py
# 這是 UVA 490 的簡易好記版 (Easy Version)

import sys

# 1. 讀取所有輸入，並依據換行符號切成一行一行的字串列表
lines = sys.stdin.read().splitlines()

if lines:
    # 2. 找出最長那行的長度 (最直白暴力的寫法)
    max_len = 0
    for line in lines:
        if len(line) > max_len:
            max_len = len(line)
            
    # 3. 外層迴圈控制「直行」的索引 (決定最後要印出幾行)
    for i in range(max_len):
        result = ""
        
        # 4. 內層迴圈控制「橫列」，而且要從最後一行「往回讀」 (reversed)
        for line in reversed(lines):
            # 判斷這行有沒有夠長，夠長就抓字元，不夠長就補空白陷阱
            if i < len(line):
                result += line[i]
            else:
                result += " "
                
        # 5. 拼完一整排後，直接印出結果
        print(result)