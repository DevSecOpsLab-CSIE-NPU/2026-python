import sys
import datetime

def process():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for _ in range(t):
        m = int(data[idx])
        d = int(data[idx+1])
        idx += 2
        dt = datetime.datetime(2011, m, d)
        print(days[dt.weekday()])

if __name__ == '__main__':
    process()
