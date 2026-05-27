import datetime

def get_doomsday_date(month):
    """获取该月的doomsday日期"""
    if month == 1:
        return (1, 10)  
    elif month == 2:
        return (2, 21)  
    elif month == 3:
        return (3, 7)  
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


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

T = int(input())
results = []
for _ in range(T):
    M, D = map(int, input().split())
    
    date = datetime.date(2011, M, D)
    day_of_week = date.weekday()  
    
    results.append(days[day_of_week])

print(" ".join(results))
