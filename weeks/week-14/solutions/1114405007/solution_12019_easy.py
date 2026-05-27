"""
題目 12019 - Doom's Day Algorithm (計算星期幾) - 簡易版本
使用更簡潔的寫法，易於在考場快速實現
"""

# 星期清單
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# 每月 Doomsday 日期
doomsdays = [0, 10, 21, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]

# 2012 年 Doomsday 是星期三 (3)
year_doomsday = 3

# 主程式
t = int(input())

for _ in range(t):
    m, d = map(int, input().split())
    
    # 計算偏移天數
    offset = d - doomsdays[m]
    
    # 計算星期幾
    day_index = (year_doomsday + offset) % 7
    
    # 輸出結果
    print(days[day_index])
