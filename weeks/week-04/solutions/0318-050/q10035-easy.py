# 檔名: q10035-easy.py
# 這是 UVA 10035 的簡易好記版 (Easy Version)

import sys

# 1. 直接逐行讀取輸入
for line in sys.stdin:
    parts = line.split()
    if len(parts) != 2:
        continue
        
    a, b = int(parts[0]), int(parts[1])
    
    # 遇到 0 0 就結束程式
    if a == 0 and b == 0:
        break
        
    ans = 0  # 統計總共進位幾次
    c = 0    # 記錄當下有沒有進位 (0 或 1)
    
    # 2. 只要其中一個數字還沒被除到變成 0，就繼續算
    while a > 0 or b > 0:
        # 把兩者的個位數，加上前一次的進位 c 加起來
        total = (a % 10) + (b % 10) + c
        
        if total >= 10:
            ans += 1
            c = 1  # 滿 10 進位，留給下一個位數
        else:
            c = 0  # 沒滿 10，進位歸零
            
        # 3. 雙雙除以 10 (把最後一位數切掉)
        a //= 10
        b //= 10
        
    # 4. 根據進位次數印出對應的句子
    if ans == 0:
        print("No carry operation.")
    elif ans == 1:
        print("1 carry operation.")
    else:
        print(f"{ans} carry operations.")