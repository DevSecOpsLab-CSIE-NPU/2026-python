# AI Easy 版: 10929 You can say 11
import sys

def solve():
    """
    判斷輸入的大數（最多 1000 位）是否為 11 的倍數。
    解法：使用逐位餘數法，避免大數直接轉 int 導致效能問題。
    """
    for line in sys.stdin:
        n_str = line.strip()
        if n_str == "0": break

        rem = 0
        for char in n_str:
            rem = (rem * 10 + int(char)) % 11

        if rem == 0:
            print(f"{n_str} is a multiple of 11.")
        else:
            print(f"{n_str} is not a multiple of 11.")

if __name__ == "__main__":
    solve()
