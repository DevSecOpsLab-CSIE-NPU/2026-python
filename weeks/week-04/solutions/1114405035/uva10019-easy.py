# UVA 10019 - Funny Encryption Method (簡單好記版)
# 學生：1114405035 賴彥廷

import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    
    for m_str in data[1:]:
        # b1: 十進位轉二進位算 1
        b1 = bin(int(m_str)).count('1')
        
        # b2: 十六進位轉二進位算 1
        # int(m_str, 16) 會把 "265" 當成 0x265
        b2 = bin(int(m_str, 16)).count('1')
        
        print(f"{b1} {b2}")

if __name__ == "__main__":
    solve()
