from datetime import datetime

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
             'Friday', 'Saturday', 'Sunday']

t = int(input())

for _ in range(t):
    m, d = map(int, input().split())

    date = datetime(2012, m, d)

    day_index = date.weekday()

    print(weekdays[day_index])