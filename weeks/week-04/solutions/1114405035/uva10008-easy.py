# UVA 10008 - What's Cryptanalysis? (簡單好記版)
# 學生：1114405035 賴彥廷

import sys
from collections import Counter

def solve():
    # 讀取所有輸入並轉大寫
    input_text = sys.stdin.read().upper()
    
    # 過濾出字母並計數
    counts = Counter(c for c in input_text if c.isalpha())
    
    # 排序：次數由大到小 (-x[1])，字母由小到大 (x[0])
    sorted_res = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    for char, count in sorted_res:
        print(f"{char} {count}")

if __name__ == "__main__":
    solve()
