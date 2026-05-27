# Doom's Day Algorithm 簡單版本
# 題目 12019: UVA — Doom's Day Algorithm
# 簡單易懂的寫法

from datetime import datetime

# 星期名稱對應表
# 對應 datetime.weekday() 的結果
# 0=Monday, 1=Tuesday, ..., 6=Sunday
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
            'Friday', 'Saturday', 'Sunday']

# 讀取測試用例數量
t = int(input())

# 重複執行每個測試用例
for _ in range(t):
    # 讀取月份和日期
    m, d = map(int, input().split())
    
    # 建立2012年該月份該日期的日期物件
    date = datetime(2012, m, d)
    
    # 取得星期幾 (0=Monday)
    day_index = date.weekday()
    
    # 輸出星期名稱
    print(weekdays[day_index])
