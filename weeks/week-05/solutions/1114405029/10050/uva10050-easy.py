# UVA 10050 - Hartals
# easy 版本：使用最直觀方式實作


# 讀入測試資料組數
t = int(input())

# 逐組處理
for _ in range(t):
    # 讀入模擬天數
    n = int(input())

    # 讀入政黨數量
    p = int(input())

    # 用集合記錄所有有效罷工日
    hartal_days = set()

    # 逐一讀入每個政黨的罷工週期
    for _ in range(p):
        h = int(input())

        # 從第 h 天開始，每隔 h 天罷工一次
        for day in range(h, n + 1, h):
            # 排除星期五與星期六
            if day % 7 != 6 and day % 7 != 0:
                hartal_days.add(day)

    # 輸出有效罷工日總數
    print(len(hartal_days))