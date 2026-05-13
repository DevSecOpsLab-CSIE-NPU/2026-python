"""
UVA 10812 - easy 版本

這版保留最直觀公式，步驟少、容易背：
1) 先排除明顯不可能情況
2) 用公式直接算兩隊分數
"""


def solve_case(total: int, diff: int) -> str:
    # 分差不可能比總分大。
    if diff > total:
        return "impossible"

    # total + diff 要是偶數，才能平分成整數。
    if (total + diff) % 2 == 1:
        return "impossible"

    a = (total + diff) // 2
    b = (total - diff) // 2

    if a < 0 or b < 0:
        return "impossible"

    return f"{a} {b}"


def main() -> None:
    import sys

    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        return

    t = int(lines[0])
    ans = []
    for i in range(1, t + 1):
        s, d = map(int, lines[i].split())
        ans.append(solve_case(s, d))

    print("\n".join(ans))


if __name__ == "__main__":
    main()
