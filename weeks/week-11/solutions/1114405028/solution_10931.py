"""
UVA 10931 — Parity 解決方案
計算整數二進位表示中 1 的個數。
"""


def calculate_parity(num):
    """計算整數 num 的二進位奇偶性輸出結果字串。"""
    binary = bin(num)[2:]
    ones = binary.count("1")
    return f"The parity of {binary} is {ones} (mod 2)."


def main():
    while True:
        n = int(input().strip())
        if n == 0:
            break
        print(calculate_parity(n))


if __name__ == "__main__":
    main()
