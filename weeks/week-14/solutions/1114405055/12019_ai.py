# UVA 12019 - Doom's Day Algorithm (AI 版本)
import sys
import datetime

def solve():
    # 讀取輸入資料
    data = sys.stdin.read().split()
    if not data:
        return
        
    t = int(data[0]) # 資料組數
    idx = 1
    
    # 對應的星期幾名稱陣列
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    for _ in range(t):
        m = int(data[idx])
        d = int(data[idx+1])
        idx += 2
        
        # 2011 年的日期，利用 datetime 來取得星期幾
        # 注意: UVa 原題年份為 2011 年
        dt = datetime.datetime(2011, m, d)
        print(days[dt.weekday()])

if __name__ == '__main__':
    solve()
