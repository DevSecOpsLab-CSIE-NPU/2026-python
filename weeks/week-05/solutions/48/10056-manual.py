import sys


def win_probability(n: int, p: float, i: int) -> float:
    if p == 0.0:
        return 0.0

    first_round = ((1.0 - p) ** (i - 1)) * p
    cycle_fail = (1.0 - p) ** n
    return first_round / (1.0 - cycle_fail)


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = float(data[idx])
        idx += 1
        i = int(data[idx])
        idx += 1

        out.append(f"{win_probability(n, p, i):.4f}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
