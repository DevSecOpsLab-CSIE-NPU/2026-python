# AI Easy 版: 10922 2 the 9s
import sys

def solve():
    """
    判斷數字是否為 9 的倍數並計算其 9-degree (遞迴位數和直到等於 9)。
    """
    for line in sys.stdin:
        s = line.strip()
        if s == "0": break

        n_str = s
        degree = 0
        is_multiple = False

        while True:
            val = sum(int(c) for c in n_str)
            degree += 1
            if val == 9:
                is_multiple = True; break
            if val < 9 or val % 9 != 0:
                break
            n_str = str(val)

        if is_multiple:
            print(f"{s} is a multiple of 9 and has 9-degree {degree}.")
        else:
            print(f"{s} is not a multiple of 9.")

if __name__ == "__main__":
    solve()
