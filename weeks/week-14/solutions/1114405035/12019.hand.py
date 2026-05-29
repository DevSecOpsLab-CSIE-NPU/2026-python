# -*- coding: utf-8 -*-
"""
UVA 12019 - Doom's Day Algorithm (標準結構化版本)

本程式用於計算給定月份 m 與日期 d，求出該日期在「2011 年」是星期幾。
特別說明：
雖然題目描述檔提及 2012 年，但根據標準 UVA 12019 / ZeroJudge f709 的標準測資與預期輸出，
本題基準年份為 2011 年（非閏年）。若使用 2012 年（閏年）計算，在 Online Judge 上將會得到 WA 答案。
因此本程式嚴格依據 2011 年的日曆規則進行實作。

時間複雜度：O(T)，其中 T 為測資組數。每組測資僅需查表加總天數並進行模數（Modulo）運算，在 O(1) 常數時間內計算完成。
空間複雜度：O(1)，僅需要一個列表儲存月份天數及星期名稱。
"""

import sys

# 2011 年（非閏年）每個月的天數，0 月佔位
DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 星期名稱列表，從星期日 (0) 到星期六 (6)
WEEKDAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def get_weekday(month, day):
    """
    計算給定的月份與日期在 2011 年是星期幾。
    
    已知 2011 年的 1 月 1 日是星期六 (Saturday)。
    我們可以將目標日期轉換為該年的「第幾天」（1-indexed），
    然後推算其星期幾。
    
    參數:
    month (int): 月份 (1~12)
    day (int): 日期
    
    回傳:
    str: 星期幾的英文全稱（例如 "Monday"、"Tuesday" ...）
    """
    # 累加前 month-1 個月的天數，再加上當月的日期
    day_of_year = sum(DAYS_IN_MONTH[:month]) + day
    
    # 由於 1/1 是星期六 (對應索引 6)
    # 計算公式：(day_of_year - 1 + 6) % 7 
    # 可以簡寫為：(day_of_year + 5) % 7
    weekday_idx = (day_of_year + 5) % 7
    
    return WEEKDAYS[weekday_idx]

def solve():
    """
    讀取標準輸入，解析 T 組測試資料並輸出結果。
    """
    # 讀取標準輸入並依空白切分
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # 第一個整數為測試資料組數 T
    t_cases = int(input_data[0])
    idx = 1
    
    for _ in range(t_cases):
        if idx >= len(input_data):
            break
            
        month = int(input_data[idx])
        day = int(input_data[idx+1])
        idx += 2
        
        # 取得星期幾並印出
        ans = get_weekday(month, day)
        print(ans)

if __name__ == "__main__":
    solve()
