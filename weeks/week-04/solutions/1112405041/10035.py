# 10035.py
import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return

    idx = 0
    while idx + 1 < len(data):
        a_str = data[idx]
        b_str = data[idx+1]
        idx += 2

        if a_str == '0' and b_str == '0':
            break

        a = list(map(int, a_str.zfill(11)[::-1]))
        b = list(map(int, b_str.zfill(11)[::-1]))

        carries = 0
        c = 0
        for i in range(11):
            if a[i] + b[i] + c >= 10:
                carries += 1
                c = 1
            else:
                c = 0

        # UVA 10035 地雷：單複數判斷
        if carries == 0:
            print("No carry operation.")
        elif carries == 1:
            print("1 carry operation.")
        else:
            print(f"{carries} carry operations.")

if __name__ == "__main__":
    solve()
