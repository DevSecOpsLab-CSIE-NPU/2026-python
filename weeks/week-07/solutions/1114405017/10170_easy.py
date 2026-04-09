import sys

# 讀取標準輸入中的每一行
for line in sys.stdin:
    # 同時解析 S (起始人數) 與 D (目標天數)
    s, d = map(int, line.split())
    
    # 邏輯簡化：不斷從目標天數 D 扣除當前團體的人數
    # 當 d 變成小於或等於 0，代表第 D 天就落在這個人數的團體裡
    while d > s:
        d -= s
        s += 1

    print(s)
