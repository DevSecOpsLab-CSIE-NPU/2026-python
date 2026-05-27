import datetime

# Doomsday列表 (month, day) - 在任何年份都是doomsday的日期
# 对于2011年（非闰年）：1/10, 2/21, 3/*, 4/4, 5/9, 6/6, 7/11, 8/8, 9/5, 10/10, 11/7, 12/12
# 其中3月的doomsday是3/0（3月前一天，即2月最后一天）

def get_doomsday_date(month):
    """获取该月的doomsday日期"""
    if month == 1:
        return (1, 10)  # 非闰年
    elif month == 2:
        return (2, 21)  # 非闰年
    elif month == 3:
        return (3, 7)   # Calculated as 3/0 + 7 = 3/7
    elif month == 4:
        return (4, 4)
    elif month == 5:
        return (5, 9)
    elif month == 6:
        return (6, 6)
    elif month == 7:
        return (7, 11)
    elif month == 8:
        return (8, 8)
    elif month == 9:
        return (9, 5)
    elif month == 10:
        return (10, 10)
    elif month == 11:
        return (11, 7)
    elif month == 12:
        return (12, 12)

# 2011年的doomsday是Monday
# 使用datetime来计算
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

T = int(input())
results = []
for _ in range(T):
    M, D = map(int, input().split())
    
    # 使用datetime来获取星期几
    date = datetime.date(2011, M, D)
    day_of_week = date.weekday()  # 0=Monday, 1=Tuesday, ...
    
    results.append(days[day_of_week])

print(" ".join(results))
