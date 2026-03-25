import sys

# 讀取標準輸入的每一行
for line in sys.stdin:
    try:
        # 去除空白並分割字串
        parts = line.split()
        
        # 如果該行沒有內容則跳過 
        if not parts:
            continue
            
        # 讀取兩個整數
        a = int(parts[0])
        b = int(parts[1])
        
        # 計算並輸出絕對值差
        print(abs(a - b))
        
    except ValueError:
        # 處理可能的轉換錯誤
        pass
