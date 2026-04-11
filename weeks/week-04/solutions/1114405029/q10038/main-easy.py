import sys

# 逐行讀取輸入，因為每一行代表一組測試資料
for line in sys.stdin:
    # 將整行切開並轉換成數字列表
    parts = list(map(int, line.split()))
    
    # 如果這行是空的（例如多餘的換行），就跳過
    if not parts:
        continue
        
    n = parts[0]       # 第一個數字是長度 n
    nums = parts[1:]   # 剩下的才是數列內容
    
    # 如果只有一個數字，根據定義直接是 Jolly
    if n == 1:
        print("Jolly")
        continue
        
    # 建立一個檢查表，長度為 n
    # 我們會用到索引 1 到 n-1，所以長度設為 n
    present = [False] * n
    
    # 檢查是否失敗的旗標
    possible = True
    
    # 跑迴圈計算相鄰兩個數字的差
    for i in range(1, n):
        diff = abs(nums[i] - nums[i-1])
        
        # 判斷差值是否在 1 到 n-1 的範圍內
        if 1 <= diff < n:
            present[diff] = True # 標記這個差值出現過
        else:
            # 差值太大或太小，這組一定不符合
            possible = False
            break
            
    # 如果目前還沒失敗，再最後檢查一次 1 到 n-1 是否都有被標記
    if possible:
        for i in range(1, n):
            if not present[i]:
                possible = False
                break
                
    # 輸出最終結果
    if possible:
        print("Jolly")
    else:
        print("Not jolly")