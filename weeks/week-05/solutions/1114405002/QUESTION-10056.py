import sys


def solve(data: bytes) -> str:
    parts = data.split()
    if not parts:
        return ""

    s = int(parts[0])
    idx = 1
    out = []

    for _ in range(s):
        n = int(parts[idx])
        p = float(parts[idx + 1])
        i = int(parts[idx + 2])
        idx += 3

        if p == 0.0:
            out.append("0.0000")
            continue

        first = ((1.0 - p) ** (i - 1)) * p
        loop = (1.0 - p) ** n
        ans = first / (1.0 - loop)
        out.append(f"{ans:.4f}")

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.buffer.read()))
