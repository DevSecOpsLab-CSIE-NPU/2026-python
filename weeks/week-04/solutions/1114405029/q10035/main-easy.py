while True:
    try:
        # 讀取一列輸入並拆分成兩個字串
        line = input().split()
        n1 = line[0]
        n2 = line[1]
        
        # 遇到 0 0 則停止
        if n1 == '0' and n2 == '0':
            break
            
        # 將字串反轉，方便從個位數（索引 0）開始跑迴圈
        n1 = n1[::-1]
        n2 = n2[::-1]
        
        carries = 0 # 總進位次數
        carry = 0   # 當前的進位值 (0 或 1)
        
        # 跑足夠長的次數（取兩數中最長的那一個）
        length = max(len(n1), len(n2))
        
        for i in range(length):
            # 如果索引超過字串長度，就當作 0
            d1 = int(n1[i]) if i < len(n1) else 0
            d2 = int(n2[i]) if i < len(n2) else 0
            
            # 計算當前位的總和
            total = d1 + d2 + carry
            
            if total >= 10:
                carries += 1
                carry = 1
            else:
                carry = 0
        
        # 判斷輸出格式
        if carries == 0:
            print("No carry operation.")
        elif carries == 1:
            print("1 carry operation.")
        else:
            print(f"{carries} carry operations.")
            
    except EOFError:
        break