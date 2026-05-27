import sys

def solve():
    # 一次性讀取所有資料並轉換為整數陣列
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
        
    T = data[0]
    
    # 2012 是閏年，2 月有 29 天。
    # 刻意在最前面補一個 0，這樣 1 月就可以直接對應 days_in_month[1]，非常直覺。
    days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 陣列對應技巧：
    # 2012/1/1 是星期日。總天數 = 0 + 1 = 1。如果 1 % 7 要對應星期日，那麼索引 1 必須放 "Sunday"。
    # 因此索引 0 就放 "Saturday"。
    weekdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    idx = 1
    for _ in range(T):
        m = data[idx]
        d = data[idx+1]
        idx += 2
        
        # 核心邏輯：計算這天是 2012 年的第幾天
        # sum(days_in_month[:m]) 可以把當前月份「之前」的所有天數加總
        # 再加上當月的日期 d，就是總天數
        total_days = sum(days_in_month[:m]) + d
        
        # 取餘數對應星期幾並輸出
        print(weekdays[total_days % 7])

if __name__ == '__main__':
    solve()