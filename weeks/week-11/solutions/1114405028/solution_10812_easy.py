"""UVA 10812 — Beat the Spread! 簡單版本"""


def solve_simple(s, d):
    """最簡單的解法"""
    if (s + d) % 2 != 0:
        return "impossible"

    big = (s + d) // 2
    small = (s - d) // 2

    if small < 0:
        return "impossible"

    return f"{big} {small}"


if __name__ == "__main__":
    print(solve_simple(40, 20))  # 30 10
    print(solve_simple(20, 40))  # impossible
    print(solve_simple(10, 2))   # 6 4
