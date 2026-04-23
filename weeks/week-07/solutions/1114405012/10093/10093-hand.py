"""10093 easy 手打版。"""

import sys


def bit_count(x: int) -> int:
    return bin(x).count("1")


def solve(input_data: str) -> str:
    data = input_data.split()
    if not data:
        return ""

    n = int(data[0])
    m = int(data[1])
    rows = data[2 : 2 + n]

    plains = []
    for r in rows:
        mask = 0
        for j, ch in enumerate(r):
            if ch == "P":
                mask |= 1 << j
        plains.append(mask)

    states = []
    for mask in range(1 << m):
        if (mask & (mask << 1)) == 0 and (mask & (mask << 2)) == 0:
            states.append(mask)

    cnt = [bit_count(s) for s in states]

    valid = []
    for i in range(n):
        row_ok = []
        for idx, st in enumerate(states):
            if (st & ~plains[i]) == 0:
                row_ok.append(idx)
        valid.append(row_ok)

    dp = {(0, 0): 0}
    for i in range(n):
        nxt = {}
        for (p1, p2), score in dp.items():
            s1 = states[p1]
            s2 = states[p2]
            for c in valid[i]:
                sc = states[c]
                if (sc & s1) != 0:
                    continue
                if (sc & s2) != 0:
                    continue
                key = (c, p1)
                val = score + cnt[c]
                if key not in nxt or val > nxt[key]:
                    nxt[key] = val
        dp = nxt

    return str(max(dp.values()) if dp else 0)


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        print(out)


if __name__ == "__main__":
    main()
