# -*- coding: utf-8 -*-
import sys
import datetime

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    for _ in range(t):
        m, d = int(data[idx]), int(data[idx+1])
        idx += 2
        
        # 利用 2011 年日期進行轉換
        dt = datetime.date(2011, m, d)
        print(dt.strftime("%A"))

if __name__ == "__main__":
    solve()
