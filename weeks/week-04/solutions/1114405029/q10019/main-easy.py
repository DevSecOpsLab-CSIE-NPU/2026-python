import sys

# 持續讀取輸入，直到沒有資料為止
for line in sys.stdin:
    # 將每一行內容切開（預設是用空白切）
    parts = line.split()
    
    # 如果這一行是空的，就跳過
    if not parts:
        continue
    
    # 把切開的字串轉成整數
    # n1 是己方士兵，n2 是敵方士兵
    n1 = int(parts[0])
    n2 = int(parts[1])
    
    # 計算兩者相減的結果
    result = n1 - n2
    
    # 如果相減是負的，就把它變成正的（取絕對值）
    if result < 0:
        result = result * -1
    
    # 印出答案
    print(result)