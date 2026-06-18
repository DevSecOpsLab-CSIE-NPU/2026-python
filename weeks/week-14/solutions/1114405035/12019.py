# -*- coding: utf-8 -*-
import sys
import datetime

def solve():
    """
    UVA 12019 — Doom's Day Algorithm 解題主程式
    說明：
    雖然題目說明文件中提到 2012 年，但經比對官方 UVA 12019 / ZeroJudge f709 測資，
    其所代表的基準年份實為 2011 年（例如：1 月 6 日在 2011 年為星期四，在 2012 年為星期五；而測資預期輸出為 Thursday）。
    因此本解法以 2011 年為基準年份進行計算。
    """
    # 讀起所有的輸入 token
    tokens = sys.stdin.read().split()
    if not tokens:
        return
        
    num_cases = int(tokens[0])
    idx = 1
    
    for _ in range(num_cases):
        m = int(tokens[idx])
        d = int(tokens[idx+1])
        idx += 2
        
        # 建立 2011 年的日期物件
        date_obj = datetime.date(2011, m, d)
        
        # strftime("%A") 可以取得星期幾的英文全稱（例如 "Monday", "Tuesday" 等）
        day_of_week = date_obj.strftime("%A")
        print(day_of_week)

if __name__ == "__main__":
    solve()
