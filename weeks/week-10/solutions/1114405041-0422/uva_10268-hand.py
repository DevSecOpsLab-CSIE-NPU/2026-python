import sys


def build_table():
    table = [[0] * 101 for _ in range(64)]
    limit = 10**19
    for t in range(1, 64):
        for k in range(1, 101):
            value = table[t - 1][k - 1] + 1 + table[t - 1][k]
            table[t][k] = value if value < limit else limit
    return table


TABLE = build_table()


def solve(data):
    vals = data.split()
    i = 0
    out = []

    while i + 1 < len(vals):
        k = int(vals[i])
        n = int(vals[i + 1])
        i += 2
        if k == 0:
            break

        k = min(k, 100)
        best = None
        for t in range(1, 64):
            if TABLE[t][k] >= n:
                best = t
                break

        if best is None:
            out.append("More than 63 trials needed.")
        else:
            out.append(str(best))

    return "\n".join(out)


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
