import sys


def solve(data: str) -> str:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    t = int(lines[0])
    p = 1
    out = []
    for case in range(1, t + 1):
        n = int(lines[p].split("=")[1])
        p += 1
        arr = []
        for _ in range(n):
            arr.extend(map(int, lines[p].split()))
            p += 1
        ok = all(x >= 0 for x in arr) and arr == arr[::-1]
        out.append(f"Test #{case}: {'Symmetric.' if ok else 'Non-symmetric.'}")
    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
