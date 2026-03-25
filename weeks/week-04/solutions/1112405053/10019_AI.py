import sys

# 逐行讀取輸入，每行應有兩個整數
for line in sys.stdin:
    tokens = line.split()
    # 確認資料完整後，輸出兩數絕對差
    if len(tokens) >= 2:
        print(abs(int(tokens[0]) - int(tokens[1])))
