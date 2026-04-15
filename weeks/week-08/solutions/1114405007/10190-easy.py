"""UVA 10190 - easy 版本（含中文註解）。"""

import sys


def build_sequence(n: int, m: int):
    # 題目要求要一直整除到 1，否則就是 Boring!
    if n < 2 or m < 2:
        return None

    seq = [n]
    while n > 1:
        if n % m != 0:
            return None
        n //= m
        seq.append(n)

    return seq if seq[-1] == 1 else None


def solve(data: str) -> str:
    out = []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        n, m = map(int, line.split())
        seq = build_sequence(n, m)
        if seq is None:
            out.append("Boring!")
        else:
            out.append(" ".join(map(str, seq)))
    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
