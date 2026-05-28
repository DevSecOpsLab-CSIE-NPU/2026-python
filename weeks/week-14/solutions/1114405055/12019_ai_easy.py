import sys, datetime

data = sys.stdin.read().split()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# 第一項是測資數量，後續為配對的月份與日期
for i in range(1, len(data)-1, 2):
    m, d = int(data[i]), int(data[i+1])
    # 運用 datetime 模組取得 2011 年的星期索引
    print(days[datetime.date(2011, m, d).weekday()])
