# 檔名: q10056-easy.py
# 這是 UVA 10056 (What is the Probability?) 的簡易好記版 (Easy Version)

import sys

# 1. 萬用讀取法：把所有輸入切成一維字串陣列
data = sys.stdin.read().split()

if data:
    S = int(data[0])  # 測資組數
    idx = 1
    
    for _ in range(S):
        N = int(data[idx])
        p = float(data[idx+1])
        i = int(data[idx+2])
        idx += 3
        
        # 2. 防呆陷阱：成功機率為 0 時沒人會贏，提早印出並結束這回合
        if p == 0:
            print("0.0000")
        else:
            # 3. 直接代入無窮等比級數公式： 首項 / (1 - 公比)
            # 首項 a = p * (1 - p)**(i - 1)
            # 公比 r = (1 - p)**N
            prob = (p * (1 - p)**(i - 1)) / (1 - (1 - p)**N)
            
            # 4. 格式化輸出小數點後四位
            print(f"{prob:.4f}")