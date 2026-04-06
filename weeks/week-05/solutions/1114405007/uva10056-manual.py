from sys import stdin


def main():
    data = stdin.read().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        p = float(data[idx + 1])
        i = int(data[idx + 2])
        idx += 3

        if p == 0:
            out.append("0.0000")
            continue

        first = ((1 - p) ** (i - 1)) * p
        all_fail = (1 - p) ** n
        ans = first / (1 - all_fail)
        out.append(f"{ans:.4f}")

    print("\n".join(out))


if __name__ == "__main__":
    main()