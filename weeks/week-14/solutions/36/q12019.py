# Doom's Day Algorithm 解答程式
# 題目 12019: UVA — Doom's Day Algorithm
# 計算2012年任意日期是星期幾

from datetime import datetime, timedelta

def get_day_of_week(month, day):
    """
    獲取2012年指定月份和日期是星期幾
    
    參數:
        month: 月份 (1-12)
        day: 日期
    
    返回:
        星期名稱 (Monday, Tuesday, ..., Sunday)
    """
    # 2012年1月1日是星期日
    date = datetime(2012, month, day)
    
    # 星期名稱對應表 (datetime.weekday()中0=Monday, 6=Sunday)
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                'Friday', 'Saturday', 'Sunday']
    
    return weekdays[date.weekday()]

def main():
    """
    主程式：讀取輸入並輸出結果
    """
    t = int(input())
    
    for _ in range(t):
        m, d = map(int, input().split())
        result = get_day_of_week(m, d)
        print(result)

if __name__ == '__main__':
    main()
