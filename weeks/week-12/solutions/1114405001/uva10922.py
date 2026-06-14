"""UVA 10922 - 2 the 9s"""


def nine_degree(num_str: str) -> int:
    # 先判斷是否為 9 的倍數，不是就直接回傳 0。
    first_sum = sum(int(ch) for ch in num_str)
    if first_sum % 9 != 0:
        return 0

    degree = 1
    current = first_sum
    while current != 9:
        current = sum(int(ch) for ch in str(current))
        degree += 1
    return degree


def solve(data: str) -> str:
    out = []
    for line in data.splitlines():
        s = line.strip()
        if not s:
            continue
        if s == "0":
            break

        deg = nine_degree(s)
        if deg == 0:
            out.append(f"{s} is not a multiple of 9.")
        else:
            out.append(f"{s} is a multiple of 9 and has 9-degree {deg}.")

    return "\n".join(out)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
