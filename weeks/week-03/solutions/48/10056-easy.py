import sys


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    s = int(data[0])
    idx = 1
    out = []

    for _ in range(s):
        n = int(data[idx])
        p = float(data[idx + 1])
        i = int(data[idx + 2])
        idx += 3

        if p == 0.0:
            out.append("0.0000")
            continue

        numerator = ((1.0 - p) ** (i - 1)) * p
        denominator = 1.0 - ((1.0 - p) ** n)
        ans = numerator / denominator
        out.append(f"{ans:.4f}")

    print("\n".join(out))


if __name__ == "__main__":
    main()
