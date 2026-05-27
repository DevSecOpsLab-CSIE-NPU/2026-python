"""
題目 12019 - Doom's Day Algorithm (計算星期幾) - 手打版本
學生自己手動編寫的解題程式
"""

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
doomsdays = [0, 10, 21, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]
year_doomsday = 3  # Wednesday

t = int(input())
for _ in range(t):
    m, d = map(int, input().split())
    offset = d - doomsdays[m]
    day_index = (year_doomsday + offset) % 7
    print(days[day_index])
