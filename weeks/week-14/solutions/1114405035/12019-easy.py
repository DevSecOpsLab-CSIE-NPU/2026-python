# -*- coding: utf-8 -*-
"""
12019 Doom's Day Algorithm —— 簡單易記版

核心邏輯：
1. 雖然題目描述中寫 2012 年，但實際 UVA/ZJ 標準測資均是基於「2011 年」。
2. 利用 Python 內建的 `datetime` 模組，不需要手動計算天數加總與餘數，直接得出星期幾。
3. 使用 `datetime.date(2011, m, d).strftime("%A")`，其中 `%A` 格式化代碼可以直接輸出英文星期全稱，如 "Monday"、"Tuesday"。

此版本非常精簡、優雅，在 CPE 考試中幾乎沒有寫錯的風險，最容易記憶！
"""

import sys
import datetime

def solve():
    # 一次性讀取標準輸入中的所有資料，並切分成整數列表
    data = [int(x) for x in sys.stdin.read().split()]
    if not data:
        return
        
    # 第一個整數為測資組數 T
    t_cases = data[0]
    idx = 1
    
    for _ in range(t_cases):
        m = data[idx]
        d = data[idx + 1]
        idx += 2
        
        # 建立 datetime 物件，直接將 2011 年的日期轉化為星期全稱 (%A)
        target_date = datetime.date(2011, m, d)
        print(target_date.strftime("%A"))

if __name__ == "__main__":
    solve()
