# UVA 10035 - Primary Arithmetic (簡單好記版)
# 學生：1114405035 賴彥廷

import sys

def solve():
    lines = sys.stdin.read().splitlines()
    for line in lines:
        a, b = map(int, line.split())
        if a == 0 and b == 0: break
        
        carries = 0
        carry_in = 0
        while a > 0 or b > 0:
            # 取出最後一位相加
            if (a % 10 + b % 10 + carry_in) >= 10:
                carries += 1
                carry_in = 1
            else:
                carry_in = 0
            a //= 10
            b //= 10
            
        if carries == 0:
            print("No carry operation.")
        elif carries == 1:
            print("1 carry operation.")
        else:
            print(f"{carries} carry operations.")

if __name__ == "__main__":
    solve()
