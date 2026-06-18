# 10931 UVA Parity 簡易版
# 這個版本直接把整數轉成二進位，並計算 1 的個數。

def solve() -> None:
    import sys

    for line in sys.stdin:
        s = line.strip()
        if not s:
            continue
        if s == "0":
            break

        n = int(s)
        b = format(n, "b")
        ones = b.count("1")
        sys.stdout.write(f"The parity of {b} is {ones} (mod 2).\n")


if __name__ == "__main__":
    solve()
