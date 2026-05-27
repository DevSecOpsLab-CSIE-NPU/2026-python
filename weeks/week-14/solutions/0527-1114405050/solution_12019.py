import sys
import datetime

def solve():
    """
    UVA 12019 - Doom's Day Algorithm
    題目要求：給定 2012 年的月份與日期，輸出該日是星期幾。
    2012 年是閏年（2 月有 29 天）。
    """
    # 讀取所有輸入資料
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # 第一個數字是測試資料的組數 T
    T = int(input_data[0])
    
    # 星期幾的英文全名列表
    # Python 的 datetime.date.weekday() 回傳 0=Monday, 1=Tuesday, ..., 6=Sunday
    weekdays = [
        "Monday", "Tuesday", "Wednesday", "Thursday", 
        "Friday", "Saturday", "Sunday"
    ]
    
    idx = 1
    for _ in range(T):
        # 讀取月份 m 與日期 d
        m = int(input_data[idx])
        d = int(input_data[idx + 1])
        idx += 2
        
        # 使用 datetime 建立日期物件 (指定為 2012 年)
        # 此方法會自動處理閏年與日期合法性
        dt = datetime.date(2012, m, d)
        
        # 取得星期索引並輸出對應的名稱
        print(weekdays[dt.weekday()])

if __name__ == '__main__':
    solve()