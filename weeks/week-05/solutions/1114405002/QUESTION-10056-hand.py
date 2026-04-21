import sys


def main() -> None:
    t = sys.stdin.buffer.read().split()
    if not t:
        return

    s = int(t[0])
    i = 1
    out = []

    for _ in range(s):
        n = int(t[i])
        p = float(t[i + 1])
        k = int(t[i + 2])
        i += 3

        if p == 0.0:
            out.append("0.0000")
            continue

        a = ((1.0 - p) ** (k - 1)) * p
        q = (1.0 - p) ** n
        out.append(f"{a / (1.0 - q):.4f}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
