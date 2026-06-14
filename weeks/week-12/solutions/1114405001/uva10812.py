"""UVA 10812 - Beat the Spread!"""


def solve(data: str) -> str:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    t = int(lines[0])
    out = []

    for i in range(1, t + 1):
        s, d = map(int, lines[i].split())

        # 若差大於和，或 (s + d) 非偶數，無法得到兩個非負整數分數。
        if d > s or (s + d) % 2 != 0:
            out.append("impossible")
            continue

        high = (s + d) // 2
        low = (s - d) // 2

        if high < 0 or low < 0:
            out.append("impossible")
        else:
            out.append(f"{high} {low}")

    return "\n".join(out)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
