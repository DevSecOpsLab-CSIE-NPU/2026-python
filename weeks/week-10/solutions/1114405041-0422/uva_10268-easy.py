from __future__ import annotations

import sys


def build_table() -> list[list[int]]:
    """
    公式好記版：
    table[t][k] = table[t-1][k-1] + 1 + table[t-1][k]
    代表：
    - 這層丟下去會破：往下查 table[t-1][k-1]
    - 這層丟下去不破：往上查 table[t-1][k]
    - +1 是目前這一層
    """
    table = [[0] * 101 for _ in range(64)]
    limit = 10**19
    for t in range(1, 64):
        for k in range(1, 101):
            value = table[t - 1][k - 1] + 1 + table[t - 1][k]
            table[t][k] = value if value < limit else limit
    return table


TABLE = build_table()


def solve(data: str) -> str:
    vals = data.split()
    i = 0
    out: list[str] = []

    while i + 1 < len(vals):
        k = int(vals[i])
        n = int(vals[i + 1])
        i += 2

        if k == 0:
            break

        best = None
        k = min(k, 100)
        for t in range(1, 64):
            if TABLE[t][k] >= n:
                best = t
                break

        if best is None:
            out.append("More than 63 trials needed.")
        else:
            out.append(str(best))

    return "\n".join(out)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
