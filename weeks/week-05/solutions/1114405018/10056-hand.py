import sys

def one_case(n: int, p: float, i: int) -> float:
    if p == 0.0:
        return 0.0

    q = 1.0 - p
    return (p * (q ** (i - 1))) / (1.0 - (q ** n))

def main() -> None:
    data = sys.stdin.read().split()
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

        out.append(f"{one_case(n, p, i):.4f}")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
    