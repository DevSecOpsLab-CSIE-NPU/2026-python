# AI Easy 版: 10931 Parity
import sys

def solve():
    """
    計算整數 i 的二進位表示中 1 的個數（即 Parity）。
    使用 Python 3.10+ 的 bit_count() 以顯高手風格。
    """
    for line in sys.stdin:
        try:
            i = int(line.strip())
        except ValueError: continue
        if i == 0: break

        binary_str = bin(i)[2:]
        parity_count = i.bit_count() # 進階寫法

        print(f"The parity of {binary_str} is {parity_count} (mod 2).")

if __name__ == "__main__":
    solve()
